import sys
from SinEmail.helper import helper
from SinEmail.checker import checkDNS
from SinEmail.call_base import Calling

#######################################
#       Основная функция чекера       #
#######################################
def SinEmail():
    try:
        argement = Arguments()
        if argement != None:
            mode = argement[-1]
            if None not in argement and mode == "Domain":
                domain, type_record = argement[0], argement[1]
                print(domain, type_record)

                if '@' in domain:domain = domain.split('@')[1]
                checkDNS(domain=domain, type_record=type_record)
    
            elif mode == "Base":
                file_name = argement[0]
                if '.csv' in file_name:
                    Calling(base=file_name) 
                else:
                    print(helper())
            else:print(helper())
    except KeyboardInterrupt:
        print("\nExit...")


#######################################
# Прием аргументов командной строки  #
#######################################
def Arguments():
    params = sys.argv
    
    if len(params) == 4 and params[1] == '--domain':
        domain = params[2]
        type_record = params[3]
        mode = "Domain"
        return domain, type_record, mode

    if len(params) == 3 and params[1] == '--calling':
        file_name = params[2]
        mode = "Base"
        return file_name, mode 

    else:
        print(helper())
        return None 

SinEmail()
