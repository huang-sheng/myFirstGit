# -*- coding: UTF-8 -*-
"""
取 http://www.com1express.net/ 物流信息
"""

import json,sys,re
import urllib.request, urllib.parse

def getTrackingInfo(trackingNo):
	url = "http://www.com1express.net/getPodInfoByWaybillNum.html"
	data = urllib.parse.urlencode({'waybillNum': trackingNo}).encode('utf-8')
	headers = {
		'Referer': 'http://www.com1express.net/PODdetailsPage.html?waybillNum=%s' %  (trackingNo),
		'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'Accept': '*/*'
	}
	try:
		request = urllib.request.Request(url, headers=headers, data=data)
		response = urllib.request.urlopen(request)
	except Exception as e:
		print(e.read().decode('utf-8'))

	return json.loads(response.read().decode('utf-8'))

trackingNo = sys.argv[1]
if re.search('([^0-9])', trackingNo):
	print("参数{%s}有误，请重新输入运单号" % trackingNo)
else:
	print(getTrackingInfo(trackingNo))
