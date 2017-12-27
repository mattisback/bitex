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

    @check_and_format_pair
    def request_public_method_with_currency(self, pair, path, **endpoint_kwargs):
        endpoint_kwargs['primaryCurrencyCode'] = pair[0]
        endpoint_kwargs['secondaryCurrencyCode'] = pair[1]
        return self.request(path, params=endpoint_kwargs)

    @staticmethod
    def add_pair_to_kwargs(formatted_pair, endpoint_kwargs):
        endpoint_kwargs['primaryCurrencyCode'] = formatted_pair[0]
        endpoint_kwargs['secondaryCurrencyCode'] = formatted_pair[1]

    @format_response
    @check_and_format_pair
    def ticker(self, pair, *args, **endpoint_kwargs):
        # https://api.independentreserve.com/Public/GetMarketSummary?primaryCurrencyCode=xbt&secondaryCurrencyCode=usd
        self.add_pair_to_kwargs(pair, endpoint_kwargs)
        return self.request('Public/GetMarketSummary', params=endpoint_kwargs)

    @check_and_format_pair
    def order_book(self, pair, *args, **endpoint_kwargs):
        self.add_pair_to_kwargs(pair, endpoint_kwargs)
        return self.request('Public/GetOrderBook', params=endpoint_kwargs)

    @check_and_format_pair
    def trades(self, pair, *args, **endpoint_kwargs):
        self.add_pair_to_kwargs(pair, endpoint_kwargs)
        if 'numberOfRecentTradesToRetrieve' not in endpoint_kwargs:
            endpoint_kwargs['numberOfRecentTradesToRetrieve'] = 50  # max is 50
        return self.request('Public/GetRecentTrades', params=endpoint_kwargs)

    def ask(self, pair, price, size, *args, **endpoint_kwargs):
        pass

    def bid(self, pair, price, size, *args, **endpoint_kwargs):
        pass

    def order_status(self, order_id, *args, **endpoint_kwargs):
        pass

    def open_orders(self, *args, **endpoint_kwargs):
        # example response
        # {'Data': [{'OrderType': 'LimitOffer', 'Volume': 0.082, 'Value': 1845.0, 'OrderGuid': 'e3dd24aa-bf46-4902-ac9c-5ef260edcc0b', 'CreatedTimestampUtc': '2017-12-24T05:41:20.3731526Z', 'FeePercent': 0.005, 'PrimaryCurrencyCode': 'Xbt', 'AvgPrice': 22500.0, 'Outstanding': 0.082, 'Price': 22500.0, 'Status': 'Open', 'SecondaryCurrencyCode': 'Aud'}], 'PageSize': 50, 'TotalPages': 1, 'TotalItems': 1}
        # primaryCurrencyCode: The primary currency of orders. This is an optional parameter.
        # secondaryCurrencyCode: The secondary currency of orders. This is an optional parameter.
        # pageIndex: The page index. Must be greater or equal to 1
        # pageSize: Must be greater or equal to 1 and less than or equal to 50.
        #           If a number greater than 50 is specified, then 50 will be used.
        if 'pageIndex' not in endpoint_kwargs:
            endpoint_kwargs['pageIndex'] = 1
        if 'pageSize' not in endpoint_kwargs:
            endpoint_kwargs['pageSize'] = 50

        return self.request('Private/GetOpenOrders', authenticate=True, params=endpoint_kwargs)

    def cancel_order(self, *order_ids, **endpoint_kwargs):
        # orderGuid: The guid of currently open or partially filled order.
        endpoint_kwargs['orderGuid'] = order_ids[0]
        return self.request('Private/CancelOrder', authenticate=True, params=endpoint_kwargs)

    def wallet(self, *args, **endpoint_kwargs):
        # example response
        # [{'AvailableBalance': 0.0, 'CurrencyCode': 'Usd', 'AccountGuid': '900aab43-6995-4812-bb02-0b13d60b039b', 'TotalBalance': 0.0, 'AccountStatus': 'Active'}, {'AvailableBalance': 1595.61, 'CurrencyCode': 'Aud', 'AccountGuid': '900aab43-6995-4812-bb02-0b13d60b039b', 'TotalBalance': 1595.61, 'AccountStatus': 'Active'}, {'AvailableBalance': 0.0, 'CurrencyCode': 'Nzd', 'AccountGuid': '900aab43-6995-4812-bb02-0b13d60b039b', 'TotalBalance': 0.0, 'AccountStatus': 'Active'}, {'AvailableBalance': 0.418, 'CurrencyCode': 'Xbt', 'AccountGuid': '900aab43-6995-4812-bb02-0b13d60b039b', 'TotalBalance': 0.5, 'AccountStatus': 'Active'}, {'AvailableBalance': 0.0, 'CurrencyCode': 'Eth', 'AccountGuid': '900aab43-6995-4812-bb02-0b13d60b039b', 'TotalBalance': 0.0, 'AccountStatus': 'Active'}, {'AvailableBalance': 0.0, 'CurrencyCode': 'Bch', 'AccountGuid': '900aab43-6995-4812-bb02-0b13d60b039b', 'TotalBalance': 0.0, 'AccountStatus': 'Active'}]
        return self.request('Private/GetAccounts', authenticate=True, params=endpoint_kwargs)

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

