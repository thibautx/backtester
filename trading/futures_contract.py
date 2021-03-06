import datetime as dt
import futures_utils as fut
# from ib.utils import create_ib_futures_contract
# from futures_utils import build_contract, get_contract_specs, get_mkt_times, get_highest_volume_contract

class FuturesContract(object):
    def __init__(self, base_symbol, exp_year=None, exp_month=None, continuous=False):
        self.exp_year = exp_year if exp_year is not None else dt.datetime.now().year
        self.exp_month = exp_month if exp_month is not None else dt.datetime.now().month

        self.base_symbol = base_symbol
        self.symbol = fut.build_contract(self.base_symbol, self.exp_year, self.exp_month)

        specs = fut.get_contract_specs(self.base_symbol)
        self.name = specs['Name']
        self.exchange = specs['Exchange']
        self.tick_value = float(specs['Tick Value'])
        self.contract_size = specs['Contract Size']
        self.active = specs['Active']
        self.deliver_months = specs['Delivery Months']
        self.units = specs['Units']
        self.currency = specs['Currency']
        self.trading_times = specs['Trading Times']
        self.min_tick_value =  (specs['Minimum Tick Value'])
        self.full_point_value = float(specs['Full Point Value'])
        self.terminal_point_value = float(specs['Terminal Point Value'])

        self.contract_multiplier = self.full_point_value*self.terminal_point_value

        self.mkt_open, self.mkt_close = fut.get_mkt_times(self.trading_times)
        # self.ib_contract = create_ib_futures_contract(self.base_symbol,
        #                                               exp_month=self.exp_month,
        #                                               exp_year=self.exp_year,
        #                                               exchange=self.exchange,
        #                                               currency=self.currency)


        self.continuous = continuous

    def update(self, year, month, day):
        self.symbol = fut.get_highest_volume_contract(self.base_symbol, year, month, day)
        self.exp_year = fut.get_exp_year_from_symbol(self.symbol)
        self.exp_month = fut.get_exp_month_from_symbol(self.symbol)


