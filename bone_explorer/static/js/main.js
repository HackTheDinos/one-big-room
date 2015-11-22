var result_template = "Something went wrong. Reload and try again.";
var title = document.title;

function init_slice_previews() {
    $('.slice-preview').each(function() {
        var $image = $(this),
            slice_urls = $image.data('slice-urls'),
            slice_count = slice_urls.length - 1;
        $image.mousemove(function(e) {
            slice = Math.floor(slice_count * (e.offsetX / this.width));
            if (slice_urls[slice]) {
                this.src = slice_urls[slice]
            }
        })
    });
}

// Ajax template loader
function templateLoader(name) {
    var result = '';
    $.ajax('/static/templates/' + name + '.mustache', {
        method: 'get',
        async: false,
        success: function (data) {
             result = data;
        }
    });
    return result;
}

function render(response) {
    $('#results').html(Mustache.render(result_template, {
        results_list: response.results
    }, templateLoader));

    init_slice_previews();
    document.title = response.query + " - " + title;
}

window.onpopstate = function(e) {
    render(e.state);
    $("#search").find('[name=query]').val(e.state.query);
}

$(function() {
    result_template = templateLoader('results');

    $("#search").submit(function(e) {
        e.preventDefault();
        var $form = $(this);
        if ($form.find('[name=query]').val() != '') {
            var query_params = $form.serialize();
            $.get("/api/search", query_params)
                .done(function(response) {
                    render(response);
                    history.pushState(response, "", "?" + query_params);
                })
                .fail(function(jqXHR, textStatus) {
                    alert(jqXHR.status + ": " + jqXHR.statusText);
                })
        }
    }).submit();
    init_slice_previews();
});