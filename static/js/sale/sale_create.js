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

    //-------------Select2-----------------------
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    //-------------Search-------------------------
    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 100,
        autoFocus: true,
        minLength: 0,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cantidad = 1;
            ui.item.subtotal = 0.00;
            ui.item.total = 0.00;
            ui.item.iva = 0.00;
            ui.item.descuento = 0.00;
            ventas.add(ui.item);
            ventas.list();
            $(this).val('');
        }
    });


    //---------------- Evento Eliminar --------------------
    $('.btnRemoveAll').on('click', function () {
        if (ventas.items.productos.length === 0) return false;
        alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?', function () {
            ventas.items.productos = [];
            ventas.list();
        });
    });

    //---------------- Evento Cantidad --------------------
    $('#tblProducts tbody')
        //---------- Eliminar Producto -----------------------------
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblProducts.cell($(this).closest('td, li')).index();
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?', function () {
                ventas.items.productos.splice(tr.row, 1);
                ventas.list();
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
    $('form').on('submit', function (e) {
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

        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/erp/home/';
        });
    });

    ventas.list();
});


