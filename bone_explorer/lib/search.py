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

# Verify that Python can talk to Bonsai (optional):
es.ping()

def do_search(q, group):
    if (es.ping()):
        query = {}

        match_q = {"match": {"name": q}}
        if (group):
            filter = {"term": {"is_skrillex": True}}
            query = {"query": {"filtered": {"filter": filter, "query": match_q}}}
        else:
            query = {"query": match_q}
        query["fields"] = {"fields":["name"]}

        res = es.search(index="test", doc_type="people", body=query)
        
        hits = res["hits"]["hits"]
        
        scan_data = [doc["fields"] for doc in hits]
        return {"query": q, "results": scan_data}
    return None
