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
            response = req.get(url,headers=header,allow_redirects=False,timeout=10)
            code = response.status_code
            
            if code == 200:
                body = re.findall(r'evil.com',response.text)
                if body:
                    print("Targe:{} is vulnerable Status:{} Location:{}".format(url,code,body))

            if (code == 301 or code == 302):
                for key,value in response.headers.items():
                    respHeader = re.findall(r'evil.com',value)
                    if respHeader:
#                        print(url,"to Location:",response.headers['Location'])
                        print("Targe:{} is vulnerable Status:{} Location:{}".format(url,code,response.headers['Location']))
            else:
                print(url,":",code)
#if (code == 301 or code == 302):
# for key,value in response.headers.items():
#					respHeader = re.findall(r'evil.com',value)
#                    print(respHeader)

#if code == 200

#				body = re.findall(r"evil.com",response.text)
#				if body:
#					print("vulnerable")


scan()
