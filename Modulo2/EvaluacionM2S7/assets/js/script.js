var opcion = prompt("¡Hola! Soy Eva, tu asistente virtual del Servicio al Cliente de Mentel. Estoy aquí para ayudarte en lo que necesites.\nEscribe el número de la opción que buscas: \n1.- Boletas y Pagos \n2.- Señal y llamadas \n3.- Oferta comercial  \n4.- Otras consultas")

//FUNCIONES
switch (parseInt(opcion)) {
    case 1:
        var subOpcion = prompt("Seleccione una opción: \n1.- Ver Boleta \n2.- Pagar cuenta")
        if (parseInt(subOpcion) === 1) {
            alert("Haga clic aquí para descargar su boleta");
        } else if (parseInt(subOpcion) === 2) {
            alert("Usted está siendo transferido. Espere por favor...");
        } else {
            alert("Opción no válida. Por favor, intente de nuevo.");
        } 
        break;
    case 2:
        var subOpcion = prompt("Seleccione una opción: \n1.- Problemas con la señal \n2.- Problemas con las llamadas")
        if (parseInt(subOpcion) === 1 || parseInt(subOpcion) === 2) {
            var solicitud = prompt("A continuación escriba su solicitud");
            if (solicitud !== null) {
                alert("Estimado usuario, su solicitud: '" + solicitud + "' Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos");
            }
        }
        break;
    case 3:
        var subOpcion = prompt("¡Mentel tiene una oferta comercial acorde a tus necesidades! Para conocer más información y ser asesorado personalmente por un ejecutivo escribe 'SI' y un ejecutivo te llamará. De lo contrario ingrese 'NO'")
        if (subOpcion === "SI" || subOpcion === "si") {
            alert("Un ejecutivo contactará con usted");
        } else if (subOpcion === "NO" || subOpcion === "no") {
            alert("Gracias por preferir nuestros servicios")
        } else {
            alert("Opción no válida. Por favor, intente de nuevo.");
        }
        break
    case 4:
        var consulta = prompt("A continuación escriba su consulta");
        if (consulta !== null) {
            alert("Estimado usuario, su consulta: '" + consulta + "' Ha sido ingresada con éxito. Pronto será contactado por uno de nuestros ejecutivos.")
        }
        break;
    default:
        alert("La opción ingresada no es válida. Gracias por preferir nuestros servicios");
        break
}