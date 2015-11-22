// Init slice previews
$('.slice-preview').each(function() {
    var $image = $(this),
        slice_urls = $image.data('slice-urls'),
        slice_count = slice_urls.length - 1;
    $image.mousemove(function(e) {
        slice = Math.floor(slice_count * (e.offsetX / this.width));
        this.src = slice_urls[slice];
    })
});

var result_template = $('#result-template').html();
Mustache.parse(result_template);
function render_results(result_list) {
    $('#results').html(Mustache.render(result_template, {
        results_list: result_list
    }));
}

var title = document.title;
$("#search").submit(function(e) {
    e.preventDefault();
    $.get("/api/search", $(this).serialize()).success(function(response) {
        render_results(response.results);
        document.title = response.query + " - " + title;
    });
});