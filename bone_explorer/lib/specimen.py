import digimorph
import json 
import math

def get_common_data(result):
  specimen_url = digimorph.get_specimen_url(result['scientific_name'])
  slice_urls = digimorph.get_slice_urls(specimen_url, 476)
  
  return {
    'digimorph_url': specimen_url,
    'imageUrl': digimorph.get_preview_url(specimen_url),
    'slice_data': {
          'slice_urls': json.dumps(slice_urls),
          'first_slice': slice_urls[int(math.floor(len(slice_urls)/2))]
    },
    'classification': [
        result.get('phylum', None),
        result.get('class', None),
        result.get('order', None),
        result.get('family', None),
        result.get('genus', None)
      ]
  }

def get_detail_view_data(result):
    data = get_common_data(result)
    data.update(result)
    return data

def get_result_view_data(result):
  data = get_common_data(result)
  data.update(result)
  data['url'] = "specimen/" + result['id'];
  return data