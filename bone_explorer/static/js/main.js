var result_template = "Something went wrong. Reload and try again.";
var title = document.title;

function init_slice_previews() {
    $('.slice-preview').each(function() {
        var $preview = $(this),
            $marker = $preview.find('.slice-marker'),
            $image = $preview.find('.slice-image'),
            slice_urls = $image.data('slice-urls'),
            slice_count = slice_urls.length - 1;
        $image.mousemove(function(e) {
            $marker.css('left', Math.min(e.offsetX, this.width - $marker.width()))
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
    $("#search").find('[name=query]').val(response.query);
    document.title = response.query + " - " + title;
}

function search(query_params) {
    $.get("/api/search", query_params)
        .done(function(response) {
            render(response);
            history.pushState(query_params, "", "?" + query_params);
        })
        .fail(function(jqXHR, textStatus) {
            alert(jqXHR.status + ": " + jqXHR.statusText);
        })
}

window.onpopstate = function(e) {
    if (e.state) {
        search(e.state);
    }
}

$(function() {
    result_template = templateLoader('search_results');
    $("#search").submit(function(e) {
        e.preventDefault();
        var $form = $(this);
        if ($form.find('[name=query]').val()
            || $form.find('[name=group]').val()) {
            search($form.serialize())
        }
    }).submit();
    init_slice_previews();
});