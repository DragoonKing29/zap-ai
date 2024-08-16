import logging
import json

logging.basicConfig(level=logging.INFO)

def log_request(request):
    logging.info(f"Request received: {json.dumps(request)}")

def format_response(data):
    return {"status": "success", "data": data}
