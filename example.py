from index_ops import *
from elasticsearch import Elasticsearch

es = Elasticsearch()

index_name = 'cebir'
document_type = 'image_info'

# delete_index('cebir')
create_index(index_name)

file_name = "data/lake.jpg"
img = Image.open(file_name)
index_image(img, file_name, index=index_name, doc_type=document_type)

hash_query = "4b6f6869d45369e0"

search_results = es.search(index=index_name, doc_type=document_type, body={"query": {"match": {"hash": hash_query}}})

print(search_results)