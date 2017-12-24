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
import base64

# Import Third-Party

# Import Homebrew
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
        req_kwargs = super(IndependentReserveREST, self).sign_request_kwargs(endpoint,
                                                                             **kwargs)

        # Parameters go into headers, so pop params key and generate signature
        params = req_kwargs.pop('params')

        params['request'] = self.generate_uri(endpoint)
        params['nonce'] = self.nonce()

        # convert to json, encode and hash
        payload = ','.join(params)  # json.dumps(params)
        data = base64.standard_b64encode(payload.encode('utf8'))

        hmac_sig = hmac.new(self.secret.encode('utf8'), data, hashlib.sha256)
        signature = hmac_sig.hexdigest().upper()

        # Update headers and return
        req_kwargs['headers'] = {"X-BFX-APIKEY": self.key,
                                 "X-BFX-SIGNATURE": signature,
                                 "X-BFX-PAYLOAD": data,
                                 "Content-Type": "application/json",
                                 "Accept": "application/json"}

        return req_kwargs
