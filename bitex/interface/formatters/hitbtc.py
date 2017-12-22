from bitex.interface.formatters import FormattedResponse
from datetime import datetime


class HitBTCFormattedResponse(FormattedResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        return {
            'timestamp': datetime.fromtimestamp(float(response_data['timestamp'])),
            'bid': float(response_data['bid']),
            'ask': float(response_data['ask']),
            'low': float(response_data['low']),
            'high': float(response_data['high']),
            'volume': float(response_data['volume']),
            'last': float(response_data['last'])
        }
        # {'volume_quote': '83133956.8778', 'low': '17900.00', 'timestamp': 1513589950091, 'last': '18541.17',
        # 'ask': '18541.13', 'open': '19222.49', 'bid': '18520.03', 'volume': '4407.55', 'high': '19531.90'}

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
