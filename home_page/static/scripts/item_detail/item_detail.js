$(document).ready(function(){
    var active_img_index = 0; 
    setActiveImage(active_img_index);
    $("#small-imgs").children().click(function(){
        // $(this).sub().removeAttr("class");
        // $(this).toggleClass("active");
    });
});

function setActiveImage(tag){
    //alert($("#small-imgs").children().length)
    $("#small-imgs").children().removeAttr("class");
    $("#small-imgs").children().eq(tag).toggleClass("active");
    $("#show-img").children().eq(0).html($("#small-imgs").children().eq(tag).html());
}