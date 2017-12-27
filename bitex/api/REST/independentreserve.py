"""Bitfinex REST API backend.

Documentation available at:
    https://www.independentreserve.com/API
"""
# pylint: disable=too-many-arguments
# Import Built-ins
import logging
import json
import hashlib
import hmac

# Import Third-Party

# Import Homebrew
from collections import OrderedDict

from bitex.api.REST import RESTAPI

log = logging.getLogger(__name__)


class IndependentReserveREST(RESTAPI):
    """IndependentReserve REST API class."""

    def __init__(self, addr=None, key=None, secret=None,
                 version=None, config=None, timeout=None):
        """Initialize the class instance."""
        addr = 'https://api.independentreserve.com' if not addr else addr
        version = None if not version else version
        super(IndependentReserveREST, self).__init__(addr=addr, version=version, key=key,
                                                     secret=secret, timeout=timeout,
                                                     config=config)

    def sign_request_kwargs(self, endpoint, **kwargs):
        """Sign the request."""
        req_kwargs = super(IndependentReserveREST, self).sign_request_kwargs(endpoint)

        url = self.generate_url(self.generate_uri(endpoint))
        nonce = self.nonce()

        kwparams = kwargs.pop('params')

        parameters = [
            url,
            'apiKey=' + self.key,
            'nonce=' + str(nonce),
        ]

        for k in kwparams:
            parameters.append(str(k) + '=' + str(kwparams[k]))

        message = ','.join(parameters)

        signature = hmac.new(
            self.secret.encode('utf-8'),
            msg=message.encode('utf-8'),
            digestmod=hashlib.sha256).hexdigest().upper()

        # make sure this collection ordered in the same way as parameters
        data_array = [
            ("apiKey", self.key),
            ("nonce", nonce),
            ("signature", str(signature))]
        for k in kwparams:
            data_array.append((k, kwparams[k]))

        data = OrderedDict(data_array)

        req_kwargs['headers'] = {'Content-Type': 'application/json'}
        req_kwargs['data'] = json.dumps(data, sort_keys=False)

        return req_kwargs
