function message_error(obj) {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<p style="text-align:center;">';
        $.each(obj, function (key, value) {
            html += '<span>' + value + '</span>';
        });
        html += '</p>';
    } else {
        html = '<p>' + obj + '</p>';
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
};

