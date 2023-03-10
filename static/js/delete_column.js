$(document).ready(function() {
    $("label[for$='DELETE']").hide();
    $('[id$="DELETE"]').css('display', 'none');
    $(document).on('click', '.delete_button', function(event) {
        event.preventDefault();
        $(this).closest(".formset-container").css('display', 'none');
        $(this).closest('.formset-container').find('[id$="-DELETE"]').prop('checked', true);
    });
});
