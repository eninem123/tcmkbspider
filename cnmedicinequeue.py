# coding=gbk
import requests
import csv, codecs
from lxml import etree
from USER_AGENT_LIST import get_agent
from bs4 import BeautifulSoup
import threading
from queue import Queue
import pymysql



class MedicineSpider(object):
    def __init__(self):
        # 爬取的url
        self.url = 'http://www.tcmkb.cn/search/?keywords={}'
        # useragent
        useragent = get_agent()
        # 组建请求头
        self.headers = {
            'User-Agent': useragent,
        }
        # 响应放到队列
        self.html_queue = Queue()
        # 爬取的数据放到队列
        self.data_queue = Queue()
        self.li = []
        # 爬取的关键词
        self.li_ws1 = ["嘈杂"]
        self.li_ws = ["生"]

    def get_page_from_url(self, url):
        """
        提取url得到响应
        """
        try:
            html = requests.get(url, headers=self.headers).content
            self.html_queue.put(html)
        except Exception as e:
            print("html异常",e)

        # print("html:",type(html))
        # print("html:",html)

    def get_deep_html(self, url, i):
        """
        爬取相关知识条目关键词加到队列里
        """
        try:
            html = requests.get(url, headers=self.headers).content
            s1 = etree.HTML(html)
            # print("get_deep_htmlhtml:", html)
            print("爬取的url:", url)
            print("获取的知识条目关键词:", i)
            # 用BeautifulSoup提取标签内容
            try:
                soup = BeautifulSoup(html, 'lxml')
                # print("get_deep_soup:",soup)
                trs = soup.select('ul li')[63:]
                print("soup的trs:", trs)
                for tr in trs:
                    keywords = tr.string.replace(' ', '')
                    if keywords not in self.li_ws:
                        # 添加到队列
                        self.li_ws.append(keywords)
                        print('添加了新name：', keywords)
                        print("添加后li_ws:", self.li_ws)
                # 如果BeautifulSoup没有，再用xpath提取
                if trs == []:
                    trs = s1.xpath("//ul[@class='nav nav-pills']/li")
                    print("xpath的trs:", trs)
                    for tr in trs:
                        keywords = tr.xpath("./a/text()")[0]
                        print("添加前li_ws:", self.li_ws)
                        if keywords not in self.li_ws:
                            self.li_ws.append(keywords)
                            print('添加了新name：', keywords)
                            print("添加后li_ws:", self.li_ws)
            except Exception as e:
                print("没有nav", e)
        except Exception as e:
            print("html异常", e)

    def get_data_from_page(self, page):
        """
        爬取知识条目内容数据
        """
        data_list = []
        print('原来page类型：', type(page))
        if page:
            s = etree.HTML(page)
            # print(list)
            # 格式都是字符串
            item = {}
            try:
                item['title'] = s.xpath("//div[@class='container']/h1/font/text()")[0]
            except Exception as e:
                print("没有title")
            try:
                # print(item['title'])
                item['tr1'] = s.xpath("//div[@class='container']/table/tr[1]/td/text()")[0]
            except Exception as e:
                print("没有tr1")
            try:
                item['tr2'] = s.xpath("//div[@class='container']/table/tr[2]/td/text()")[0]
            except Exception as e:
                print("没有tr2")
            try:
                item['tr3'] = s.xpath("//div[@class='container']/table/tr[3]/td/text()")[0]
            except Exception as e:
                print("没有tr3")
            try:
                item['tr4'] = s.xpath("//div[@class='container']/table/tr[4]/td/text()")[0]
            except Exception as e:
                print("没有tr4")
            try:
                item['tr5'] = s.xpath("//div[@class='container']/table/tr[5]/td/text()")[0]
            except Exception as e:
                print("没有tr5")
            try:
                item['tr6'] = s.xpath("//div[@class='container']/table/tr[6]/td/text()")[0]
            except Exception as e:
                print("没有tr6")
            try:
                item['tr7'] = s.xpath("//div[@class='container']/table/tr[7]/td/text()")[0]
            except Exception as e:
                print("没有tr7")
            try:
                item['tr8'] = s.xpath("//div[@class='container']/table/tr[8]/td/text()")[0]
            except Exception as e:
                print("没有tr8")
            try:
                item['tr9'] = s.xpath("//div[@class='container']/table/tr[9]/td/text()")[0]
            except Exception as e:
                print("没有tr9")
            try:
                item['tr10'] = s.xpath("//div[@class='container']/table/tr[10]/td/text()")[0]
            except Exception as e:
                print("没有tr10")
            try:
                item['tr11'] = s.xpath("//div[@class='container']/table/tr[11]/td/text()")[0]
            except Exception as e:
                print("没有tr11")
            try:
                item['tr12'] = s.xpath("//div[@class='container']/table/tr[12]/td/text()")[0]
            except Exception as e:
                print("没有tr12")
            try:
                item['tr13'] = s.xpath("//div[@class='container']/table/tr[13]/td/text()")[0]
            except Exception as e:
                print("没有tr13")
            try:
                item['tr14'] = s.xpath("//div[@class='container']/table/tr[14]/td/text()")[0]
            except Exception as e:
                print("没有tr14")
            try:
                item['tr15'] = s.xpath("//div[@class='container']/table/tr[15]/td/text()")[0]
            except Exception as e:
                print("没有tr15")
            try:
                item['tr16'] = s.xpath("//div[@class='container']/table/tr[16]/td/text()")[0]
            except Exception as e:
                print("没有tr16")
            try:
                item['tr17'] = s.xpath("//div[@class='container']/table/tr[17]/td/text()")[0]
            except Exception as e:
                print("没有tr17")
            try:
                item['tr18'] = s.xpath("//div[@class='container']/table/tr[18]/td/text()")[0]
            except Exception as e:
                print("没有tr18")
            try:
                item['tr19'] = s.xpath("//div[@class='container']/table/tr[19]/td/text()")[0]
            except Exception as e:
                print("没有tr19")
            try:
                item['tr20'] = s.xpath("//div[@class='container']/table/tr[20]/td/text()")[0]
            except Exception as e:
                print("没有tr20")
            try:
                item['tr21'] = s.xpath("//div[@class='container']/table/tr[21]/td/text()")[0]
            except Exception as e:
                print("没有tr21")
            try:
                item['tr22'] = s.xpath("//div[@class='container']/table/tr[22]/td/text()")[0]
            except Exception as e:
                print("没有tr22")
            try:
                item['tr23'] = s.xpath("//div[@class='container']/table/tr[23]/td/text()")[0]
            except Exception as e:
                print("没有tr23")
            try:
                item['tr24'] = s.xpath("//div[@class='container']/table/tr[24]/td/text()")[0]
            except Exception as e:
                print("没有tr24")
            try:
                item['tr25'] = s.xpath("//div[@class='container']/table/tr[25]/td/text()")[0]
            except Exception as e:
                print("没有tr25")
            try:
                item['tr26'] = s.xpath("//div[@class='container']/table/tr[26]/td/text()")[0]
            except Exception as e:
                print("没有tr26")
            try:
                item['tr27'] = s.xpath("//div[@class='container']/table/tr[27]/td/text()")[0]
            except Exception as e:
                print("没有tr27")
            try:
                item['tr28'] = s.xpath("//div[@class='container']/table/tr[28]/td/text()")[0]
            except Exception as e:
                print("没有tr28")
            try:
                item['tr29'] = s.xpath("//div[@class='container']/table/tr[29]/td/text()")[0]
            except Exception as e:
                print("没有tr29")
            try:
                item['tr30'] = s.xpath("//div[@class='container']/table/tr[30]/td/text()")[0]
            except Exception as e:
                print("没有tr30")
            try:
                item['tr31'] = s.xpath("//div[@class='container']/table/tr[31]/td/text()")[0]
            except Exception as e:
                print("没有tr31")
            try:
                item['tr32'] = s.xpath("//div[@class='container']/table/tr[32]/td/text()")[0]
            except Exception as e:
                print("没有tr32")
            try:
                item['tr33'] = s.xpath("//div[@class='container']/table/tr[33]/td/text()")[0]
            except Exception as e:
                print("没有tr33")
            try:
                item['tr34'] = s.xpath("//div[@class='container']/table/tr[34]/td/text()")[0]
            except Exception as e:
                print("没有tr34")
            # 添加到字典
            data_list.append(item)
            print('data_list', data_list)
            #  解析结果放到数据队列.
            self.data_queue.put(data_list)
            # 页面数据处理完了, 该响应队列任务完成了
            self.html_queue.task_done()


    def save_data_csv(self, data_list):
        """
        保存数据到csv
        """
        for data in data_list:
            # print(data)
            f = open('tcmkb2.csv', 'w', encoding='utf-8-sig', newline='')
            writer = csv.writer(f)
            # 将提取的字段转化，写入格式，没有的字段为null
            title = data['title'] if ('title' in data) else 'null'
            tr1 = data['tr1'] if ('tr1' in data) else 'null'
            tr2 = data['tr2'] if ('tr2' in data) else 'null'
            tr3 = data['tr3'] if ('tr3' in data) else 'null'
            tr4 = data['tr4'] if ('tr4' in data) else 'null'
            tr5 = data['tr5'] if ('tr5' in data) else 'null'
            tr6 = data['tr6'] if ('tr6' in data) else 'null'
            tr7 = data['tr7'] if ('tr7' in data) else 'null'
            tr8 = data['tr8'] if ('tr8' in data) else 'null'
            tr9 = data['tr9'] if ('tr9' in data) else 'null'
            tr10 = data['tr10'] if ('tr10' in data) else 'null'
            tr11 = data['tr11'] if ('tr11' in data) else 'null'
            tr12 = data['tr12'] if ('tr12' in data) else 'null'
            tr13 = data['tr13'] if ('tr13' in data) else 'null'
            tr14 = data['tr14'] if ('tr14' in data) else 'null'
            tr15 = data['tr15'] if ('tr15' in data) else 'null'
            tr16 = data['tr16'] if ('tr16' in data) else 'null'
            tr17 = data['tr17'] if ('tr17' in data) else 'null'
            tr18 = data['tr18'] if ('tr18' in data) else 'null'
            tr19 = data['tr19'] if ('tr19' in data) else 'null'
            tr20 = data['tr20'] if ('tr20' in data) else 'null'
            tr21 = data['tr21'] if ('tr21' in data) else 'null'
            tr22 = data['tr22'] if ('tr22' in data) else 'null'
            tr23 = data['tr23'] if ('tr23' in data) else 'null'
            tr24 = data['tr24'] if ('tr24' in data) else 'null'
            tr25 = data['tr25'] if ('tr25' in data) else 'null'
            tr26 = data['tr26'] if ('tr26' in data) else 'null'
            tr27 = data['tr27'] if ('tr27' in data) else 'null'
            tr28 = data['tr28'] if ('tr28' in data) else 'null'
            tr29 = data['tr29'] if ('tr29' in data) else 'null'
            tr30 = data['tr30'] if ('tr30' in data) else 'null'
            tr31 = data['tr31'] if ('tr31' in data) else 'null'
            tr32 = data['tr32'] if ('tr32' in data) else 'null'
            tr33 = data['tr33'] if ('tr33' in data) else 'null'
            tr34 = data['tr34'] if ('tr34' in data) else 'null'

            # print('follow:',follow) # 是一个个字符串
            t = (title, tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10, tr11, tr12, tr13, tr14, tr15, tr16, tr17, tr18, tr19, tr20, tr21, tr22, tr23, tr24, tr25, tr26, tr27, tr28, tr29, tr30, tr31, tr32, tr33, tr34)
            self.li.append(t)
            # 列表格式 ：[('xxx',), ('xxx',)]
            # print('list:',self.li)
            # writerows保存多行，格式是[('xxx',), ('xxxx',)] writerow保存单行，格式['a','b']
            writer.writerows([['title', 'tr1', 'tr2', 'tr3', 'tr4', 'tr5', 'tr6', 'tr7', 'tr8', 'tr9', 'tr10', 'tr11',
                               'tr12', 'tr13', 'tr14', 'tr15', 'tr16', 'tr17', 'tr18', 'tr19', 'tr20', 'tr21', 'tr22', 'tr23', 'tr24', 'tr25', 'tr26', 'tr27',
                               'tr28', 'tr29', 'tr30', 'tr31', 'tr32', 'tr33', 'tr34']])
            writer.writerows(self.li)
    def save_data_mysql(self, data_list):
        """
        保存数据到mysql
        """
        for data in data_list:
            # print(data)

            # 将提取的字段转化，写入格式，没有的字段为null,字典取出的数据是lxml类，转化为字符串
            title = data['title'].encode('utf-8').decode('utf-8') if ('title' in data) else 'null'
            tr1 = data['tr1'].encode('utf-8').decode('utf-8') if ('tr1' in data) else 'null'
            tr2 = data['tr2'].encode('utf-8').decode('utf-8') if ('tr2' in data) else 'null'
            tr3 = data['tr3'].encode('utf-8').decode('utf-8') if ('tr3' in data) else 'null'
            tr4 = data['tr4'].encode('utf-8').decode('utf-8') if ('tr4' in data) else 'null'
            tr5 = data['tr5'].encode('utf-8').decode('utf-8') if ('tr5' in data) else 'null'
            tr6 = data['tr6'].encode('utf-8').decode('utf-8') if ('tr6' in data) else 'null'
            tr7 = data['tr7'].encode('utf-8').decode('utf-8') if ('tr7' in data) else 'null'
            tr8 = data['tr8'].encode('utf-8').decode('utf-8') if ('tr8' in data) else 'null'
            tr9 = data['tr9'].encode('utf-8').decode('utf-8') if ('tr9' in data) else 'null'
            tr10 = data['tr10'].encode('utf-8').decode('utf-8') if ('tr10' in data) else 'null'
            tr11 = data['tr11'].encode('utf-8').decode('utf-8') if ('tr11' in data) else 'null'
            tr12 = data['tr12'].encode('utf-8').decode('utf-8') if ('tr12' in data) else 'null'
            tr13 = data['tr13'].encode('utf-8').decode('utf-8') if ('tr13' in data) else 'null'
            tr14 = data['tr14'].encode('utf-8').decode('utf-8') if ('tr14' in data) else 'null'
            tr15 = data['tr15'].encode('utf-8').decode('utf-8') if ('tr15' in data) else 'null'
            tr16 = data['tr16'].encode('utf-8').decode('utf-8') if ('tr16' in data) else 'null'
            tr17 = data['tr17'].encode('utf-8').decode('utf-8') if ('tr17' in data) else 'null'
            tr18 = data['tr18'].encode('utf-8').decode('utf-8') if ('tr18' in data) else 'null'
            tr19 = data['tr19'].encode('utf-8').decode('utf-8') if ('tr19' in data) else 'null'
            tr20 = data['tr20'].encode('utf-8').decode('utf-8') if ('tr20' in data) else 'null'
            tr21 = data['tr21'].encode('utf-8').decode('utf-8') if ('tr21' in data) else 'null'
            tr22 = data['tr22'].encode('utf-8').decode('utf-8') if ('tr22' in data) else 'null'
            tr23 = data['tr23'].encode('utf-8').decode('utf-8') if ('tr23' in data) else 'null'
            tr24 = data['tr24'].encode('utf-8').decode('utf-8') if ('tr24' in data) else 'null'
            tr25 = data['tr25'].encode('utf-8').decode('utf-8') if ('tr25' in data) else 'null'
            tr26 = data['tr26'].encode('utf-8').decode('utf-8') if ('tr26' in data) else 'null'
            tr27 = data['tr27'].encode('utf-8').decode('utf-8') if ('tr27' in data) else 'null'
            tr28 = data['tr28'].encode('utf-8').decode('utf-8') if ('tr28' in data) else 'null'
            tr29 = data['tr29'].encode('utf-8').decode('utf-8') if ('tr29' in data) else 'null'
            tr30 = data['tr30'].encode('utf-8').decode('utf-8') if ('tr30' in data) else 'null'
            tr31 = data['tr31'].encode('utf-8').decode('utf-8') if ('tr31' in data) else 'null'
            tr32 = data['tr32'].encode('utf-8').decode('utf-8') if ('tr32' in data) else 'null'
            tr33 = data['tr33'].encode('utf-8').decode('utf-8') if ('tr33' in data) else 'null'
            tr34 = data['tr34'].encode('utf-8').decode('utf-8') if ('tr34' in data) else 'null'
            # print("title:",title)
            # print("tr1:",tr1)
            # print("tr2:",tr2)
            # print("title:",type(title))
            try:
                conn = pymysql.connect(host='120.78.129.89', port=3306, user='root', password='mysql', db='tcmkbdata',
                                       charset="utf8")

                cursor = conn.cursor()
                try:
                    select_sql = """select * from test where title = %s"""
                except Exception as e:
                    print("select_sql error:",e)
                try:
                    if cursor.execute(select_sql, title) ==0:
                        insert_sql = """insert into test(id,title, tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10, tr11, tr12, tr13, tr14, tr15, tr16, tr17, tr18, tr19, tr20, tr21, tr22, tr23, tr24, tr25, tr26, tr27, tr28, tr29, tr30, tr31, tr32, tr33, tr34)
                                        values(null,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                        cursor.execute(insert_sql, (title, tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10, tr11, tr12, tr13, tr14, tr15, tr16, tr17, tr18, tr19, tr20, tr21, tr22, tr23, tr24, tr25, tr26, tr27, tr28, tr29, tr30, tr31, tr32, tr33, tr34))
                        print("%s导入数据库成功", title)
                except Exception as e:
                    print("%s导入数据库失败", title)
                    print("insert_sql error:", e)
                #print('*********save to mysql********', data)

            except Exception as e:
                print('mysql wrong:',e)
            finally:
                conn.commit()
                cursor.close()
                conn.close()


    def run(self):

        for i in self.li_ws:
            print("爬取：", i)
            print("待爬取li_ws:", self.li_ws)
            # 获取url
            url = self.url.format(i)
            self.get_page_from_url(url)
            # 解析url，放进队列，不阻塞队列
            html = self.html_queue.get(False,)


            # 深层次url
            self.get_deep_html(url, i)


            # 获取数据
            self.get_data_from_page(html)
            try:
                data_list = self.data_queue.get()
            except Exception as e:
                print("----------------datalist is None-----------------")
                print(e)
            finally:
                # 保存数据为csv
                # t1 = threading.Thread(target=self.save_data_csv, args=(data_list,))
                # t1.start()
                self.save_data_mysql(data_list)



if __name__ == '__main__':
    mm = MedicineSpider()
    mm.run()
