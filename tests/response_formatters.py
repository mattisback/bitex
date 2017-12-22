import unittest

import math

import bitex
from datetime import datetime
from unittest.mock import patch, Mock
import requests
import json
from freezegun import freeze_time


class MockResponse(requests.Response):
    def __init__(self, json_data, status_code):
        super().__init__()
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def check_ticker_format(formatted_response):
    result = formatted_response.formatted
    assert 'timestamp' in result
    assert 'bid' in result
    assert 'ask' in result
    assert 'low' in result
    assert 'high' in result
    assert 'volume' in result
    assert 'last' in result

    assert isinstance(result['timestamp'], datetime)
    assert isinstance(result['bid'], float)
    assert isinstance(result['ask'], float)
    assert isinstance(result['low'], float)
    assert isinstance(result['high'], float)
    assert isinstance(result['volume'], float)
    assert isinstance(result['last'], float)


class BinanceFormattingTests(unittest.TestCase):
    @patch('requests.request')
    def test_ticker(self, mock_request):
        exchange_info_data = json.load(open('example_responses/binance/api_v1_exchangeInfo.txt'))
        mock_request.side_effect = [MockResponse(exchange_info_data, 200),  # supported pairs
                                    MockResponse({'symbol': 'LTCBTC',
                                                  'priceChange': '0.00077900',
                                                  'priceChangePercent': '4.862',
                                                  'weightedAvgPrice': '0.01654431',
                                                  'prevClosePrice': '0.01604100',
                                                  'lastPrice': '0.01680000',
                                                  'lastQty': '3.16000000',
                                                  'bidPrice': '0.01680000',
                                                  'bidQty': '90.41000000',
                                                  'askPrice': '0.01680200',
                                                  'askQty': '6.08000000',
                                                  'openPrice': '0.01602100',
                                                  'highPrice': '0.01720000',
                                                  'lowPrice': '0.01592900',
                                                  'volume': '280075.72000000',
                                                  'quoteVolume': '4633.66016380',
                                                  'openTime': 1513517073466,
                                                  'closeTime': 1513603473466,
                                                  'firstId': 2256032,
                                                  'lastId': 2318568,
                                                  'count': 62537}, 200)]

        with freeze_time('2017-12-18 20:35:44'):
            formatted_response = bitex.Binance().ticker('LTCBTC')

        check_ticker_format(formatted_response)
        self.assertDictEqual(formatted_response.formatted,
                             {
                                 'timestamp': datetime(2017, 12, 18, 20, 35, 44, 0),
                                 'bid': 0.01680000,
                                 'ask': 0.01680200,
                                 'low': 0.01592900,
                                 'high': 0.01720000,
                                 'volume': 280075.72000000,
                                 'last': 0.01680000,
                             })


class BitfinexFormattingTests(unittest.TestCase):
    @patch('requests.request')
    def test_ticker(self, mock_request):
        mock_request.side_effect = [MockResponse({'btcusd', 'ltcusd'}, 200),  # supported pairs
                                    MockResponse({'bid': '18629.0',
                                                  'timestamp': '1513589744.5260189',
                                                  'ask': '18630.0',
                                                  'mid': '18629.5',
                                                  'low': '18010.0',
                                                  'volume': '63690.87027664',
                                                  'last_price': '18630.0',
                                                  'high': '19891.0'}, 200)]

        formatted_response = bitex.Bitfinex().ticker(bitex.BTCUSD)

        check_ticker_format(formatted_response)
        self.assertDictEqual(formatted_response.formatted,
                             {
                                 'timestamp': datetime(2017, 12, 18, 20, 35, 44, 526019),
                                 'bid': 18629.0,
                                 'ask': 18630.0,
                                 'low': 18010.0,
                                 'volume': 63690.87027664,
                                 'last': 18630.0,
                                 'high': 19891.0
                             })


class BitstampFormattingTests(unittest.TestCase):
    @patch('requests.request')
    def test_ticker(self, mock_request):
        mock_request.side_effect = [  # MockResponse({'btcusd', 'ltcusd'}, 200),  # supported pairs
            MockResponse({'bid': '18795.00',
                          'open': '18953.00',
                          'timestamp': '1513589738',
                          'ask': '18831.82',
                          'volume': '13558.68696337',
                          'low': '17835.20',
                          'high': '19666.00',
                          'vwap': '18809.34',
                          'last': '18832.93'}, 200)]

        formatted_response = bitex.Bitstamp().ticker(bitex.BTCUSD)

        check_ticker_format(formatted_response)
        self.assertDictEqual(formatted_response.formatted,
                             {
                                 'timestamp': datetime(2017, 12, 18, 20, 35, 38, 0),
                                 'bid': 18795.00,
                                 'ask': 18831.82,
                                 'low': 17835.20,
                                 'high': 19666.00,
                                 'volume': 13558.68696337,
                                 'last': 18832.93,
                             })


class BittrexFormattingTests(unittest.TestCase):
    @patch('requests.request')
    def test_ticker(self, mock_request):
        exchange_info_data = json.load(open('example_responses/bittrex/api_v1.1_public_getmarkets.txt'))
        mock_request.side_effect = [MockResponse(exchange_info_data, 200),  # supported pairs
                                    MockResponse({"success": True,
                                                  "message": "",
                                                  "result": [{"MarketName": "BTC-LTC",
                                                              "High": 0.01980000,
                                                              "Low": 0.01710000,
                                                              "Volume": 351275.48627484,
                                                              "Last": 0.01793009,
                                                              "BaseVolume": 6651.09475051,
                                                              "TimeStamp": "2017-12-22T12:01:51.87",
                                                              "Bid": 0.01793502,
                                                              "Ask": 0.01804016,
                                                              "OpenBuyOrders": 4055,
                                                              "OpenSellOrders": 6906,
                                                              "PrevDay": 0.01889867,
                                                              "Created": "2014-02-13T00:00:00"}]}, 200)]

        formatted_response = bitex.Bittrex().ticker('BTC-LTC')

        check_ticker_format(formatted_response)
        self.assertDictEqual(formatted_response.formatted,
                             {'timestamp': datetime(2017, 12, 22, 12, 1, 51, 870000),
                              'bid': 0.01793502,
                              'ask': 0.01804016,
                              'low': 0.01710000,
                              'high': 0.01980000,
                              'volume': 6651.09475051,
                              'last': 0.01793009})


class CCEXFormattingTests(unittest.TestCase):
    @patch('requests.request')
    def test_ticker(self, mock_request):
        exchange_info_data = json.load(open('example_responses/ccex/pairs.json'))
        mock_request.side_effect = [MockResponse(exchange_info_data, 200),  # supported pairs
                                    MockResponse({'ticker': {'updated': 1513591935,
                                                             'lastbuy': 0.03794999,
                                                             'buy': 0.03794999,
                                                             'sell': 0.03798,
                                                             'buysupport': 7.03034809,
                                                             'lastprice': 0.03794999,
                                                             'high': 0.03879995,
                                                             'low': 0.03600001,
                                                             'avg': 0.03739998,
                                                             'lastsell': 0.03794999}}, 200)]

        formatted_response = bitex.CCEX().ticker(bitex.BTCUSD)

        check_ticker_format(formatted_response)
        self.assertDictContainsSubset(
            {'timestamp': datetime(2017, 12, 18, 21, 12, 15),
             'bid': 0.03794999,
             'ask': 0.03798,
             'low': 0.03600001,
             'high': 0.03879995,
             # 'volume': float('nan'), # checking for nan doesn't work here!
             'last': 0.03794999}, formatted_response.formatted)
        self.assertTrue(math.isnan(formatted_response.formatted['volume']))


class CoinCheckFormattingTests(unittest.TestCase):
    @patch('requests.request')
    def test_ticker(self, mock_request):
        exchange_info_data = json.load(open('example_responses/ccex/pairs.json'))
        mock_request.side_effect = [  # MockResponse(exchange_info_data, 200),  # supported pairs
            MockResponse({"last": 2171460.0,
                          "bid": 2171460.0,
                          "ask": 2171871.0,
                          "high": 2277722.0,
                          "low": 2000000.0,
                          "volume": 42302.59403478,
                          "timestamp": 1513592823}, 200)]

        formatted_response = bitex.CoinCheck().ticker('btc-jpy')

        check_ticker_format(formatted_response)
        self.assertDictEqual(formatted_response.formatted,
                             {'timestamp': datetime(2017, 12, 18, 21, 27, 3),
                              'bid': 2171460.0,
                              'ask': 2171871.0,
                              'low': 2000000.0,
                              'high': 2277722.0,
                              'volume': 42302.59403478,
                              'last': 2171460.0})


class CryptopiaFormattingTests(unittest.TestCase):
    @patch('requests.request')
    def test_ticker(self, mock_request):
        exchange_info_data = json.load(open('example_responses/cryptopia/GetTradePairs.json'))
        mock_request.side_effect = [MockResponse(exchange_info_data, 200),  # supported pairs
                                    MockResponse({'Error': None,
                                                  'Message': None,
                                                  'Success': True,
                                                  'Data': {'BaseVolume': 115.20140042,
                                                           'SellBaseVolume': 7895377.3822143,
                                                           'Label': 'ETH/BTC',
                                                           'SellVolume': 610.85063355,
                                                           'Close': 0.03827886,
                                                           'Change': 4.87,
                                                           'LastPrice': 0.03827886,
                                                           'AskPrice': 0.03827886,
                                                           'Volume': 3086.02843597,
                                                           'Low': 0.03526454,
                                                           'BuyVolume': 696183.93492498,
                                                           'BidPrice': 0.03820002,
                                                           'High': 0.03899999,
                                                           'Open': 0.0365,
                                                           'TradePairId': 5203,
                                                           'BuyBaseVolume': 11.94683624}}, 200)]

        with freeze_time('2017-12-18 20:35:44'):
            formatted_response = bitex.Cryptopia().ticker('ETH_BTC')

            check_ticker_format(formatted_response)
            self.assertDictEqual(formatted_response.formatted,
                                 {
                                     'timestamp': datetime(2017, 12, 18, 20, 35, 44, 0),
                                     'bid': 0.03820002,
                                     'ask': 0.03827886,
                                     'low': 0.03526454,
                                     'high': 0.03899999,
                                     'volume': 3086.02843597,
                                     'last': 0.03827886
                                 })


class PoloniexFormattingTests(unittest.TestCase):
    @patch('requests.request')
    def test_ticker(self, mock_request):
        return_ticker_data = json.loads(open('example_responses/poloniex/returnTicker.txt').read().replace("'", '"'))
        mock_request.side_effect = [MockResponse(return_ticker_data, 200),  # supported pairs
                                    MockResponse(return_ticker_data, 200)]

        with freeze_time('2017-12-18 20:35:44'):
            formatted_response = bitex.Poloniex().ticker('USDT_BTC')

        check_ticker_format(formatted_response)
        self.assertDictEqual(formatted_response.formatted,
                             {
                                 'timestamp': datetime(2017, 12, 18, 20, 35, 44, 0),
                                 'bid': 13730.00000013,
                                 'ask': 13754.97450170,
                                 'low': 13164.61000000,
                                 'high': 17375.98798753,
                                 'volume': 243864092.21685281,
                                 'last': 13730.00000013
                             })


if __name__ == '__main__':
    unittest.main()
