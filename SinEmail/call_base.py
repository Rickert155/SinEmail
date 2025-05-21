from SinEmail.checker import checkDNS
from SinEmail.colors import RED, GREEN, RESET, BLUE
import csv, os

types = ["MX", "TXT"]

#checkDNS(domain="google.com", type_record="MX")
def checkerFile(base):
    if os.path.exists(base):
        return True
    else:
        print("Такой базы нет!")
        return False

def Calling(base:str):
    checkFile = checkerFile(base=base)
    if checkFile:
        with open(base, 'r') as file:
            number_domain = 0
            for row in csv.DictReader(file):
                number_domain+=1
                try:email = row['Email']
                except:email = None
                try:company = row['Company']
                except:company = None
                try:name = row['Name']
                except:name = None
                
                domain = row['Domain']
                print(f"{RED}[{number_domain}]{RESET} {GREEN}{domain}{RESET}")

                for type_record in types:
                    print(f"{BLUE}Type: {type_record}{RESET}")
                    checkDNS(
                            domain=domain,
                            type_record=type_record,
                            email=email,
                            company=company,
                            name=name
                            )
    
     


