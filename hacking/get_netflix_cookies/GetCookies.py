import requests
import re
from notion.client import NotionClient
from notion.block import TodoBlock
from notion.block import DividerBlock
from notion.block import SubsubheaderBlock
from notion.block import ToggleBlock
from notion.block import TextBlock
import requests
import json
import datetime
import schedule
import time
import sys

def getCookies():
    # payload = {'userLoginId':'patrick.piette@gmail.com', 'password':'connect01'}
    output = []

    with requests.Session() as s:
        r = s.get('https://www.netflix.com/ca/')
        # p = s.post('https://www.netflix.com/ca/login', data=payload)    
        # print(r.text)
        for cookie in r.cookies:
            output += [[cookie.name, cookie.value, cookie.domain]]
    return(output)

def sendCookies():
    client = NotionClient(token_v2="a101688b1a347ab26b980ee4ccde34355620c02f56039bd8d94359cfb8efe54909d58a41f73a4b134c2ca3eb58306e54269b8cabd5232972209a9b72291286b7e02715780b265a6caa3549712e39")
    page = client.get_block("https://www.notion.so/Cookies-efe872d38ff744a5bb99b35803da55e7")
    data = getCookies()
    newchild = page.children.add_new(DividerBlock)
    newchild = page.children.add_new(TextBlock,title=str(datetime.datetime.now()).split(" ")[0])
    for i in range(len(data)):
        newchild = page.children.add_new(TextBlock,title=data[i][0] + "  |  " + data[i][1])
        
sendCookies()

