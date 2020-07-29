# @Time : 2020/7/27
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
from typing import Any

from core.engine import BaseEngine
from core.constant import SINA_OPTION_K,SINA_OPTION_LAST_5_MIN
import json
import pandas as pd
import re

class TimeSharingOption(BaseEngine):

    def __init__(self):
        super().__init__(SINA_OPTION_LAST_5_MIN)

    def columns(self):
        return '时间,价格,成交,持仓,均价,日期'.split(',')

    def convert_format(self, symbol):
        return self.api.format(symbol)

    def parser(self, data):
        data = json.loads(data.content)['result']['data']
        source_data = []
        date_str = ''
        for item in data:
            for row in item:
                if 'd' in row:
                    date_str = row['d']
                row['i'] = '{} {}'.format(date_str, row['i'])
                row['d'] = date_str
                source_data.append(row)
        return source_data

    def get_info(self, symbols):
        ticks = self.run(symbols)
        ticks_pd = pd.DataFrame(ticks)
        ticks_pd.columns = self.columns()
        return ticks_pd


class KTimeSharingOption(BaseEngine):

    def __init__(self):
        super().__init__(SINA_OPTION_K)

    def columns(self):
        return '时间,开盘,最高,最低,收盘,成交'.split(',')

    def convert_format(self, symbol):
        return self.api.format(symbol)

    def parser(self, data):
        content = re.findall(r'[^()]+', str(data.content))[1]
        data = json.loads(content)
        return data

    def get_info(self, symbols):
        ticks = self.run(symbols)
        ticks_pd = pd.DataFrame(ticks)
        ticks_pd.columns = self.columns()
        return ticks_pd


