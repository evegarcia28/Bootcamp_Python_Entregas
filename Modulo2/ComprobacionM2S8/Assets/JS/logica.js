function mostrarMenu(){
    return prompt("Seleccione una opción:\n1.-Estado de su tarjeta \n2.-Información de saldo disponible. \n3.-Fecha de vencimiento y monto. \n4.-Ofertas vigentes. \n5.- Salir.");
}

function estado(){
    alert("Su tarjeta se encuentra Activa");
}
function saldo(){
    alert("El saldo disponible de su tarjeta es $1.500.000");
}
function vcto(){
    alert("Su fecha de vencimiento es el 30/06 y su monto a pagar es de $130.000");
}
function ofertas(){
    alert("Por el momento no tiene ofertas vigentes");
}

let opcion;
while (opcion !== "5"){
    opcion = mostrarMenu();
    switch (opcion) {
        case "1":
            estado();
            break;
        case "2":
            saldo();
            break;
        case "3":
            vcto();
            break;
        case "4":
            ofertas();
            break;
        case "5":
            alert("Gracias por su visita")
            break;
        default:
            alert("Opción no válida. Por favor elija una opción entre 1 al 5");
            break;
    }
}