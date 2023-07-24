//Envio Formulario Contacto
   
const btn = document.getElementById('button-contacto');
const nombre = document.getElementById('nombre');
const correo = document.getElementById('correo');
const celular = document.getElementById('celular');
const mensaje = document.getElementById('mensaje');

btn.addEventListener("click", enviarDatos);

function enviarDatos(event) {
    event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario


    const datos = {
        nombre: nombre.value,
        correo: correo.value,
        celular: celular.value,
        mensaje: mensaje.value
    };

    // Convertir el objeto a formato JSON
    const datosJSON = JSON.stringify(datos);
    console.log(datosJSON);
    
    const url='http://127.0.0.1:5000'
     return fetch(url+'/gafas', {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: datosJSON
     })
     .then(response => response.json())
     .then(data => {
       console.log(data);
       // Borrar los campos después de enviar el formulario
       nombre.value = '';
       correo.value = '';
       celular.value = '';
       mensaje.value = '';
     })
     .catch(error => {
       console.error('Error al crear el worker:', error);
     });
}
