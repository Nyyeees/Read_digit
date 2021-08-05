import tensorflow as tf
from flask import Flask, request
from flask.templating import render_template
import base64
import re
import io
from PIL import Image, ImageFilter,ImageOps
import numpy as np
from load_model import model


app = Flask(__name__)

@app.route('/')
def home():
       
    return render_template('index.html')


@app.route('/process', methods=['GET','POST'])
def predict():
    result = 0
    
    image_data = request.values['imageBase64']
    image_string = re.search(r'base64,(.*)', image_data).group(1)
    decode_image = base64.b64decode(image_string)
    #Process img
    image = Image.open(io.BytesIO(decode_image)).convert('L')
    cropped_img = image.crop(image.getbbox())
    expanded_img = ImageOps.expand(cropped_img, border = 60).filter(ImageFilter.BLUR)
    processed_img = expanded_img.resize((28,28),Image.LANCZOS)
    to_array = np.array(processed_img, dtype=np.float32).reshape(1,28,28,1)
    to_array /= 255
    predictions= model.predict([to_array])
    result = np.argmax(predictions[0])
    print(result)
    return str(result)




