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
    list: function () {
        $('#tblProducts').DataTable({
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
                        return '<input type="text" name="cantidad" class="form-control form-control-sm" autocomplete="off" value="' + row.cantidad + '">';
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
        step: 0.1,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    })
    $("input[name='descuento']").TouchSpin({
        min: 0,
        max: 100,
        step: 0.1,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
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
        select: function (event, ui) {
            event.preventDefault();
            ui.item.cantidad = 1;
            ui.item.subtotal = 0.00;
            ventas.items.productos.push(ui.item);
            ventas.list();
            $(this).val('');

        }
    });
});
