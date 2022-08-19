function imgOnHover(post_id){
    document.getElementById('post-description-'+post_id).style.opacity = 1;
    document.getElementById('post-img-'+post_id).style.opacity = 0.5;
}

function imgOnOut(post_id){
    document.getElementById('post-description-'+post_id).style.opacity = 0;
    document.getElementById('post-img-'+post_id).style.opacity = 1;
}