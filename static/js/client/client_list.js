$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            { "data": "nombre" },
            { "data": "apellido" },
            { "data": "tipo_documento" },
            { "data": "num_documento" },
            { "data": "num_telefono" },
            { "data": "email" },
            { "data": "fecha_alta" },
            { "data": "id" },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/client/detail/' + row.id + '/" class="btn btn-info btn-xs "><i class="fas fa-search"></i></a> ';
                    buttons += '<a href="/erp/client/update/' + row.id + '/" class="btn btn-success btn-xs "><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/client/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});