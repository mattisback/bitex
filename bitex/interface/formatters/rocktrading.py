from bitex.interface.formatters import FormattedResponse
from datetime import datetime


class TheRockTradingFormattedResponse(FormattedResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        d = response_data['date']
        if ":" == d[-3:-2]:
            d = d[:-3] + d[-2:]
        return {
            'timestamp': datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f%z'),
            'bid': float(response_data['bid']),
            'ask': float(response_data['ask']),
            'low': float(response_data['low']),
            'high': float(response_data['high']),
            'volume': float(response_data['volume_traded']),
            'last': float(response_data['last'])
        }
        # {'last': 19100.0, 'volume': 8665.12, 'open': 19000.0, 'close': 19999.99, 'volume_traded': 0.459,
        # 'date': '2017-12-18T10:40:54.866+01:00', 'fund_id': 'BTCUSD', 'high': 19999.99, 'bid': 18900.01,
        # 'low': 19000.0, 'ask': 19899.0}

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
