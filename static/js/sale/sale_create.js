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
    add: function () {
        
    }
};
//-------------datetimepicker----------------- 
$(function () {
    $('#fecha_venta').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        maxDate: moment().format('YYYY-MM-DD')
    });
});

//-------------TouchSpin-----------------------
$(function () {
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
});

//-------------Select2-----------------------
$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });
})