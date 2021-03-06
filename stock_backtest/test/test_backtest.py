import unittest
import datetime as dt
from queue import Queue
from trading.stock import Stock
from stock_backtest.backtest import StockBacktest
from stock_backtest.data_handler import StockBacktestDataHandler
from stock_backtest.execution_handler import StockBacktestExecutionHandler
from strategies.buy_strategy_stock import BuyStrategy


class TestStockBacktest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.events = Queue()
        cls.start_date = dt.datetime(year=2015, month=12, day=1)
        cls.end_date = dt.datetime(year=2015, month=12, day=31)
        cls.products = [Stock('MSFT')]
        cls.data = StockBacktestDataHandler(cls.events, cls.products, cls.start_date, cls.end_date)
        cls.execution = StockBacktestExecutionHandler(cls.events)
        cls.strategy = BuyStrategy(cls.events, cls.data, cls.products)
        cls.backtest = StockBacktest(cls.events, cls.strategy, cls.data, cls.execution, cls.start_date, cls.end_date)


    def test_run_backtest(self):
        self.backtest.run()
        print type(self.strategy.positions_series)