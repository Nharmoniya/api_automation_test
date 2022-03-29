import requests
from login import Login

class Upload():
    def __init__(self, s=requests.session(), host="http://123.56.170.43:8888"):
        self.s = s
        self.host = host
        Login(self.s).login()

    def up(self):
        url = self.host+"/uploadmulti"
        file = {"uploadFiles":open("123.png","rb")}
        print(open("123.png"),"rb")
        res = self.s.post(url=url,files=file)
        print(res.text)


    def getAlbum(self):
        url = self.host+"/album/manage?filter=me"
        res = self.s.get(url=url)



if __name__ == '__main__':
    up = Upload()
    up.up()
    up.getAlbum()