# @Time : 2020/7/23
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from core.engine import BaseEngine
from core.constant import SINA_MONTYLY_CON, SINA_UP_OPTION, SINA_DOWN_OPTION
import json
from core.constant import QUOTE_EASTMONEY_OPTION_NAME
from bs4 import BeautifulSoup


class Monthly(BaseEngine):
    """
    获取指定标的当前可交易的合约月份
    """

    def __init__(self):
        super().__init__(SINA_MONTYLY_CON)

    def columns(self):
        return ['月份']

    def convert_format(self, symbol: str):
        return self.api.format(symbol)

    def parser(self, data):
        result = json.loads(data.text)
        months = result['result']['data']['contractMonth']
        return sorted(list(set(months)))


class ContractUp(BaseEngine):
    """
    获取指定月份的认购合约
    """
    def __init__(self):
        super().__init__(SINA_UP_OPTION)

    def columns(self):
        return ['编码']

    def convert_format(self, symbol: str):
        return self.api.format(*symbol)

    def parser(self, data):
        ticks = data.text.splitlines()
        ticks = [str(item).split('\"')[1].split(',') for item in ticks][0][:-1]
        ticks = [str(item).replace('CON_OP_', '') for item in ticks]
        return ticks


class ContractDown(BaseEngine):
    """
    获取指定月份的认沽合约
    """
    def __init__(self):
        super().__init__(SINA_DOWN_OPTION)

    def columns(self):
        return ['编码']

    def convert_format(self, symbol: str):
        return self.api.format(*symbol)

    def parser(self, data):
        ticks = data.text.splitlines()
        ticks = [str(item).split('\"')[1].split(',') for item in ticks][0][:-1]
        ticks = [str(item).replace('CON_OP_', '') for item in ticks]
        return ticks


class ContractName(BaseEngine):

    def __init__(self):
        super().__init__(QUOTE_EASTMONEY_OPTION_NAME)

    def columns(self):
        return ['名称']

    def convert_format(self, symbol: str):
        return self.api.format(symbol)

    def get_info(self, symbols):
        ticks = self.run(symbols)
        return ticks

    def parser(self, data):
        soup = BeautifulSoup(data.content, 'html.parser', from_encoding='utf-8')
        title = soup.find('title')
        return str(title).split('股吧')[0].replace('<title>', '')


