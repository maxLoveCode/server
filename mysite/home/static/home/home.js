$(document).ready(function(){
    $(".tagline").click(function(){

        $(".fullscreen-bg__video").play();
        alert("play");
    });

    $(".fullscreen-bg__video").bind('ended', function(){
        this.play();
    });

    $(".fullscreen-bg__video").bind('play', function(){
    });

    $(".fullscreen-bg__video").click(function(){
    });
});

