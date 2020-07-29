# @Time : 2020/7/29
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from apps.option_data import *

if __name__ == '__main__':
    # 获取合约名称
    test_contract_name = contract_name('10001011')
    print(test_contract_name)

    # 获取指定标的可交易月份合约
    test_contract_monthly = contract_monthly('300ETF')
    print(test_contract_monthly)

    # 获取指定标的、时间、可交易的认购期权合约
    test_contract_up = contract_up("510050", "2009")
    print(test_contract_up)

    # 获取指定标的、时间、可交易的认沽期权合约
    test_contract_down = contract_down("510050", "2009")
    print(test_contract_down)

    # 获取指定编码的股票tick简易行情
    test_tick_simple = tick_simple(['510050.SH', '603000.SH'])
    print(test_tick_simple)

    # 获取指定编码的股票tick高质量行情
    test_tick_quality = tick_quality(['510050.SH', '603000.SH'])
    print(test_tick_quality)

    # 获取期权tick行情数据
    test_tick_option = tick_option(['10002591', '10002592'])
    print(test_tick_option)

    # 获取指定多个期权合约的希腊字母
    test_option_greeks = option_greeks(['10002591', '10002592'])
    print(test_option_greeks)

    # 获取期权分时行情，默认最近5日分时行情
    test_option_minline = option_minline('10002591')
    print(test_option_minline)

    # 获取期权k线数据
    test_option_k_bar = option_k_bar('10002591')
    print(test_option_k_bar)
