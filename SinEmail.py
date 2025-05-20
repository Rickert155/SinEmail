import sys
from modules.checker import checkDNS

#######################################
#       Основная функция чекера       #
#######################################
def SinEmail():
    argement = Arguments()
    if argement != None:
        domain, type_record = argement
        print(domain, type_record)

        if '@' in domain:domain = domain.split('@')[1]
        checkDNS(domain=domain, type_record=type_record)

    else:print("help")


#######################################
# Прием аргументов командной строки  #
#######################################
def Arguments():
    params = sys.argv
    if len(params) == 4 and params[1] == '--domain':
        domain = params[2]
        type_record = params[3]
        return domain, type_record
    else:
        return None 

SinEmail()
