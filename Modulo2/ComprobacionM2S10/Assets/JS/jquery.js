//se coloca siempre encerrando todo el contenido para asegurar la ejecución cuando esté cargado el html

$(document).ready(function() {

//al pasar el mouse por text1 aparece text2 y al salir vuelve a desaparecer
    $("#text1").mouseenter(function(){
        $("#text2").toggle();
    })

//al hacer click en caja2 la imagen se agranda en 100% y al salir vuelve al tamaño inicial
$("#caja2").click(function(){
    $("#img").css("width", "100%");
})
$("#caja2").mouseleave(function(){
    $("#img").css("width", "30%");
})

//al hacer doble click en caja3 el tamaño de letra se agrandará
$("#caja3").dblclick(function(){
    $("#caja3").css("font-size", "2rem");
})

});