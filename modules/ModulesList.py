""" This Module file is containing following Module classes
1. Auth
2. Vehicles
"""
from pprint import pprint

class Auth:

    def __init__(self,UR,D):
        self.url="/api-token-auth/"
        self.UR=UR
        self.D=D
        self.DoList=['getToken']

    def getToken(self):
        print ("Getting a Tokken",end='')
        self.D.payload['email']=self.D.email
        res = self.UR.Send(self.url,'POST',json=self.D.payload,headers=self.D.headers)
        tempjson = res.json()
        self.D.headers['Authorization'] = 'jwt ' + tempjson['token']
        print ("\t - Done!")
        return res




class Facilities:

    def __init__(self,UR,D):
        self.url="/facilities/"
        self.UR=UR
        self.D=D
        self.DoList = ['getAFacility']

    def getAFacility(self):
        print("Getting a Facility",end='')
        Facs = self.D.getValue('Facilities')
        Fac=Facs[self.D.memo['factopick']]
        res = self.UR.Send(self.url+Fac+'/','GET',headers=self.D.headers)
        print("\t - Done!")
        return res


class DMV_Facilities:

    def __init__(self,UR,D):
        self.url="/dmv-users/{{user_id}}/facilities/"
        self.UR=UR
        self.D=D

    def getAllFacilities(self):
        print("Getting all Facilities and saving to Data json",end='')
        dynamic_url = self.url.replace('{{user_id}}', self.D.user_id)
        res = self.UR.Send(dynamic_url,'GET',headers=self.D.headers)
        tempjson=res.json()
        ListofFacilities=[]
        if tempjson['count']>0:
            for item in tempjson['results']:
                ListofFacilities.append(item['id'])
        self.D.updateData('Facilities',ListofFacilities)
        print("\t - Done!")
        return res


class Facility_Relationships:

    def __init__(self,UR,D):
        self.url="/facilities/{{facility}}/relationships/"
        self.UR=UR
        self.D=D


    def getAFacilityRelationships(self,facnumber):
        print ("Getting relationships of a Facility")
        dynamic_url = self.url.replace('{{facility}}', facnumber)
        res=self.UR.Send(dynamic_url,'GET',headers=self.D.headers)
        return res


class Facility_Vehicles:

    def __init__(self,UR,D):
        self.url="/facilities/{{facility}}/vehicles/"
        self.UR=UR
        self.D=D
        self.DoList = ['getAllVehicles']

    def getAllVehicles(self,headers,facnumber):
        print("Getting all Vehicles of a Facility")
        dynamic_url = self.url.replace('{{facility}}', facnumber)
        res = self.UR.Send(dynamic_url,'GET',headers=headers)
        return res

