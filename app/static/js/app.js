document.getElementById("crear-curso-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("/api/cursos", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            location.reload(); // Recargar la página para mostrar el nuevo curso
        } else {
            const errorData = await response.json();
            alert("Error: " + JSON.stringify(errorData));
        }
    } catch (error) {
        alert("Error al enviar el formulario: " + error.message);
    }
});
let cursoSeleccionadoId = null;

function confirmarEliminar(id, titulo) {
    cursoSeleccionadoId = id;
    UIkit.modal.confirm(`¿Estás seguro de que deseas eliminar el curso "${titulo}"?`).then(() => {
        deleteCurso(cursoSeleccionadoId);
    }).catch(() => {
        console.log("Eliminación cancelada");
    });
}

async function deleteCurso(id) {
    try {
        const response = await fetch(`/api/cursos/${id}`, {
            method: "DELETE"
        });
        if (response.ok) {
            location.reload(); // Recargar la página si se elimina correctamente
        } else {
            const errorData = await response.json();
            UIkit.notification({
                message: `Error al eliminar el curso: ${JSON.stringify(errorData)}`,
                status: 'danger',
                pos: 'top-right',
                timeout: 5000
            });
        }
    } catch (error) {
        UIkit.notification({
            message: `Error al eliminar el curso: ${error.message}`,
            status: 'danger',
            pos: 'top-right',
            timeout: 5000
        });
    }
}

// Prellenar el modal de edición con los datos del curso seleccionado
function setCursoEditar(id, titulo, descripcion, capacidad, precio) {
    // Prellenar el modal con los datos del curso seleccionado
    document.getElementById("editar-titulo").value = titulo;
    document.getElementById("editar-descripcion").value = descripcion;
    document.getElementById("editar-capacidad").value = capacidad;
    document.getElementById("editar-precio").value = precio;

    // Guardar el ID del curso en una variable global (si es necesario para otras acciones)
    cursoSeleccionadoId = id;
}

// Enviar los datos actualizados al backend
async function updateCurso() {
    const titulo = document.getElementById("editar-titulo").value;
    const descripcion = document.getElementById("editar-descripcion").value;
    const capacidad = document.getElementById("editar-capacidad").value;
    const precio = document.getElementById("editar-precio").value;

    try {
        const response = await fetch(`/api/cursos/${cursoSeleccionadoId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ titulo, descripcion, capacidad, precio }),
        });

        if (response.ok) {
            location.reload(); // Recargar la página si se actualiza correctamente
        } else {
            const errorData = await response.json();
            UIkit.notification({
                message: `Error al actualizar el curso: ${JSON.stringify(errorData)}`,
                status: 'danger',
                pos: 'top-right',
                timeout: 5000
            });
        }
    } catch (error) {
        UIkit.notification({
            message: `Error al actualizar el curso: ${error.message}`,
            status: 'danger',
            pos: 'top-right',
            timeout: 5000
        });
    }
}