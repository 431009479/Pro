#!/usr/bin/env python
# coding=utf-8

import re


p = re.compile(r')
url = re.findall(r'<a href="(.*?)".*?>下一页&gt;</a>',str)
