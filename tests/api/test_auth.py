import copy
from unittest import TestCase
import api_base
import global_variables

class APIAuth(api_base.APITestBase):
    uri = copy.copy(global_variables.DEFAULT_OBJECTS['auth']['uri'])
    base_payload = copy.copy(global_variables.DEFAULT_OBJECTS['auth']['payload'])

    def test_landing_page(self):
        super().landing_page()

    def test_invalid_uri(self):
        super().invalid_uri()

    def test_invalid_post(self):
        payload = {
            'username': '',
        }
        errors = {"missing": ["username", 'password']}
        super().invalid_post(payload, errors)

    def test_valid_post(self):
        super().valid_post(self.base_payload, self.base_payload)

    def test_invalid_put(self):
        payload = {
            'username': '',
            'password': 'pass'
        }
        errors = {"missing": ["username"]}
        super().invalid_put(payload, errors)

    def test_valid_put(self):
        payload = {
            'username': 'update',
            'password': 'pass'
        }
        super().valid_put(payload, payload)

    def test_invalid_patch(self):
        payload = {
            'usernamez': 'update',
            'password': 'pass'
        }
        errors = {"unknown": ["usernamez"]}
        super().invalid_patch(payload, errors)

    def test_valid_patch(self):
        payload = {
            'username': 'update',
        }
        result = copy.copy(self.base_payload)
        result.update(payload)
        resp = self.create_valid(self.base_payload)
        self.valid_patch(payload, result)
