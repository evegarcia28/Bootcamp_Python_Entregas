//Código inicialmente dado:
/*$(document).ready(function() {
  $(".text-body-secondary").click(function() {
    var idBoton = $("#Rio").attr("id");
    $("#detalles" + idBoton).toggle();
  });

  $(".btn-close").click(function() {
      $(".detalles").show();
  });
});
*/

//Modificaciones que hacen funcional la página de acuerdo a los requerimientos de la actividad(pdf):

$(document).ready(function() {
    $(".text-body-secondary").click(function() {
      var idBoton = $(this).attr("id");
// o lo que es similar:
//    var idBoton = $(this).closest(".text-body-secondary").attr("id");

      $("#detalles" + idBoton).toggle();
    });

    $(".btn-close").click(function() {
        $(".detalles").hide();
    });
  });