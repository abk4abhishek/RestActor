from pprint import pprint

from Utils.U_Requests import *
from modules.ModulesList import *


class Base:

    # def __init__(self,baseurl,*args):
    #     self.UR=UR(baseurl)
    #     if 'Auth' in args:
    #         self.Auth=Auth(self.UR)
    #     if 'Vehicles' in args:
    #         self.Vehicles=Vehicles(self.UR)
    #     if 'Facility' in args:
    #         self.Facility=Facility(self.UR)
    #     if 'Facilities' in args:
    #         self.Facilities=Facilities(self.UR)
    #     if 'FacilityRelationships' in args:
    #         self.FacilityRelationships=FacilityRelationships(self.UR)
    #
    #     self.MList=['Auth','Facility','Vehicles','Facilities','FacilityRelationships']
    #     self.URLs = {}

    def __init__(self,D):
        self.D=D
        self.UR=UR(D.baseurl)
        self.Auth=Auth(self.UR,self.D)
        self.Facilities=Facilities(self.UR,self.D)
        self.Facility_Vehicles = Facility_Vehicles(self.UR, self.D)
        self.DMV_Facilities=DMV_Facilities(self.UR,self.D)
        self.Facility_Relationships=Facility_Relationships(self.UR,self.D)

        self.MList=['Auth','Facilities','Facility_Vehicles','DMV_Facilities','Facility_Relationships']
        self.URLs = {}

    def getModulesList(self):
        for item in self.MList:
            print (item)
            M=getattr(self,item)
            self.URLs[item]=M.url

        print ("="*50)
        print ("    List of implemented Modules and URLs    ")
        pprint (self.URLs)
        print ("=" * 50)

    def setUser(self,user):
        print ("Setting a user : " + user , end='')
        users=self.D.getValue('users')
        gotuser=users[self.D.memo[user]][str(self.D.memo[user]+1)+'_user']
        gotuser_id=users[self.D.memo[user]][str(self.D.memo[user]+1)+'_user_id']
        self.D.user_id=gotuser_id
        self.D.email=gotuser
        print("\t - Done!")


    def T_StatusCode(self,res,expectedSCode):
        return self.UR.V_StatusCode(res,expectedSCode)


