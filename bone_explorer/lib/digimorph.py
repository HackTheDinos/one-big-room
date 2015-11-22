import math

BASE_URL = 'http://digimorph.org/'
PREVIEW_SLICES = 50

def get_slice_url(specimen_url, slice):
    return specimen_url + '/applet/slicessm/coronal/cor%04d.jpg' % slice

def get_slice_urls(specimen_url, total_slices):
    delta = int(math.floor(total_slices / PREVIEW_SLICES))
    return [ get_slice_url(specimen_url, slice)
        for slice in range(1, total_slices, delta) ]

def get_preview_url(specimen_url):
    return specimen_url + '/specimen.jpg'