import requests,random

url = "https://pastebin.com/raw/01yJu4gY"
h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
data = requests.get(url,headers=h,timeout=10)
url_list = data.text.split("\r\n")
#print(l)
for i in url_list:
    try:
        imagesData = requests.get(i,headers=h,timeout=10)
        num = str(random.randint(1,100))
        f = open("images"+num+".jpg","wb")
        f.write(imagesData.content)
        f.close()
    except:
        pass
