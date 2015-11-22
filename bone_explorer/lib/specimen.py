import digimorph
import json 
import math

def get_common_data(result):
  specimen_url = digimorph.get_specimen_url(result['specimen_url'])
  
  slice_data = None
  if result.get('slice_count', 0) > 0:
    slice_urls = digimorph.get_slice_urls(specimen_url,
                          result.get('slice_count', 100),
                          result.get('zero_padding', 1))
    slice_data = {
      'has_slices': 'slice_count' in result,
      'slice_urls': json.dumps(slice_urls),
      'first_slice': slice_urls[int(math.floor(len(slice_urls)/2))]
    }

  return {
    'title': result.get('scientific_name') if result.get('scientific_name') else result.get('species'), 
    'digimorph_url': specimen_url,
    'imageUrl': digimorph.get_preview_url(specimen_url),
    'slice_data': slice_data,
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