import requests


class APIResponse(requests.Response):
    """Formatted Response base class"""

    def __init__(self, method, params, response):
        assert (isinstance(response, requests.Response))  # can't remember if this is good practice in python
        self.__class__ = type(response.__class__.__name__,
                              (self.__class__, response.__class__),
                              {})
        self.__dict__ = response.__dict__
        # super(APIResponse, self).__init__()
        self.called_method = method  # need to know the type of method so we know how to format it, just a string
        self.called_method_params = params  # do we need this?
        self.response = response  # could be called response instead of raw

    # def __getattr__(self, attr):
    #     if attr in self.__dict__:
    #         return getattr(self, attr)
    #     return getattr(self.response, attr)

    @property
    def formatted(self):
        func_name = '_format_' + self.called_method
        func = getattr(self, func_name, None)
        if func is None:
            raise NotImplementedError
        return func(self.response)

    def _format_ticker(self, response):
        raise NotImplementedError

    def _format_order_book(self, response):
        raise NotImplementedError

    def _format_trades(self, response):
        raise NotImplementedError

    def _format_ask(self, response):
        raise NotImplementedError

    def _format_bid(self, response):
        raise NotImplementedError

    def _format_order_status(self, response):
        raise NotImplementedError

    def _format_open_orders(self, response):
        raise NotImplementedError

    def _format_cancel_order(self, response):
        raise NotImplementedError

    def _format_wallet(self, response):
        raise NotImplementedError
