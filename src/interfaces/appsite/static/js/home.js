function openPopup(){
    document.getElementById('pop-up-div').style.display = 'block';
    var div = document.getElementById('div-op-popup');
    div.style.opacity = 0.5;

    if(div.style.opacity == 0.5){
      div.addEventListener("click", function() {
        closeDiv();
      })
    }
  }

  function closeDiv(){
    document.getElementById('pop-up-div').style.display = 'none';
    document.getElementById('div-op-popup').style.opacity = 1;
  }

  setTimeout(openPopup, 5000);