import logging
import os

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    application_version = os.getenv('APPLICATION_VERSION')
    environment = os.getenv('ENVIRONMENT')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        response_string = f'{environment} environment\n'
        return func.HttpResponse(f"{response_string}Hello, {name}. This HTTP triggered function executed successfully. v{application_version}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
