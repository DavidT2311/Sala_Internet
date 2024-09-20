document.addEventListener('DOMContentLoaded', () => {
    let contenedor_mensaje = document.getElementById('activador_alerta');
    let titulo = document.getElementById('mensaje_1');
    let mensaje = document.getElementById('mensaje_2');
    let tipo = document.getElementById('mensaje_3')
    
    if (contenedor_mensaje && mensaje) {
        let titulo_completo = titulo.textContent;
        let mensaje_completo = mensaje.textContent;
        let tipo_completo = tipo.textContent;

        if (tipo_completo == 'success') {
            Swal.fire({
                title: titulo_completo,
                text: mensaje_completo,
                icon: 'success',
                confirmButtonText: 'Continuar'
            });
        }
        if (tipo_completo == 'error') {
            Swal.fire({
                title: titulo_completo,
                text: mensaje_completo,
                icon: 'error',
                confirmButtonText: 'Continuar'
            });
        }
    }
});

