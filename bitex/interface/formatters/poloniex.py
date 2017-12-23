from bitex.interface.formatters import APIResponse
from datetime import datetime


class PoloniexAPIResponse(APIResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        d = response_data[self.called_method_params[0]]
        return {
            'timestamp': response.receive_time,
            'bid': float(d['highestBid']),
            'ask': float(d['lowestAsk']),
            'low': float(d['low24hr']),
            'high': float(d['high24hr']),
            'volume': float(d['baseVolume']),
            'last': float(d['last'])
        }
        # {'BTC_CLAM': {'id': 20, 'highestBid': '0.00058379', 'percentChange': '0.32601675', 'low24hr': '0.00042656',
        #               'baseVolume': '77.25725539', 'high24hr': '0.00058657', 'quoteVolume': '152023.08084615',
        #               'lowestAsk': '0.00058719', 'isFrozen': '0', 'last': '0.00058720'}, '
        #  BTC_XPM': {'id': 116, 'highestBid': '0.00002168', 'percentChange': '0.02300469', 'low24hr': '0.00002107',
        #             'baseVolume': '8.41716666', 'high24hr': '0.00002299', 'quoteVolume': '383520.44957097',
        #             'lowestAsk': '0.00002178', 'isFrozen': '0', 'last': '0.00002179'},
        #  ... (for each coin!)
        # }

    def _format_order_book(self, response):
        pass
    
    def _format_trades(self, response):
        pass

    def _format_ask(self, response):
        pass

    def _format_bid(self, response):
        pass

    def _format_order_status(self, response):
        pass

    def _format_open_orders(self, response):
        pass

    def _format_cancel_order(self, response):
        pass

    def _format_wallet(self, response):
        pass
