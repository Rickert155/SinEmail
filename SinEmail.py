import sys
from modules.checker import checkMX


#######################################
#       Основная функция чекера       #
#######################################
def SinEmail():
    argement = Arguments()
    if argement != None:domain = argement
    else:domain = str(input("Domain: "))

    """Проверям MX"""
    status_dns, err = checkMX(domain=domain)
    if err == None:
        status_dns.sort()
        number_mx = 0
        for record in status_dns:
            number_mx+=1
            print(f"[{number_mx}] {record}")

    else:
        print(f"Domain:\t{err[1]}\n{err[0]}")


#######################################
# Прием аргументов командной строки  #
#######################################
def Arguments():
    params = sys.argv
    if len(params) == 2 and '.' in params[1]:
        return params[1]
    else:
        return None 

SinEmail()
