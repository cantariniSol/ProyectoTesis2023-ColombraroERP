var tblProducts;

var ventas = {
    items: {
        cliente: '',
        fecha_venta: '',
        subtotal: 0.00,
        iva: 0.00,
        descuento: 0.00,
        total: 0.00,
        productos: []
    },
    calcular_factura: function () {
        var subtotal = 0.00;
        var iva = $('input[name="iva"]').val();
        var descuento = $('input[name="descuento"]').val();
        $.each(this.items.productos, (pos, dict) => {
            dict.pos = pos;
            dict.subtotal = dict.cantidad * parseFloat(dict.precio_venta);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = (this.items.subtotal * parseFloat(iva) / 100);
        this.items.descuento = (this.items.subtotal * parseFloat(descuento) / 100)
        this.items.total = (this.items.subtotal + this.items.iva) - this.items.descuento;


        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2))
        $('input[name="total"]').val(this.items.total.toFixed(2))
    },
    add: function (item) {
        this.items.productos.push(item)
        this.list();
    },
    list: function () {
        this.calcular_factura();
        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.productos,
            columns: [
                { "data": "id" },
                { "data": "nombre" },
                { "data": "categoria.nombre" },
                { "data": "precio_venta" },
                { "data": "cantidad" },
                { "data": "subtotal" },
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat rounded"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cantidad + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {
                $(row).find('input[name="cantidad"]').TouchSpin({
                    min: 1,
                    max: 100000000,
                    step: 1
                });
            },
            initComplete: function (settings, json) {

            }
        });
    }
};

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">' +
        '<div class="row">' +
        '<div class="col-lg-1">' +
        '<img src="' + repo.imagen + '" class="img-fluid img-thumbnail d-block mx-auto rounded">' +
        '</div>' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>Artículo:</b> ' + repo.articulo + '<br>' +
        '<b>Nombre:</b> ' + repo.nombre + '<br>' +
        '<b>Precio Venta:</b> <span class="badge badge-warning">$' + repo.precio_venta + '</span>' +
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');

    return option;
}




$(function () {
    //-------------datetimepicker----------------- 
    $('#fecha_venta').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        maxDate: moment().format('YYYY-MM-DD')
    });

    //-------------TouchSpin-----------------------
    $("input[name='iva']").TouchSpin({
        min: 0,
        max: 100,
        step: 5,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    }).on('change', function () {
        ventas.calcular_factura();
    })


    $("input[name='descuento']").TouchSpin({
        min: 0,
        max: 100,
        step: 5,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    }).on('change', function () {
        ventas.calcular_factura();
    })

    //-------------Search Cliente--------------------
    $('select[name="cliente"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_clients'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el nombre de un cliente',
        minimumInputLength: 1
    });

    //------------Modal Crear nuevo Cliente-----------------
    $('.btnAddClient').on('click', function () {
        $('#myModalClient').modal('show');
    });

    $('#myModalClient').on('hidden.bs.modal', function (e) {
        $('#frmClientes').trigger('reset');
    })

    //--------------Guardar Cliente ---------------------
    $('#frmClientes').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_client');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Esta segura/o de crear un nuevo cliente?', parameters, function (response) {
                //console.log(response);
                var newOption = new Option(response.full_name, response.id, false, true);
                $('select[name="cliente"]').append(newOption).trigger('change');
                $('#myModalClient').modal('hide');
            });
    });

    // $('.btnAddClient').on('click', function () {
    //     $('#myModalClient').modal('show');
    // });

    $('#myModalClient').modal('show');
    //---------------- Evento Eliminar --------------------
    $('.btnRemoveAll').on('click', function () {
        if (ventas.items.productos.length === 0) return false;
        alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?',
            function () {
                ventas.items.productos = [];
                ventas.list();
            }, function () {

            });
    });

    //---------------- Evento Cantidad --------------------
    $('#tblProducts tbody')
        //---------- Eliminar Producto -----------------------------
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?',
                function () {
                    ventas.items.productos.splice(tr.row, 1);
                    ventas.list();
                }, function () {

                });
        })
        //--------- Agregar Cantidad de productos ---------------------
        .on('change', "input[name='cantidad']", function () {
            var cantidad = parseInt($(this).val());
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            ventas.items.productos[tr.row].cantidad = cantidad;
            ventas.calcular_factura();
            $('td:eq(5)', tblProducts.row(tr.row).node()).html('$' + ventas.items.productos[tr.row].subtotal.toFixed(2));
        });

    //--------------Guardar Factura ---------------------
    $('#frmVentas').on('submit', function (e) {
        e.preventDefault();
        if (ventas.items.productos.length == 0) {
            message_error('Debe al menos tener un item en su deatalle de venta');
            return false;
        }
        ventas.items.fecha_venta = $('input[name="fecha_venta"]').val();
        ventas.items.cliente = $('select[name="cliente"]').val();

        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('ventas', JSON.stringify(ventas.items));

        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {
                alert_action('Notificación', '¿Desea imprimir la boleta de venta?', function () {
                    window.open('/erp/sale/invoice/pdf/' + response.id + '/', '_blank');
                    location.href = '/erp/sale/list/';
                }, function () {
                    location.href = '/erp/sale/list/';
                });
            });
    });

    //-------------Search-------------------------
    $('select[name="search"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_products'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese el nombre de un producto',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        data.cantidad = 1;
        data.subtotal = 0.00;
        ventas.add(data);
        $(this).val('').trigger('change.select2');
    });

    ventas.list();
});


