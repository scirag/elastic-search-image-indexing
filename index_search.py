from flask import Flask, jsonify, request
from PIL import Image
import imagehash
from elasticsearch import Elasticsearch

ES_INDEX_NAME = 'cebir'
ES_DOC_TYPE = 'image_info'

es = Elasticsearch()
app = Flask(__name__)


@app.route("/api/pycebir/fileUpload", methods=['POST'])
def file_upload():
    file = request.files['file']
    img = Image.open(file.stream)
    phash = imagehash.phash(img)
    hash_string = str(phash)
    return jsonify({
        'result': 'OK',
        'hash': hash_string
    })


@app.route("/api/pycebir/search/<phash>/<min_score>", methods=['GET'])
def search_image(phash, min_score):
    search_results = es.search(index=ES_INDEX_NAME, doc_type=ES_DOC_TYPE, body={
        "query": {
            "function_score": {
                "min_score": min_score,
                "query": {
                    "match_all": {}
                },
                "functions": [
                    {
                        "script_score": {
                            "script": "hamming_distance",
                            "lang": "native",
                            "params": {
                                "hash": phash,
                                "field": "hash"
                            }
                        }
                    }
                ]
            }
        }
    })

    return jsonify(search_results)

if __name__ == '__main__':
    IP = "0.0.0.0"
    PORT = 1453
    app.run(host=IP, port=PORT, debug=True)