import dns.resolver
from modules.config import divide
from modules.recording import RecordLog 

def checkDNS(domain:str, type_record:str):
    """Проверяем записи"""
    status_dns, err = checkRecords(domain=domain, type_record=type_record)
    if err == None:
        status_dns.sort()
        for record in status_dns:
            print(f"{record}")
        print(f"{divide}\n")
        

    else:
        print(f"Domain:\t{err[1]}\n{err[0]}")
        RecordLog(err=err, type_record=type_record)

def checkRecords(domain:str, type_record:str):
    records = []
    err = None
    try:
        for x in dns.resolver.resolve(domain, type_record):
            records.append(x.to_text())
    except Exception as dns_error:
        records = None
        err = [dns_error, domain]
    return records, err


