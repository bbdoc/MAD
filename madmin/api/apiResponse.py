import flask
import json
from . import apiException, global_variables

class APIResponse(object):
    def __init__(self, logger, request, **kwargs):
        self.logger = logger
        self.request = request
        self.headers = self.request.headers
        self.mimetype = self.request.accept

    def __call__(self, content, status_code, **kwargs):
        headers = kwargs.get('', self.headers)
        converted_data = self.convert_to_format(content)
        resp = flask.Response(converted_data, mimetype=self.mimetype)
        resp.status_code = status_code
        for key, val in kwargs.items():
            if key == 'headers':
                for header_key, header_val in val.items():
                    resp.headers.add(header_key, header_val)
            else:
                setattr(resp, key, val)
        self.logger.debug4('Return Data: {}', converted_data)
        self.logger.debug4('Return Headers: {}', resp.headers)
        return resp

    def convert_to_format(self, content):
        beautify = self.headers.get('X-Beautify')
        if self.mimetype == 'application/json':
            try: 
                if beautify and beautify.isdigit() and int(beautify) == 1:
                    return json.dumps(content, indent=4)
                else:
                    return json.dumps(content)
            except Exception as err:
                raise apiException.FormattingError(500, err)