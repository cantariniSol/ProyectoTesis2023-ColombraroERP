$(function () {
    $('select[name="groups"]').select2({
        theme: "bootstrap4",
        language: 'es',
        placeholder: "Seleccionar Rol",
        allowClear: true
    });
});