import digimorph
import json, sys, urllib2
from pprint import pprint


def has_image(url):
    try:
        res = urllib2.urlopen(url)
    except(urllib2.HTTPError):
        return False
    return res.code == 200

def find_last(specimen_url, padding, start, step):
    max_slice = start
    print "Images found... "
    while has_image(digimorph.get_slice_url(specimen_url, max_slice, padding)):
        print str(max_slice) + ",",
        max_slice+=step
    print
    return max_slice - step


all_species = {}
for line in open('url_map.json'):
    all_species.update(json.loads(line))
pprint(all_species)

urls = []
for val in all_species.values():
    urls.extend(val['urls'])

pprint(urls)
slice_data = {}
for u in urls:
    specimen_url = digimorph.get_specimen_url(u)
    padding = 0
    max_slice = 0
    has_slices = True

    print "Finding images for %s" % specimen_url
    print digimorph.get_slice_url(specimen_url, 1, 3)
    # 3 or 4 padding?
    if has_image(digimorph.get_slice_url(specimen_url, 1, 3)):
        padding = 3
        print "Padding 3!"
    elif has_image(digimorph.get_slice_url(specimen_url, 1, 4)):
        padding = 4
        print "Padding 4!"
    else:
        print "Failed to find first image with 3 or 4 padding"
        has_slices = False

    if has_slices:
        # Find last slice image
        max_slice = find_last(specimen_url, padding, 100, 100)
        max_slice = find_last(specimen_url, padding, max_slice, 10)
        max_slice = find_last(specimen_url, padding, max_slice, 1)
        
        slice_data[u] = {
            'zero_padding': padding,
            'slice_count': max_slice,
        }

pprint(slice_data)
