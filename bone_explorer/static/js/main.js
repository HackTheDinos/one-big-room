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