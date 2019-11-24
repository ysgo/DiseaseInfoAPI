$('#login').on('click', function() {
    $.ajax({
        url: '/rest-auth/login/',
        type: 'POST',
        data: {
            'username': $('#loginUsername').val(),
            'password': $('#loginPassword').val()
        },
        dataType:'json',
        headers: { 'X-CSRFToken': csrftoken },
        success: function(response) {
            $("#getToken").val(response.token);
        }, error: function(request, status, error) {
            console.log("code = "+ request.status + " message = " + request.responseText + " error = " + error);
        }, complete: function() {
            location.replace('/main/');
        }
    });
})

$('#logout').on('click', function() {
    $.ajax({
        url: '/rest-auth/logout/',
        type: 'POST',
        headers: { 'X-CSRFToken': csrftoken },
        success: function(response) {
            location.replace('/main/');
            console.log(response);
        }, error: function(request, status, error) {
            console.log("code = "+ request.status + " message = " + request.responseText + " error = " + error);
        }
    });
})

$('#register').on('click', function() {
    $.ajax({
        url: '/rest-auth/registration/',
        type: 'POST',
        data: {
            'username': $('#registerUsername').val(),
            'password1': $('#registerPassword').val(),
            'password2': $('#repeatPassword').val()
        },
        dataType:'json',
        headers: { 'X-CSRFToken': csrftoken },
        success: function(response) {
            location.replace('/main/login');
            console.log(response);
        }, error: function(request, status, error) {
            console.log("code = "+ request.status + " message = " + request.responseText + " error = " + error);
        }
    });
})

