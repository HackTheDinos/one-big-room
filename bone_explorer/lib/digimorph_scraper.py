import digimorph
import json, sys, urllib2, re
from pprint import pprint
from bs4 import BeautifulSoup

with open(sys.argv[1]) as data_file:    
    data = json.load(data_file)

def get_page(url):
    print "getting " + url
    response = urllib2.urlopen(url)
    return response.read()

species = filter(None, [ d.get('species', None) for d in data ])
species = [species[0]]

species_data = []

date_re = re.compile('Publication Date:([^<]*)', re.DOTALL)

for s in species:
    data = {}

    try:
        html = get_page(digimorph.get_specimen_url(s))
        soup = BeautifulSoup(html, 'html.parser')
        
        # Author and institution
        author_link = soup.select('.author a')[0]
        institution = soup.select('.institution')[0]
        data['author_url'] = author_link.get('href').strip()
        data['author_name'] = author_link.get_text().strip()
        data['author_name'] = author_link.get_text().strip()
        data['institution'] = institution.get_text().strip()

        # Image data
        image_processing = soup.body.find_all(string=re.compile('Image processing'))
        image_processing_links = image_processing[0].parent.find_all('a')
        date_string = image_processing[0].parent.contents[-1].get_text();

        data['image_processing_date'] = date_re.search(date_string).group(1).strip()

        data['image_processing_links'] = [ {
            'name': a.get_text(),
            'url': a.get('href')
        } for a in image_processing_links ]

        # Available Images

        available_images_table = soup.body.find_all(string='Java Slice Viewer')[0].parent.parent.parent
        available_images = []
        last_header = ''
        for tr in available_images_table.find_all('tr')[1:]:
            td = tr.find_all('td')[0];
            if td.get('class') and 'menuheading' in td.get('class'):
                last_header = td.get_text().strip()
            elif len(td.find_all('a')) > 0:
                available_images.append(last_header + " - " + td.find_all('a')[0].get_text().strip())
        data['available_images'] = available_images

        species_data.append(data)
    except(urllib2.HTTPError):
        print "Error"
        pass

print json.dumps(species_data)