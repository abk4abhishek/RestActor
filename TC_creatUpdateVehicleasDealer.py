
from pprint import pprint

from modules.M_Base import *
from data.DataConnector import *


class T_createUpdateVehicleasDealer:
    def __init__(self):
        self.DI=DI()
        # self.DI.setupData()
        self.Base=Base(self.DI.baseurl,'Auth', 'Facility','Vehicles','Facilities','FacilityRelationships')

    def info(self):
        ''' Printing Modules list currently added in Base Class '''
        self.Base.getModulesList()

    def setup_auth(self):
        ''' Setting up the initial Data by fetching information from DB directly'''
        res=self.Base.Auth.getToken(self.DI.headers, self.DI.payload)
        pprint(res.json())
        tempjson = res.json()
        self.DI.headers['Authorization'] = 'jwt ' + tempjson['token']
        return tempjson['token']

    def getAFacilityRelationships_saveit(self):
        ''' Getting all Facilities as DMV and saving its id in data json'''
        users=self.DI.getValue('users')
        whichfacility = self.DI.memo['factopick'] - 1
        self.DI.fac = self.DI.getValue('Facilities')[WhichFacility]
        self.DI.dmv_user_id=users[self.DI.memo['dmvuser']-1][str(self.DI.memo['dmvuser'])+'_user_id']
        res=self.Base.FacilityRelationships.getAFacilityRelationships(self.DI.headers,self.DI.f)
        tempjson=res.json()
        ListofFacilities=[]
        if tempjson['count']>0:
            for item in tempjson['results']:
                ListofFacilities.append(item['id'])
        self.DI.updateData('Facilities',ListofFacilities)
        pprint (res.json())
        return res.json()

    def getAFacility(self,whichfacility=0):
        '''Get a Facility'''
        whichfacility=self.DI.memo['factopick']-1
        ''' Getting a Facility's info by passing the id saved in data json facility list'''
        self.DI.fac=self.DI.getValue('Facilities')[whichfacility]
        res=self.Base.Facility.getAFacility(self.DI.headers,self.DI.fac)
        pprint (res.json())
        return res.json()

    def teardown(self):
        print ("End of Test")





Test=T_createUpdateVehicleasDealer()


