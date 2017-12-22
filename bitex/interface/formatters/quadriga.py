from bitex.interface.formatters import FormattedResponse
from datetime import datetime


class QuadrigaCXFormattedResponse(FormattedResponse):

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
        # {'timestamp': '1513590053', 'last': '18664.39', 'high': '19149.99', 'low': '18302.00',
        # 'vwap': '19398.35646730', 'ask': '19484.79', 'volume': '16.86610461', 'bid': '18664.50'}

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
