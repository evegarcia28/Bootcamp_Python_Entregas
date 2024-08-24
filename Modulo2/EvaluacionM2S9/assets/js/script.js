// Array de tareas inicial
var tareas = [
    { tarea: "Pintar la fachada de la casa" },
    { tarea: "Comprar comida para el perro" },
    { tarea: "Pagar la tarjetas de crédito" }
];

// Función para mostrar el formulario
function mostrarFormulario() {
    document.getElementById('formulario').style.display = 'block';
}

// Función para ocultar el formulario
function ocultarFormulario() {
    document.getElementById('formulario').style.display = 'none';
}

// Función para agregar una tarea a la tabla
function agregarTarea() {
    var nuevaTarea = document.getElementById('nuevaTarea').value;
    if (nuevaTarea.trim() === '') {
        alert('La tarea no puede estar vacía');
        return;
    }

    var tarea = { tarea: nuevaTarea };
    tareas.push(tarea);
    renderTareas();

    document.getElementById('nuevaTarea').value = '';
}

// Función para renderizar las tareas en la tabla
function renderTareas() {
    var cuerpoTabla = document.getElementById('cuerpo-tabla');
    cuerpoTabla.innerHTML = '';

    tareas.forEach(function(item, index) {
        var fila = document.createElement('tr');

        var celdaTarea = document.createElement('td');
        celdaTarea.textContent = item.tarea;

        var celdaFinalizar = document.createElement('td');
        var botonFinalizar = document.createElement('button');
        botonFinalizar.textContent = 'Finalizar';
        botonFinalizar.className = 'btn btn-danger';
        botonFinalizar.onclick = function() {
            eliminarTarea(index);
        };

        celdaFinalizar.appendChild(botonFinalizar);
        fila.appendChild(celdaTarea);
        fila.appendChild(celdaFinalizar);
        cuerpoTabla.appendChild(fila);
    });
}

// Función para eliminar una tarea de la lista
function eliminarTarea(index) {
    tareas.splice(index, 1);
    renderTareas();
}

// Inicializa la lista de tareas al cargar la página
document.addEventListener('DOMContentLoaded', function() {
    renderTareas();
    ocultarFormulario();
});

// Asocia la función de agregar tarea al botón correspondiente
document.querySelector('#formulario button').onclick = agregarTarea;
