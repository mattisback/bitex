"""IndependentReserve Interface class."""
# Import Built-Ins
import logging

# Import Third-Party
import requests

# Import Homebrew
from bitex.api.REST.independentreserve import IndependentReserveREST
from bitex.interface.rest import RESTInterface
from bitex.interface.formatters import IndependentReserveAPIResponse
from bitex.utils import check_version_compatibility, check_and_format_pair, format_response

# Init Logging Facilities
log = logging.getLogger(__name__)


class IndependentReserve(RESTInterface):
    """IndependentReserve Interface class.

    Includes standardized methods, as well as all other Endpoints
    available on their REST API.
    """

    # pylint: disable=arguments-differ

    def __init__(self, **api_kwargs):
        """Initialize class instance."""
        super(IndependentReserve, self).__init__('IndependentReserve', IndependentReserveREST(**api_kwargs))

    def request(self, endpoint, authenticate=False, **req_kwargs):
        """Preprocess request to API."""
        if not authenticate:
            return super(IndependentReserve, self).request('GET', endpoint, authenticate=authenticate,
                                                           **req_kwargs)
        return super(IndependentReserve, self).request('POST', endpoint, authenticate=authenticate,
                                                       **req_kwargs)

    def _get_supported_pairs(self):
        """Return supported pairs."""
        primary = self.get_valid_primary_currency_codes().json()
        secondary = self.get_valid_secondary_currency_codes().json()
        return [(x, y) for x in primary for y in secondary]

    # Public Exchange Endpoints
    def get_valid_primary_currency_codes(self):
        return self.request('Public/GetValidPrimaryCurrencyCodes')

    def get_valid_secondary_currency_codes(self):
        return self.request('Public/GetValidSecondaryCurrencyCodes')

    @format_response
    @check_and_format_pair
    def ticker(self, pair, *args, **endpoint_kwargs):
        # https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd
        endpoint_kwargs['primaryCurrencyCode'] = pair[0]
        endpoint_kwargs['secondaryCurrencyCode'] = pair[1]
        return self.request('Public/GetMarketSummary', params=endpoint_kwargs)

    def order_book(self, pair, *args, **kwargs):
        pass

    def trades(self, pair, *args, **kwargs):
        pass

    def ask(self, pair, price, size, *args, **kwargs):
        pass

    def bid(self, pair, price, size, *args, **kwargs):
        pass

    def order_status(self, order_id, *args, **kwargs):
        pass

    def open_orders(self, *args, **kwargs):
        pass

    def cancel_order(self, *order_ids, **kwargs):
        pass

    def wallet(self, *args, **kwargs):
        pass

    ###############
    # Basic Methods
    ###############
    # @format_response
    # @check_and_format_pair
    # def ticker(self, pair, **endpoint_kwargs):
    #     """Return the ticker for a given pair."""
    #     self.is_supported(pair)
    #     if self.REST.version == 'v1':
    #         return self.request('pubticker/%s' % pair)
    #     return self.request('ticker/%s' % pair, params=endpoint_kwargs)

