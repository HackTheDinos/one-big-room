import math

BASE_URL = 'http://digimorph.org/'
PREVIEW_SLICES = 50

def get_specimen_url(specimen_name):
    return BASE_URL + 'specimens/%s' % specimen_name.replace(" ", "_")

def get_slice_url(specimen_url, slice, zero_padding):
    return specimen_url + ('/applet/slicessm/coronal/cor%0' + str(zero_padding) + 'd.jpg') % slice

def get_slice_urls(specimen_url, total_slices):
    delta = int(math.floor(total_slices / PREVIEW_SLICES))
    return [ get_slice_url(specimen_url, slice, 3)
        for slice in range(1, total_slices, delta) ]

def get_preview_url(specimen_url):
    return specimen_url + '/specimen.jpg'