# -*- coding: utf-8 -*-
'''
Created on 2018年4月6日

@author: Loong
'''
from util.logutil import logger
from config import configs
from bs4 import BeautifulSoup
from util.decode import decode
from urllib.request import urlopen


class Spider():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def get_novel_baseurl(self):
        return configs['baseurl']
    
    def get_novel_filepath(self):
        return configs['novel_path']
    
    def get_novel_filename(self):
        return configs['novel_name']

    def get_novel_chapter_urls(self, novel_baseurl):
        if novel_baseurl is None:
            return None
        response = urlopen(novel_baseurl)
        if response.getcode() != 200:
            return None
        
        tag_as = list()
        html = decode(response.read())
        soup = BeautifulSoup(html, "html.parser")
        tag_a = soup.findAll('a', attrs={'style':'font-size:13px'})
        for tag in tag_a:
            chapter_href = tag.get('href')
            if chapter_href is None or chapter_href == "":
                continue
            index = chapter_href[0:chapter_href.index(".")]
            tag_as.append(int(index))
        tag_as.sort()
        
        chapter_urls = list()
        for chapter in tag_as:
            chapter_urls.append(self.create_chapter_url(novel_baseurl, chapter))
        return chapter_urls
    
    def create_chapter_url(self, novel_baseurl , chapter):
        chapter_url = novel_baseurl + "/" + str(chapter) + ".html"
        return chapter_url
    
    def get_novel_chapter_content(self, chapter_url):
        content = "";
        if chapter_url is None:
            return content
        response = urlopen(chapter_url)
        if response.getcode() != 200:
            return content
        
        html = decode(response.read())
        soup = BeautifulSoup(html, "html.parser")
        chapter_name_tag = soup.h3.string
        content_div_strings = soup.find("div", class_="txt").stripped_strings
        content = chapter_name_tag + "\n"
        for content_str in content_div_strings:
            content += "        " + content_str + "\n"
        return content
    
    def getNovel(self):
        # 1.获取小说主页根路径
        novel_baseurl = self.get_novel_baseurl();
            
        # 2.根据根路径获取章节路径
        chapter_urls = self.get_novel_chapter_urls(novel_baseurl);
        # 3.根据章节路径获取章节内容，并写入txt文档
        with open(self.get_novel_filepath() + "/" + self.get_novel_filename() + ".txt", "w+",encoding='gb18030') as document:
            for chapter_url in chapter_urls:
                content = self.get_novel_chapter_content(chapter_url)
                logger.info(chapter_url)
                document.write("\n");
                document.write(content);
        return

        
if __name__ == '__main__':
    logger.info(Spider().getNovel());    
