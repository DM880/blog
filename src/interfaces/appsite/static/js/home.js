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


function imgOnHover(post_id){
    document.getElementById('post-description-'+post_id).style.opacity = 1;
    document.getElementById('post-img-'+post_id).style.opacity = 0.5;
}

function imgOnOut(post_id){
    document.getElementById('post-description-'+post_id).style.opacity = 0;
    document.getElementById('post-img-'+post_id).style.opacity = 1;
}