import abc
import requests
# from enum import Enum


# class InterfaceMethod(Enum):
#     UNKNOWN = 0
#     TICKER = 1
#     ORDER_BOOK = 2
#     TRADES = 3
#     ASK = 4
#     BID = 5
#     ORDER_STATUS = 6
#     OPEN_ORDERS = 7
#     CANCEL_ORDER = 8
#     WALLET = 9


class FormattedResponse(metaclass=abc.ABCMeta):
    """Formatted Response base class"""

    def __init__(self, method, params, response):
        assert (isinstance(response, requests.Response))  # can't remember if this is good practice in python
        self.method = method  # need to know the type of method so we know how to format it, just a string
        self.method_params = params  # do we need this?
        self.raw = response  # could be called response instead of raw

    @property
    def formatted(self):
        func_name = '_format_' + self.method
        func = getattr(self, func_name, None)
        if func is None:
            raise NotImplementedError
        return func(self.raw)

    @abc.abstractmethod
    def _format_ticker(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def _format_order_book(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def _format_trades(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def _format_ask(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def _format_bid(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def _format_order_status(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def _format_open_orders(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def _format_cancel_order(self, response):
        raise NotImplementedError

    @abc.abstractmethod
    def _format_wallet(self, response):
        raise NotImplementedError
