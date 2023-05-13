# -*- coding:utf-8 -*-
import requests
from lxml import etree
from datetime import datetime

def split():
    link = 'https://www.arthur-conan-doyle.com/index.php?title=A_Study_in_Scarlet#Chapter_1:_Mr_Sherlock_Holmes'

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    r = requests.get(link, headers=header, timeout=2000)
    r.encoding = 'utf-8'
    html = etree.HTML(r.text)
    titles = html.xpath('//*[@id="mw-content-text"]/div//h4//*[@class="mw-headline"]/text()')
    print(type(titles[0]))
    targets = []
    for i in range(0,len(titles)):
        targets.append(str(titles[i]))
    print(len(targets))
    source_dir = r'A Study in Scarlet.txt'
    target_dir = r'../content/'
    # 文件名索引值
    flag = 0
    # 文件名
    name = titles[0]
    # 存放数量
    dataset = []
    print("开始拆分……")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    #读取source文件，每遇到字符为’\n‘时,写入到一个新的txt文件中(判断逻辑可以更换)
    with open(source_dir,'r',encoding='utf-8') as f_source:
        for line in f_source:
            dataset.append(line)
            if line == '\n':
                with open(target_dir +targets[flag]+".txt" ,'w+',encoding='utf-8') as f_target:
                    for data in dataset:
                        f_target.write(data)
                flag += 1
                dataset = []

    with open(target_dir +targets[flag]+".txt",'w+',encoding='utf-8') as f_target:
        for data in dataset:
            f_target.write(data)

    print("拆分完成！")
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def main():
    split()

if __name__ == "__main__":
    main()

