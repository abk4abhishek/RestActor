
from pprint import pprint

from modules.M_Base import *
from data.DataConnector import *

# Making objects of Verify Modules and Data inteface
D=DI()
#D.setupData()   # It should be executed once after startup Docker.
Verifi=Base(D)


Verifi.setUser('dmvauth')
Verifi.Auth.getToken()
Verifi.DMV_Facilities.getAllFacilities()
Verifi.Facilities.getAFacility()