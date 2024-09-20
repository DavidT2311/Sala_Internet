new gridjs.Grid({
    search: true,
    columns: [
        { name: "Codigo venta", sort: true }, 
        { name: "Codigo factura", sort: true },
        { name: "Precio", sort: true },
        { name: "Ver detalle", 
            width: '15%', formatter: (cell, row) => {
                if (row.cells[3].data == null) {
                    return gridjs.html(`
                        <i class="fa-solid fa-eye mx-1 btn btn-small btn-primary text-white" onclick="window.location.href='/VentaProductos/VerDetalleVentaProducto/${row.cells[0].data}'"></i>
                        `)
                } else {
                    return 'No hay datos'
                }
            }
        },
        { name: 'Acciones', width: '15%', formatter: (cell, row) => {
                if (row.cells[3].data == null) {
                    return gridjs.html(`
                        <i class="fa-solid fa-pencil mx-1 btn btn-small btn-warning text-white" onclick="window.location.href='/VentaProductos/EditarVentaProducto/${row.cells[0].data}'"></i>
                        <i class="fa-solid fa-trash mx-1 btn btn-small btn-danger" onclick="window.location.href='/VentaProductos/EliminarVentaProducto/${row.cells[0].data}'"></i>
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
        url: 'http://127.0.0.1:8000/VentaProductos/ObtenerVentaProductos/',
        then: data => data.ListaVentaProductos.map(ventaproducto => 
            [ventaproducto.pk, ventaproducto.fields.Codigo_Factura, ventaproducto.fields.Precio, ventaproducto.Estado]
        ),
    }

}).render(document.getElementById("Tabla_Venta_Productos"));

