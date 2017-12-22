from bitex.interface.formatters import FormattedResponse
from datetime import datetime


class OkCoinFormattedResponse(FormattedResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        return {
            'timestamp': datetime.fromtimestamp(float(response_data['date'])),
            'bid': float(response_data['ticker']['buy']),
            'ask': float(response_data['ticker']['sell']),
            'low': float(response_data['ticker']['low']),
            'high': float(response_data['ticker']['high']),
            'volume': float(response_data['ticker']['vol']),
            'last': float(response_data['ticker']['last'])
        }
        #  {'date': '1513589963', 'ticker': {'vol': '242.63', 'sell': '19304.32', 'low': '18463.31', 'buy': '19250.00',
        #                                    'last': '19305.32', 'high': '20312.39'}}

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
