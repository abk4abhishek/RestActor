
from pprint import pprint

from modules.M_Base import *
from data.DataConnector import *


class T_getVehicles:
    def __init__(self):
        self.DI=DI()
        # self.DI.setupData()
        self.Base=Base(self.DI.baseurl,'Auth', 'Facility','Vehicles','Facilities')

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

    def getAFacility(self,WhichFacility=0):
        ''' Getting a Facility's info by passing the id saved in data json facility list'''
        whichfacility = self.DI.memo['factopick'] - 1
        self.DI.fac=self.DI.getValue('Facilities')[WhichFacility]
        res=self.Base.Facility.getAFacility(self.DI.headers,self.DI.fac)
        pprint (res.json())
        return res.json()

    def getAllVehiclesofAFacility(self):
        ''' Getting all Vehicles under a Facility '''
        res=self.Base.Vehicles.getAllVehicles(self.DI.headers,self.DI.fac)
        pprint (res.json())
        return res.json()

    def teardown(self):
        print ("End of Test")





Test=T_getVehicles()

Test.info()
Test.setup_auth()
Test.getAFacility()
Test.getAllVehiclesofAFacility()
Test.teardown()


