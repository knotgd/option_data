# @Time : 2020/7/28
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from api.contract import Monthly, ContractUp, ContractDown, ContractName
from api.realtime import TickOptionGreeks, TickOption, TickQuality, TickSimple
from api.timesharing import TimeSharingOption, KTimeSharingOption


def contract_monthly(underlying: str):
    """
    获取指定标的可以交易的合约月份
    上证50ETF：50ETF，沪深300ETF：300ETF
    :param underlying:
    :return:
    """
    monthly = Monthly()
    return monthly.get_info(underlying)


def contract_up(underlying: str, date: str):
    """
    获取指定标的、时间、可交易的认购期权合约
    :param underlying:
    :param date:
    :return:
    """
    args = [underlying, date]
    up = ContractUp()
    return up.get_info(args)


def contract_down(underlying: str, date: str):
    """
    获取指定标的、时间、可交易的认沽期权合约
    :param underlying:
    :param date:
    :return:
    """
    args = [underlying, date]
    down = ContractDown()
    return down.get_info(args)


def contract_name(symbol: str):
    """
    获取指定期权合约编码的名称
    :param symbol:
    :return:
    """
    c_name = ContractName()
    return c_name.get_info(symbol)


def option_greeks(symbols):
    """
    获取指定多个期权合约的希腊字母
    例如：["10002591", "10002592"]
    :param symbols:
    :return:
    """
    option_greek = TickOptionGreeks()
    return option_greek.get_info(symbols)


def tick_simple(symbols):
    """
    获取指定编码的股票tick简易行情
    例如：["510050.SH", "510300.SH"]
    :param symbols:
    :return:
    """
    simple = TickSimple()
    return simple.get_info(symbols)


def tick_quality(symbols):
    """
    获取高质量tick行情数据
    :param symbols: ["510050.SH", "510300.SH"]
    :return:
    """
    quality = TickQuality()
    return quality.get_info(symbols)


def tick_option(symbols):
    """
    获取期权tick行情数据
    :param symbols:
    :return:
    """
    option = TickOption()
    return option.get_info(symbols)


def option_minline(symbol):
    """
    获取期权分时行情，默认最近5日分时行情
    :param symbol:
    :return:
    """
    time_option = TimeSharingOption()
    return time_option.get_info(symbol)


def option_k_bar(symbol):
    """
    获取期权k线数据
    :param symbol:
    :return:
    """
    k_data = KTimeSharingOption()
    return k_data.get_info(symbol)
