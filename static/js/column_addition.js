$(document).ready(function() {
    var addBtn = $('#add_form');

    addBtn.click(function() {
        var form_idx = $("#id_form-TOTAL_FORMS").val();
        var $container = $('<div>', {'class': 'formset-container'});
        $newform = $("#empty_form").clone(true,true)
        $container.append($newform.html().replace(/__prefix__/g, form_idx)).append('<button class="delete_button">Delete</button>');
        $container.find("label[for$='-extra_data1']").hide();
        $container.find("label[for$='-extra_data2']").hide();
        $container.find('[id$="-extra_data1"]').hide();
        $container.find('[id$="-extra_data2"]').hide();
        $("#incredible_form").append($container);
        $("#id_form-TOTAL_FORMS").val(parseInt(form_idx)+1);
        });

    $("#incredible_form").submit(function() {
        var totalForms = $("#incredible_form").find('.formset-container').length;
        $("#incredible_form").find('#id_form-TOTAL_FORMS').val(totalForms);
  });

});
