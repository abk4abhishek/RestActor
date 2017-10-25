from sqlalchemy import create_engine
import json


class DI:

    def __init__(self):
        self.baseurl = "https://192.168.99.100:5000"
        self.headers={
            'content-type': "application/json",
            'Authorization':"blank"
            }
        self.email="dmvauthuser@test.com"
        self.user_id=""
        self.payload= {
            "email": "dmvauthuser@test.com",
            "password": "1234"
            }
        self.memo={
            'dmv':4,
            'dmvauth': 5,
            'test':0,
            'poc':1,
            'admin':2,
            'user':3,
            'factopick':1
        }


    def updateData(self,ObjName,NewObj):
        InitialSetup=[]
        with open('data\InitialData_01.json', 'r') as fp:
            InitialSetup=json.load(fp)
        InitialSetup[0][ObjName]=NewObj
        with open('data\InitialData_01.json', 'w') as fp:
            json.dump(InitialSetup, fp)

    def getValue(self,ObjName):
        with open('data\InitialData_01.json', 'r') as fp:
            InitialSetup=json.load(fp)
        return InitialSetup[0][ObjName]

    def setupData(self):
        connection_string='postgresql://postgres:@192.168.99.100:5432/postgres'
        engine = create_engine(connection_string)
        InitialSetup=[]
        users=[]
        facility_roles=[]
        dmv_roles=[]
        dealers=[]
        veh_make=[]
        veh_bodytype=[]


        connection = engine.connect()

        result = connection.execute("SELECT * FROM accounts_user")
        i=1
        for row in result:
            id1=str(row["id"])
            users.append({str(i)+"_user":row["email"],str(i)+"_user_id":id1})
            i+=1

        result = connection.execute("SELECT * FROM dealers_facilityrole")


        for row in result:
            id1=str(row["id"])
            facility_roles.append({"role_name":row["name"],"role_id":id1})


        result = connection.execute("SELECT * FROM dmv_dmvrole")
        for row in result:
            id1=str(row["id"])
            dmv_roles.append({"dmv_role_name":row["name"],"dmv_role_id":id1})

        result = connection.execute("SELECT * FROM dealers_dealer")
        for row in result:
            id1=str(row["id"])
            dealers.append({"dealer_name":row["name"],"dealer_id":id1})

        result = connection.execute("SELECT * FROM vehicles_make")
        ii=0
        for row in result:
            id1=str(row["id"])
            veh_make.append({"make_name":row["name"],"make_id":id1})
            if ii>=10:
                break
            ii+=1


        ii=0
        result = connection.execute("SELECT * FROM vehicles_bodytype")
        for row in result:
            id1=str(row["id"])
            veh_bodytype.append({"bodytype_name":row["name"],"bodytype_id":id1,"bodytype_code":row["code"]})
            if ii>=10:
                break
            ii+=1

        InitialSetup = [{ "users" : users, "fac_roles" : facility_roles,"dmv_roles":dmv_roles,"dealers":dealers, "veh_make":veh_make,"veh_bodytype":veh_bodytype}]

        connection.close()
        with open('data\InitialData_01.json', 'w') as fp:
            json.dump(InitialSetup, fp)
