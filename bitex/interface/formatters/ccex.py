from bitex.interface.formatters import APIResponse
from datetime import datetime


class CCEXAPIResponse(APIResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        return {
            'timestamp': datetime.fromtimestamp(float(response_data['ticker']['updated'])),
            'bid': float(response_data['ticker']['buy']),
            'ask': float(response_data['ticker']['sell']),
            'low': float(response_data['ticker']['low']),
            'high': float(response_data['ticker']['high']),
            'volume': float('nan'),
            'last': float(response_data['ticker']['lastprice'])
        }
        # {'ticker': {'updated': 1513591935, 'lastbuy': 0.03794999, 'buy': 0.03794999, 'sell': 0.03798,
        #             'buysupport': 7.03034809, 'lastprice': 0.03794999, 'high': 0.03879995, 'low': 0.03600001,
        #             'avg': 0.03739998, 'lastsell': 0.03794999}}

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
