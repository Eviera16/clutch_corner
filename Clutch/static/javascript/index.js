$(document).ready(function(){
    $(".hoverElement").hide();

    $(".box").mouseover(function(){
        $(this).find(".hoverElement").show();
    })
    $(".box").mouseout(function(){
        $(this).find(".hoverElement").hide();
    })

});