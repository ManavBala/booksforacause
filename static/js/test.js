$(document).ready(function(){
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $("#deleteButton").on('click', function(){
        var id = $(this).data("id")

        $.ajax({
            url: "/order_cancel/" + id,
            data: {
            csrfmiddlewaretoken: csrftoken,
                id: id
            },
            type: "post",
            dataType:"json",
            success: function() {
                location.reload()
            }

        });


    })

})