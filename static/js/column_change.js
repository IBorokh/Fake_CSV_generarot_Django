$(document).ready(function() {
  $('[id*=data_type]').each(function() {
    var selectedValue = $(this).val();
    if (selectedValue !== 'integer' && selectedValue !== 'text') {
      $(this).closest('.formset-container').find("label[for$='-extra_data1']").hide();
      $(this).closest('.formset-container').find("label[for$='-extra_data2']").hide();
      $(this).closest('.formset-container').find('[id$="-extra_data1"]').hide();
      $(this).closest('.formset-container').find('[id$="-extra_data2"]').hide();
    }
  });
  $(document).on('change', '[id$="-data_type"]', function() {
    if (this.value === 'integer' || this.value === 'text') {
      $(this).closest('.formset-container').find("label[for$='-extra_data1']").show();
      $(this).closest('.formset-container').find("label[for$='-extra_data2']").show();
      $(this).closest('.formset-container').find('[id$="-extra_data1"]').show();
      $(this).closest('.formset-container').find('[id$="-extra_data2"]').show();
    } else {
      $(this).closest('.formset-container').find("label[for$='-extra_data1']").hide();
      $(this).closest('.formset-container').find("label[for$='-extra_data2']").hide();
      $(this).closest('.formset-container').find('[id$="-extra_data1"]').hide();
      $(this).closest('.formset-container').find('[id$="-extra_data2"]').hide();
    }
  });
});
