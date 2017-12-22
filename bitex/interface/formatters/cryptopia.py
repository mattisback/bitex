from bitex.interface.formatters import FormattedResponse
from datetime import datetime


class CryptopiaFormattedResponse(FormattedResponse):

    def _format_ticker(self, response):
        response_data = response.json()
        return {
            'timestamp': datetime.fromtimestamp(float(response_data['TimeStamp'])),
            'bid': float(response_data['result']['Bid']),
            'ask': float(response_data['result']['Ask']),
            'low': float(response_data['result']['Low']),
            'high': float(response_data['result']['High']),
            'volume': float(response_data['result']['BaseVolume']),
            'last': float(response_data['result']['Last'])
        }
        # {'success': True, 'result': [{'Ask': 0.01664998, 'BaseVolume': 2772.17956679, 'MarketName': 'BTC-LTC',
        #                               'OpenSellOrders': 9647, 'Low': 0.01589002, 'Created': '2014-02-13T00:00:00',
        #                               'OpenBuyOrders': 7846, 'Bid': 0.01663114, 'PrevDay': 0.01613444,
        #                               'High': 0.0171071, 'Volume': 168102.39042146,
        #                               'TimeStamp': '2017-12-18T09:42:47.75',
        #                               'Last': 0.01663114}], 'message': ''}

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
