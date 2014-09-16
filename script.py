#!/usr/bin/python
# -*- coding: utf-8 -*-
import lxml.html as lh
import requests

r = requests.post('http://bash.im')
html = lh.fromstring(r.text)
for i in html.cssselect('div.quote div.text'):
    print lh.tostring(i)
    print '<hr>'
