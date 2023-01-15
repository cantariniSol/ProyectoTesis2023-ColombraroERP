function message_error(obj) {
    var html = ''
    if (typeof (obj) === 'object') {
        html = '<p style="text-aling: left;">';
        $.each(obj, (key, value) => {
            html += '<span>' + key + ': ' + value + '</span>';
        });
        html += '</p>';
    } else {
        html = '<p>' + obj + '</p>'
    }
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    })
}