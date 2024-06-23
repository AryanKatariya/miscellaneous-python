import requests as req
import argparse as ap,re

parser = ap.ArgumentParser(usage="python3 hostInjection.py <-t|--target> <URLs as file> ",description="Host Header Detection")
parser.add_argument("-t","--target",dest="target",help="Provide target URLs as file",required=True)
arg = parser.parse_args()
def scan():
	with open(arg.target,"r") as f:
		for i in f.readlines():
			url = i.strip("\r\n")
			header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.','Host':'evil.com'}
			response = req.get(url,headers=header,allow_redirects=False)
			print(url,":",response.status_code)
			code = response.status_code
			
#			if code == 200:
#				body = re.findall(r"evil.com",response.text)
#				if body:
#					print("vulnerable")
				
			if code == 301 or code == 302:
				print(url)
				for key,value in response.headers.items():
					respHeader = re.findall(r'evil.com',value)
					if respHeader:
						print()	


scan()
