import os, base64, re, logging
from elasticsearch import Elasticsearch

# Log transport details (optional):
logging.basicConfig(level=logging.INFO)

# Parse the auth and host from env:
#bonsai = os.environ['BONSAI_URL']
bonsai = "https://uhxnwjp8:t3y4mdk8zo1ck366@pine-2787280.us-east-1.bonsai.io"
auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')

# Connect to cluster over SSL using auth for best security:
es_header = [{
    'host': host,
    'port': 443,
    'use_ssl': True,
    'http_auth': (auth[0],auth[1])
}]

# Instantiate the new Elasticsearch connection:
es = Elasticsearch(es_header)

index_name = "scans"

text_fields = ["species", "phylum", "family", "class", "genus", "scientific_name", "wikipedia_snippet",
        "wikipedia_misc", "gbif_snippet", "gbif_misc"]

def do_search(q, groups):
    if (es.ping()):
        query = {}

        matches = [{"match": {f: q}} for f in text_fields]
        match_q = {"dis_max": {"queries": matches}}

        if (len(groups) > 0):
            group_matches = [{"term": {"group": group}} for group in groups]
            filter = {"or": group_matches}

            query = {"query": {"filtered": {"filter": filter}}}
            if (q):
                query["query"]["filtered"]["query"] = match_q
        else:
            query = {"query": match_q}

        res = es.search(index=index_name, doc_type="scans_test", body=query)
        hits = res["hits"]["hits"] # why
        
        scan_data = []
        for doc in hits:
            data = doc["_source"]
            data["id"] = doc["_id"]
            scan_data.append(data)

        return scan_data
    return None

def get_scan_data(id):
    if (es.ping()):
        return es.get(index=index_name, doc_type="scans_test", id=id)["_source"]
    return None
