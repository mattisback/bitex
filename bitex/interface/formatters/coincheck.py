from bitex.interface.formatters import APIResponse
from datetime import datetime


class CoinCheckAPIResponse(APIResponse):

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
        # {"last":2171460.0,"bid":2171460.0,"ask":2171871.0,"high":2277722.0,
        # "low":2000000.0,"volume":42302.59403478,"timestamp":1513592823}

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
