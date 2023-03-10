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
            { "data": "full_name" },
            { "data": "email" },
            { "data": "username" },
            { "data": "date_joined" },
            { "data": "groups" },
            { "data": "imagen" },
            { "data": "id" },
        ],
        columnDefs: [
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var html = '';
                    $.each(row.groups, function (key, value) {
                        html += '<span class="badge badge-secondary mr-1 mb-1">' + value.name + '</span>'
                    });
                    return html;
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="' + row.imagen + '" class="img-fluid mx-auto d-block" style="width: 40px; height: 40px;">';
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/user/detail/' + row.id + '/" class="btn btn-info btn-xs "><i class="fas fa-search"></i></a> ';
                    buttons += '<a href="/user/update/' + row.id + '/" class="btn btn-success btn-xs "><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/user/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs "><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});