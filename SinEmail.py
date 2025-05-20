import sys
from modules.checker import checkDNS

#######################################
#       Основная функция чекера       #
#######################################
def SinEmail():
    argement = Arguments()
    if argement != None:domain = argement
    else:domain = str(input("Domain: "))

    if '@' in domain:domain = domain.split('@')[1]
    checkDNS(domain=domain)



#######################################
# Прием аргументов командной строки  #
#######################################
def Arguments():
    params = sys.argv
    if len(params) == 3 and params[1] == '--domain':
        return params[2]
    else:
        return None 

SinEmail()
