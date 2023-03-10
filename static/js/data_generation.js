$(document).ready(function() {
    $('#generation_button').click(function(event) {
        event.preventDefault()
        var url = window.location.href;
        var pk = url.substring(url.lastIndexOf('/') + 1);
        var form_data = $('#number_form').serialize();
        $('#id_rows').val('');
        var table = $('.generated_data');
        var currentDate = new Date();
        var options = {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
          };
        var raw_num = table.find('tr').length
        var download_num = 'download' + raw_num
        var newRow = "<tr>\n" +
            "            <td>" + raw_num + "</td>\n" +
            "            <td>" + currentDate.toLocaleDateString('en-US', options) + "</td>\n" +
            "            <td><span class='processing_spinner processing''>Processing..</span></td>\n" +
            "            <td><a href=\"\" id='" + download_num + "' >Download</a></td>\n" +
            "        </tr>"
        table.append(newRow);

        // Відправити AJAX-запит на сервер
        $.ajax({
          type: 'POST',
          url: url,
          headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
          data: {
              pk: pk,
              rows_number: form_data
          },
          dataType: 'json',
          success: function(data) {
            var newRow = '<span class="processing_spinner ready" id="new">Ready</span>'
            $('.processing_spinner').replaceWith(newRow);
            $('#' + download_num).attr("href", "/generate_csv/download/" + data.pk +"")
          },
          error: function(jqXHR, textStatus, errorThrown) {
            // handle error response
            console.log("AJAX request failed: " + textStatus + ", " + errorThrown);
            if (jqXHR.status === 0) {
              alert("Not connect.\n Verify Network.");
            } else if (jqXHR.status == 404) {
              alert("Requested page not found. [404]");
            } else if (jqXHR.status == 500) {
              alert("Internal Server Error [500].");
            } else if (textStatus === "parsererror") {
              alert("Error parsing JSON or XML response.");
              console.log("Error parsing JSON response: " + textStatus + ", " + errorThrown);
            } else if (textStatus === "timeout") {
              alert("Timeout error.");
            } else if (textStatus === "abort") {
              alert("Ajax request aborted.");
            } else {
              alert("Uncaught Error.\n" + jqXHR.responseText);
            } }
        });
      });
    });
