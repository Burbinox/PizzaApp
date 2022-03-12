from bson import json_util
import json


def sanitize_mongodb_document(doc):
    """Sanitize mongodb document to allow correct return it."""
    return json.loads(json_util.dumps(doc))
