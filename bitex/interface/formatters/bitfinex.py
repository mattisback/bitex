from bitex.interface.formatters import FormattedResponse
from datetime import datetime


class BitfinexFormattedResponse(FormattedResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        return {
            'timestamp': datetime.fromtimestamp(float(response_data['timestamp'])),
            'bid': float(response_data['bid']),
            'ask': float(response_data['ask']),
            'low': float(response_data['low']),
            'high': float(response_data['high']),
            'volume': float(response_data['volume']),
            'last': float(response_data['last_price'])
        }
        # {'bid': '18629.0', 'timestamp': '1513589744.5260189', 'ask': '18630.0', 'mid': '18629.5', 'low': '18010.0',
        #  'volume': '63690.87027664', 'last_price': '18630.0', 'high': '19891.0'}

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
