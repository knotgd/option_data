# @Time : 2020/7/23
# @Author : 大太阳小白
# @Software: PyCharm
# @blog：https://blog.csdn.net/weixin_41579863
import requests
import pandas as pd
from typing import Any
from abc import ABC


class BaseEngine(ABC):
    """
    负责网络请求，并设计数据组装步骤
    """
    def __init__(self, api: str):
        """
        定义http接口
        :param api:
        """
        self.api = api

    def columns(self):
        """
        设置返回字段
        :return:
        """
        pass

    def convert_format(self, symbols: Any):
        """
        对api接口进行拼接转换
        :param symbols:
        :return:
        """
        pass

    def run(self, symbols) -> Any:
        headers = { 'Referer':"http://finance.sina.com.cn"}
        uri = self.convert_format(symbols)
        data = requests.get(uri, params=None, headers=headers)
        ticks = self.parser(data)
        return ticks

    def get_info(self, symbols):
        """
        批量获取信息
        :param symbols:
        :return:
        """
        ticks = self.run(symbols)
        return pd.DataFrame(ticks, columns=self.columns())

    def parser(self, data):
        """
        对网络请求的结果进行加工解析
        :param data:
        :return:
        """
        pass
#
#
# if __name__ == '__main__':
#     data = requests.get("http://guba.eastmoney.com/list,so10002111.html")
#     soup = BeautifulSoup(data.content,  # HTML文档字符串
#                          'html.parser',  # HTML解析器
#                          from_encoding='utf-8'  # HTML文档编码
#                          )
#     title = soup.find('title')
#     print(title)