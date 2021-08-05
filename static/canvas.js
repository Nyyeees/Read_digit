window.addEventListener('load', () => {
    let openmenu = document.getElementsByClassName('icon')[0]
    let dropmenu = document.getElementsByClassName('drop-menu')[0]
    
    document.body.addEventListener('click', function(e){
      if(e.target === openmenu){
        dropmenu.style.left = '0';
      }
      else if (!dropmenu.contains(e.target)){

        dropmenu.style.left='-300%';
      }
    })
    const canvas = document.querySelector('canvas');  
    const ctx = canvas.getContext('2d');
    //canvas size
    canvas.width = 310;
    canvas.height = 300;
    canvas.style.top = 20;
    ctx.fillStyle = 'black';
    ctx.fillRect(0,0,canvas.width,canvas.height);
    
    //variables
    let painting = false;

    function startingPos(e){
        painting = true;
        paint(e);
    }

    function endPos(){
        painting = false;
        ctx.beginPath();
    }

    function paint(e){
        if (!painting) {return;}

        ctx.lineWidth = 13;
        ctx.lineCap = 'round';
        ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
        ctx.strokeStyle = 'white';
        ctx.stroke();
    }
    //EventListeners
    canvas.addEventListener('mousedown', startingPos);
    canvas.addEventListener('mouseup', endPos);
    canvas.addEventListener('mousemove', paint);
    //clear button
    let clear = document.getElementsByClassName('clear')[0];
    clear.onclick = () =>{
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = 'black';
      ctx.fillRect(0,0,canvas.width,canvas.height);
    }
    
    //Save image(predict)


});

let p = document.getElementsByClassName('predict')[0];   
p.onclick = function() {
    var dataURL = canvas.toDataURL();
    $('#result').text('......');
    $.ajax({
      type: 'POST',
      url: '/process',
      data: {
          imageBase64 : dataURL
      },
      success: function(data){
          $('#result').text(data);
      }              
  });                     

 };

