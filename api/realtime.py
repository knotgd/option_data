# @Time : 2020/7/23
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from core.engine import BaseEngine
from core.constant import SINA_REAL_TICK


class TickSimple(BaseEngine):

    def __init__(self):
        super().__init__(SINA_REAL_TICK)

    def columns(self):
        return '证券简称,最新价,涨跌额,涨跌幅,成交量,成交额'.split(',')

    def convert_format(self, symbol):
        symbols = ["s_{}{}".format(*value.lower().split('.')[::-1]) for value in symbol]
        return self.api.format(','.join(symbols))

    def parser(self, data: str):
        ticks = data.text.splitlines()
        return [str(item).split('\"')[1].split(',') for item in ticks]


class TickQuality(BaseEngine):

    def __init__(self):
        super().__init__(SINA_REAL_TICK)

    def columns(self):
        return '证券简称,今日开盘价,昨日收盘价,最近成交价,最高成交价,最低成交价,买入价,卖出价,成交数量,成交金额,' \
               '买数量一,买价位一,买数量二,买价位二,买数量三,买价位三,买数量四,买价位四,买数量五,买价位五,卖数量一,' \
               '卖价位一,卖数量二,卖价位二,卖数量三,卖价位三,卖数量四,卖价位四,卖数量五,卖价位五,行情日期,行情时间,' \
               '停牌状态,1'.split(',')

    def convert_format(self, symbol):
        symbols = ["{}{}".format(*value.lower().split('.')[::-1]) for value in symbol]
        return self.api.format(','.join(symbols))

    def parser(self, data: str):
        ticks = data.text.splitlines()
        return [str(item).split('\"')[1].split(',') for item in ticks]


class TickOption(BaseEngine):

    def __init__(self):
        super().__init__(SINA_REAL_TICK)

    def columns(self):
        return '买量,买价,最新价,卖价,卖量,持仓量,涨幅,行权价,昨收价,开盘价,涨停价,跌停价,' \
               '申卖价五,申卖量五,申卖价四,申卖量四,申卖价三,申卖量三,申卖价二,申卖量二,申卖价一,' \
               '申卖量一,申买价一,申买量一 ,申买价二,申买量二,申买价三,申买量三,申买价四,申买量四,' \
               '申买价五,申买量五,行情时间,主力合约标识,状态码,标的证券类型,标的股票,期权合约简称,振幅,' \
               '最高价,最低价,成交量,成交额,分红调整标志,昨结算价,认购认沽标志,到期日,剩余天数,虚实值标志,' \
               '内在价值,时间价值'.split(',')

    def convert_format(self, symbol):
        symbols = ["CON_OP_{}".format(value) for value in symbol]
        return self.api.format(','.join(symbols))

    def parser(self, data: str):
        ticks = data.text.splitlines()
        return [str(item).split('\"')[1].split(',') for item in ticks]


class TickOptionGreeks(BaseEngine):

    def __init__(self):
        super().__init__(SINA_REAL_TICK)

    def columns(self):
        return '期权合约简称,1,2,3,4,成交量,Delta,Gamma,Theta,Vega,隐含波动率,最高价,最低价,交易代码,行权价,最新价,理论价值'.split(',')

    def convert_format(self, symbol):
        symbols = ["CON_SO_{}".format(value) for value in symbol]
        return self.api.format(','.join(symbols))

    def parser(self, data: str):
        ticks = data.text.splitlines()
        return [str(item).split('\"')[1].split(',') for item in ticks]



