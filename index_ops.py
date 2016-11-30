from elasticsearch import Elasticsearch
from PIL import Image
import imagehash
import json
import uuid
import base64
from io import BytesIO

es = Elasticsearch()


def generate_guid():
    return str(uuid.uuid4())


def delete_index(index):
    es.indices.delete(index=index, ignore=[400, 404])


def create_index(index):
    es.indices.create(index=index, ignore=400)


def index_image(image, file_name, index, doc_type):
    hash = imagehash.phash(image)
    thumbnail_size = 128, 128
    image.thumbnail(thumbnail_size)
    output = BytesIO()
    image.save(output, format="JPEG", quality=66, optimize=True)
    img_base64 = base64.b64encode(output.getvalue())
    output.close()
    uid = generate_guid()
    json_data = json.dumps({
        'hash': str(hash),
        'fileName': file_name,
        'imgBase64': img_base64.decode()
    })
    es.index(index=index, doc_type=doc_type, id=uid, body=json_data)
