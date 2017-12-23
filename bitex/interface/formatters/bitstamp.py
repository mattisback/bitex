from bitex.interface.formatters import APIResponse
from datetime import datetime


class BitstampAPIResponse(APIResponse):

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
        # {'bid': '18795.00', 'open': '18953.00', 'timestamp': '1513589738', 'ask': '18831.82',
        # 'volume': '13558.68696337', 'low': '17835.20', 'high': '19666.00', 'vwap': '18809.34', 'last': '18832.93'}

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
