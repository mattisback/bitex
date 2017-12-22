from bitex.interface.formatters import FormattedResponse
from datetime import datetime


class KrakenFormattedResponse(FormattedResponse):

    def _format_ticker(self, response):
        """
        from: https://www.kraken.com/en-gb/help/api#get-ticker-info
        Result: array of pair names and their ticker info

        <pair_name> = pair name
            a = ask array(<price>, <whole lot volume>, <lot volume>),
            b = bid array(<price>, <whole lot volume>, <lot volume>),
            c = last trade closed array(<price>, <lot volume>),
            v = volume array(<today>, <last 24 hours>),
            p = volume weighted average price array(<today>, <last 24 hours>),
            t = number of trades array(<today>, <last 24 hours>),
            l = low array(<today>, <last 24 hours>),
            h = high array(<today>, <last 24 hours>),
            o = today's opening price
        Note: Today's prices start at 00:00:00 UTC
        """
        response_data = response.json()
        d = response_data['result'][next(iter(response_data['result']))]
        return {
            'timestamp': response.receive_time,
            'bid': float(d['b'][0]),
            'ask': float(d['a'][0]),
            'low': float(d['l'][0]),  # today so far
            'high': float(d['h'][0]),  # today so far
            'volume': float(d['v'][0]),  # today so far
            'last': float(d['c'][0])
        }
        # {'result': {'XXBTZUSD': {'l': ['18298.50000', '18298.50000'], 't': [10565, 25136],
        # 'h': ['19248.80000', '19660.00000'], 'p': ['18621.15863', '18915.79287'],
        # 'c': ['18730.00000', '0.03250000'], 'a': ['18736.20000', '1', '1.000'], 'b': ['18734.00000', '1', '1.000'],
        # 'o': '18920.60000', 'v': ['1625.24396735', '3765.20743005']}}, 'error': []}

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
