from bitex.interface.formatters import APIResponse
from datetime import datetime


class IndependentReserveAPIResponse(APIResponse):
    def _format_ticker(self, response):
        response_data = response.json()
        return {
            # timestamp has 'Z' at then end to signify it's utc.  Remove the 'Z' before parsing.  Also they give the
            # time in 10ths of a microsecond but %f only parses down to a microsecond, so just ignore the 10th of a
            # microsecond.  Ie.  remove two chars from the end of the timestamp (the 'Z' and the 10th us)
            'timestamp': datetime.strptime(response_data['CreatedTimestampUtc'][:-2], '%Y-%m-%dT%H:%M:%S.%f'),
            'bid': float(response_data['CurrentHighestBidPrice']),
            'ask': float(response_data['CurrentLowestOfferPrice']),
            'low': float(response_data['DayLowestPrice']),
            'high': float(response_data['DayHighestPrice']),
            'volume': float(response_data['DayVolumeXbt']),
            'last': float(response_data['LastPrice'])
        }
        # {
        #     "CreatedTimestampUtc ": "2014-08-05T06:42:11.3032208Z",
        #     "CurrentHighestBidPrice": 500.00000000,
        #     "CurrentLowestOfferPrice": 1001.00000000,
        #     "DayAvgPrice": 510.000000,
        #     "DayHighestPrice": 510.00000000,
        #     "DayLowestPrice": 510.00000000,
        #     "DayVolumeXbt": 1.00000000,
        #     "DayVolumeXbtInSecondaryCurrrency": 0.75000000,
        #     "LastPrice": 510.00000000,
        #     "PrimaryCurrencyCode": "Xbt",
        #     "SecondaryCurrencyCode": "Usd"
        # }

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
