    $('#reqGenerate').on('click', function() {
        $.ajax({
          url: "/api/token/",
          type: "POST",
          data: {
            username: $("#username").val(),
            password: $("#password").val()
          },
          dataType: "json",
          headers: { "X-CSRFToken": csrftoken, 'csrftoken': csrftoken },
          success: function(response) {
            console.log("Success Response : " + response.token);
            $("#getToken").val(response.token);
          }, error: function(request, status, error) {
            console.log("code = " + request.status + " message = " + request.responseText + " error = " + error);
          }
        });
    })

    $('#reqVerify').on('click', function() {
        $.ajax({
            url: "/api/token/verify/",
            type: 'POST',
            data: {'token': $('#getToken').val() },
            dataType:'json',
            headers: { "X-CSRFToken": csrftoken, 'csrftoken': csrftoken },
            success: function(response) {
                $('#resVerify').val('The token is authenticated');
                console.log('success')
            }, error: function(request, status, error) {
                $('#resVerify').val('The token is not authenticated');
                console.log("code = "+ request.status + " message = " + request.responseText + " error = " + error);
            }
        });
    })

    $('#reqRefresh').on('click', function() {
        $.ajax({
            url: "/api/token/refresh/",
            type: 'POST',
            data: {'token': $('#getToken').val() },
            dataType:'json',
            headers: { "X-CSRFToken": csrftoken, 'csrftoken': csrftoken },
            success: function(response) {
                console.log('success')
                console.log('Success Response : ' + response)
                $('#getToken').val(response.token);
                $('#getRetoken').val(response.token);
            }, error: function(request, status, error) {
                console.log("code = "+ request.status + " message = " + request.responseText + " error = " + error);
            }
        });
    })

    $('#reqData').on('click', function() {
        $.ajax({
            url: "/api/data/",
            type: 'GET',
            dataType:'json',
            headers: {
                'Authorization': 'jwt ' + $('#getToken').val(),
            },
            success: function(response) {
                $('#resData').val('Data Response Success');
                let data = null;
                $.each(response, function() {
                    data = this.fields;
                    $('#dataTable').append('<tr>');
                    $('#dataTable').append('<td>' + this.pk + '</td>');
                    $('#dataTable').append('<td>' + data.name + '</td>');
                    $('#dataTable').append('<td>' + data.symptom + '</td>');
                    $('#dataTable').append('<td>' + data.diagnosis + '</td>');
                    $('#dataTable').append('</tr>');
                });
                $('#collapseCardExample').collapse();
            }, error: function(request, status, error) {
                $('#resData').val('Data Response Failed');
                console.log("code = "+ request.status + " message = " + request.responseText + " error = " + error);
            }
        });
    })