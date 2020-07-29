# @Time : 2020/7/22
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from enum import Enum

# 获取标的当前可交易的合约月接口
SINA_MONTYLY_CON = "http://stock.finance.sina.com.cn/futures/api/openapi.php/StockOptionService.getStockName?exchange=null&cate={}"
# 获取指定月份指定标的的看涨期权合约接口
SINA_UP_OPTION = "http://hq.sinajs.cn/list=OP_UP_{}{}"
# 获取指定月份指定标的的看跌期权合约接口
SINA_DOWN_OPTION = "http://hq.sinajs.cn/list=OP_DOWN_{}{}"
# 获取指定期权合约实时行情接口
SINA_REAL_TICK = "http://hq.sinajs.cn/list={}"
# 获取指定期权合约实时隐波、希腊字母接口
SINA_OPTION_GREEKS = "http://hq.sinajs.cn/list=CON_SO_{}"
# 获取指定期权合约分时行情接口
SINA_OPTION_MIN = "https://stock.finance.sina.com.cn/futures/api/openapi.php/StockOptionDaylineService.getOptionMinline?symbol=CON_OP_{}"
# 获取指定期权合约K线行情接口
SINA_OPTION_K = "http://stock.finance.sina.com.cn/futures/api/jsonp_v2.php//StockOptionDaylineService.getSymbolInfo?symbol=CON_OP_{}"
# 获取指定期权合约5个交易日分时行情接口
SINA_OPTION_LAST_5_MIN = "http://stock.finance.sina.com.cn/futures/api/openapi.php/StockOptionDaylineService.getFiveDayLine?symbol=CON_OP_{}"
# 获取期权名称
QUOTE_EASTMONEY_OPTION_NAME = "http://guba.eastmoney.com/list,so{}.html"


class Underlying(Enum):

    SZ50 = "50ETF"
    HS300 = "300ETF"
    SZ_50_SYMBOL = "510050"
    SZ_300_SYMBOL = "510300"


