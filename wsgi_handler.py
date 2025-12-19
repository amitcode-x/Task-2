from serverless_wsgi import handle_request
from ats_service.wsgi import application

def handler(event, context):
    return handle_request(application, event, context)
