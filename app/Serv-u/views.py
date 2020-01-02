import os

import requests
from bs4 import BeautifulSoup


class DataPicker:
    '''
    数据采集器。
    '''

    def __init__(self, url):
        # 初始化时接受一个采集地址
        self._url = url
        self._res = None

    def get_data(self):
        # get方法直接采集
        try:
            res = requests.get(self._url)
            self._res = res.text
            print('抓取数据成功....')
        except Exception as e:
            print('爬取数据出错： %s ' % e)
            raise e
        return self._res


class DataClean:
    '''
    数据清洗器
    可以解析HTML中的版本信息
    '''

    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._version_list = None

    def Clean(self):
        soup = BeautifulSoup(self._raw_data, 'html.parser')
        version_tags = soup.find_all('h2')
        version_list = [item.get_text().lower() for item in version_tags]
        print(version_list)
        self._version_list = version_list
        print('解析数据成功....')
        return self._version_list


class FileGen:
    '''
    文件生成器，生成版本列表的txt文件
    '''

    def __init__(self, version_list):
        self._version_list = version_list

    def write_data(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'result.txt', mode='w', encoding='utf-8')  as f:
            for line in self._version_list:
                f.writelines(line + '\n')
        print('写文件成功....')


if __name__ == '__main__':
    url = r'https://documentation.solarwinds.com/en/success_center/servu/Content/previous_versions.htm'
    # 抓取数据
    res = DataPicker(url).get_data()
    # 格式化数据，获得版本列表
    version_list = DataClean(res).Clean()
    # 写文件
    FileGen(version_list).write_data()
