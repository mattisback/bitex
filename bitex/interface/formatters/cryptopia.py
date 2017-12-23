from bitex.interface.formatters import APIResponse
from datetime import datetime


class CryptopiaAPIResponse(APIResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        return {
            'timestamp': response.receive_time,
            'bid': float(response_data['Data']['BidPrice']),
            'ask': float(response_data['Data']['AskPrice']),
            'low': float(response_data['Data']['Low']),
            'high': float(response_data['Data']['High']),
            'volume': float(response_data['Data']['Volume']),
            'last': float(response_data['Data']['LastPrice'])
        }

        # {'Error': None, 'Message': None, 'Success': True,
        #  'Data': {'BaseVolume': 115.20140042, 'SellBaseVolume': 7895377.3822143, 'Label': 'ETH/BTC',
        #           'SellVolume': 610.85063355, 'Close': 0.03827886, 'Change': 4.87, 'LastPrice': 0.03827886,
        #           'AskPrice': 0.03827886, 'Volume': 3086.02843597, 'Low': 0.03526454, 'BuyVolume': 696183.93492498,
        #           'BidPrice': 0.03820002, 'High': 0.03899999, 'Open': 0.0365, 'TradePairId': 5203,
        #           'BuyBaseVolume': 11.94683624}}

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
