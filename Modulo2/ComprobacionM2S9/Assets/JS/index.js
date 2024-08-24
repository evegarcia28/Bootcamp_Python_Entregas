/*se muestra y oculta texto al pasar el mouse en el primer div y luego salir de él */
function mostrarMensaje() {
    document.getElementById('text2').style.display="block";
}
function ocultarMensaje(){
    document.getElementById('text2').style.display="none";
}

/*se agranda la imagen al hacer click en el div y luego vuelve a su tamaño inicial al salir del div*/
function agrandarImagen(){
    document.getElementById("caja2").style.width="90%";
}
function reducirImagen() {
    document.getElementById("caja2").style.width = "20%";
}

/*se agranda el tamaño de la letra del texto al hacer doble click en el div que lo contiene */
function agrandarLetra() {
    document.getElementById("caja3").style.fontSize = "40px";
}