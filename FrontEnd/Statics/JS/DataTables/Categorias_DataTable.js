const eliminarRegistro = (redireccion) => {
    Swal.fire({
        title: "¿Estas seguro?",
        text: "Una vez borrado no podras recuperar este registro",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href=redireccion;
        }
    });
}

new gridjs.Grid({
    search: true,
    columns: [
        { name: "ID Categoria", sort: true }, 
        { name: "Nombre", sort: true }, 
        { name: 'Acciones', width: '15%', formatter: (cell, row) => {
                if (row.cells[2].data == null) {
                    return gridjs.html(`
                        <i class="fa-solid fa-pencil mx-1 btn btn-small btn-warning text-white" onclick="window.location.href='/Categorias/EditarCategoria/${row.cells[0].data}'"></i>
                        <i class="fa-solid fa-trash mx-1 btn btn-small btn-danger" onclick="eliminarRegistro('/Categorias/EliminarCategoria/${row.cells[0].data}')"></i>
                        `)
                } else {
                    return 'No hay datos'
                }
            }
        },
    ],
    className:{
        container: 'table-responsive',
        thead: 'text-center',
        tbody: 'text-center' 
    },
    pagination: {
        limit: 5,
        summary: true
    },
    //Configurando el lenguaje
    language: {
        search: {
            placeholder: 'Buscar 🔍'
        },
        sort: {
            sortAsc: 'Orden de columna ascendente.',
            sortDesc: 'Orden de columna descendente.',
        },
        pagination: {
            previous: 'Anterior',
            next: 'Siguiente',
            navigate: (page, pages) => `Página ${page} de ${pages}`,
            page: (page) => `Página ${page}`,
            showing: 'Mostrando del',
            of: 'de',
            to: 'al',
            showing: '😃 Mostrando',
            results: () => 'Registros'
        },
        loading: 'Cargando...',
        noRecordsFound: 'Sin coincidencias encontradas.',
        error: 'Ocurrió un error al obtener los datos, clic en el boton buscar.',
    },
    //Obteniendo datos del controlador
    server: {
        url: 'http://127.0.0.1:8000/Categorias/ObtenerCategorias',
        then: data => data.ListaCategorias.map(categoria => 
            [categoria.pk, categoria.fields.Nombre_Categoria, categoria.Estado]
        ),
    }

}).render(document.getElementById("Tabla_Categorias"));


