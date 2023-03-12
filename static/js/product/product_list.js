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
            { "data": "articulo" },
            { "data": "nombre" },
            { "data": "categoria.nombre" },
            { "data": "precio" },
            { "data": "stock" },
            { "data": "imagen" },
            { "data": "id" },
        ],
        columnDefs: [
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if(row.stock >= 20 ){
                        return '<span class="badge badge-success">'+data+'</span>'
                    }
                    else if (row.stock < 20 && row.stock >= 10) {
                        return '<span class="badge badge-warning">'+data+'</span>'
                    }
                    return '<span class="badge badge-danger">'+data+'</span>'
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="' + data + '" class="img-fluid d-block mx-auto rounded" style="width: 70px; height: 70px;">';
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/product/detail/' + row.id + '/" class="btn btn-info btn-xs "><i class="fas fa-search"></i></a> ';
                    buttons += '<a href="/erp/product/update/' + row.id + '/" class="btn btn-success btn-xs "><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/product/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});