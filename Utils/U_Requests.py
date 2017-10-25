import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class UR:

    def __init__(self,baseurl):
        self.baseurl = baseurl
        self.certVerify=False

    def Send(self,url,method,**kwargs):

        kwargs['method']=method
        kwargs['url']=self.baseurl+url
        kwargs['verify']=self.certVerify
        res = requests.request(**kwargs)
        return res

    def V_StatusCode(self,res,expectedSCode):
        if res.status_code==expectedSCode:
            return True
        else:
            return False