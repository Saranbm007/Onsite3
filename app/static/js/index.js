$(function() {
    $.ajax({
        url: '{{ url_for("searchList") }}'
        }).done(function (data){
            $('#searchlist').autocomplete({
                source: data,
                minLength: 2
            });
        });
    });