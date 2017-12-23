from bitex.interface.formatters import APIResponse
from datetime import datetime


class BinanceAPIResponse(APIResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        return {
            'timestamp': response.receive_time,
            'bid': float(response_data['bidPrice']),
            'ask': float(response_data['askPrice']),
            'low': float(response_data['lowPrice']),
            'high': float(response_data['highPrice']),
            'volume': float(response_data['volume']),
            'last': float(response_data['lastPrice'])
        }
        # {'symbol': 'LTCBTC', 'priceChange': '0.00077900', 'priceChangePercent': '4.862',
        # 'weightedAvgPrice': '0.01654431', 'prevClosePrice': '0.01604100', 'lastPrice': '0.01680000',
        # 'lastQty': '3.16000000', 'bidPrice': '0.01680000', 'bidQty': '90.41000000', 'askPrice': '0.01680200',
        # 'askQty': '6.08000000', 'openPrice': '0.01602100', 'highPrice': '0.01720000', 'lowPrice': '0.01592900',
        # 'volume': '280075.72000000', 'quoteVolume': '4633.66016380', 'openTime': 1513517073466,
        # 'closeTime': 1513603473466, 'firstId': 2256032, 'lastId': 2318568, 'count': 62537}

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
