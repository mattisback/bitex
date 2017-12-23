# Import Built-Ins
import logging
import unittest
from unittest import mock

# Import Third-Party
import requests

# Import Homebrew
try:
    from bitex.interface.formatters import APIResponse
except ImportError:
    raise AssertionError("'APIResponse' not implemented!")

# Init Logging Facilities
log = logging.getLogger(__name__)


def buld_mock_response():
    """Build a mock response object with all necessary parameters mocked"""
    response = mock.MagicMock(spec=requests.Response)
    response.content = bytes()
    response.status_code = 200
    response.cookies = []
    response.elapsed = 0
    response.encoding = 'utf8'
    response.headers = {'link': ''}
    response.history = []
    response.next = None
    response.raw = None
    response.reason = None
    response.request = None
    response.url = ''
    response._content_consumed = ''
    response._content = bytes()
    return response


class APIResponseTests(unittest.TestCase):

    def test_class_instance_handles_like_requestsResponse_instance(self):
        response = buld_mock_response()
        api_response = APIResponse('', {}, response)

        # Assert all expected attributes are present on the proxy object
        expected_attributes = ['apparent_encoding', 'content', 'cookies', 'elapsed', 'encoding',
                               'headers', 'history', 'is_permanent_redirect', 'is_redirect',
                               'links', 'next', 'ok', 'raw', 'reason', 'request',  'status_code',
                               'text', 'url', 'response', 'json']
        for attr in expected_attributes:
            self.assertTrue(hasattr(api_response, attr),
                            msg="%s has no attribute '%s'" % (api_response, attr))

        # Assert that we can access the original Response object via the APIResponse.response
        # attribute.
        self.assertEqual(api_response.response, response)

        # Assert that all callable methods of requests.Response are also callable in APIResponse
        try:
            api_response.iter_content()
        except TypeError as e:
            if e.args[0].endswith('object is not callable'):
                self.fail("Method 'iter_content' not implemented!")
            else:
                raise

        try:
            api_response.iter_lines()
        except TypeError as e:
            if e.args[0].endswith('object is not callable'):
                self.fail("Method 'iter_lines' not implemented!")
            else:
                raise

    def test_formatter_methods_raise_NotImplementedError_for_base_class(self):
        response = mock.MagicMock(spec=requests.Response)
        api_response = APIResponse('', {}, response)
        with self.assertRaises(NotImplementedError):
            api_response._format_ticker(None)

        with self.assertRaises(NotImplementedError):
            api_response._format_order_book(None)

        with self.assertRaises(NotImplementedError):
            api_response._format_trades(None)

        with self.assertRaises(NotImplementedError):
            api_response._format_bid(None)

        with self.assertRaises(NotImplementedError):
            api_response._format_ask(None)

        with self.assertRaises(NotImplementedError):
            api_response._format_order_status(None)

        with self.assertRaises(NotImplementedError):
            api_response._format_open_orders(None)

        with self.assertRaises(NotImplementedError):
            api_response._format_cancel_order(None)

        with self.assertRaises(NotImplementedError):
            api_response._format_wallet(None)


if __name__ == '__main__':
    unittest.main()
