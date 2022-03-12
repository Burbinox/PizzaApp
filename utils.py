from bson import json_util
import json


def sanitize_mongodb_document(doc):
    return json.loads(json_util.dumps(doc))
