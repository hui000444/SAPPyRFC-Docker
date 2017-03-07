from pyrfc import Connection
from pprint import PrettyPrinter
conn = Connection(user='USER_RFC', passwd='password', ashost='sap.com', sysnr='15', client='700')

function_name = 'Z_ECATT_DEVOPS_AUTO_EXTRACT'
imp = dict(
    START_LNR='000001', 
    OBJ_LNR='000001', 
    OBJ_VER='00000001', 
    OBJ_TYPE=u'ECSC', 
    OBJ_NAME=u'ZCRM_AO_PROCESS', 
)

result = conn.call(function_name, TO_EXECUTE=[imp])

#INPUT:
#TO_EXECUTE
#START_LNR 000001 NUMC 6
#OBJ_LNR 000001 NUMC 6
#OBJ_TYPE 'ECSC' CHAR 4
#OBJ_NAME 'ZCRM_AO_PROCESS' CHAR 30
#OBJ_VER 00000001 NUMC 8

#OUTPUT:
#lt_execute
#lv_status CHAR 120 


#print result
pp = PrettyPrinter(indent=4)
pp.pprint(result)
print "ERR_MSG: ", result["EXECUTED"][0]["ERR_MSG"]
print "EV_STATUS: ", result["EV_STATUS"]
print "LOGID: ", result["LOGID"]["LOGID"]

