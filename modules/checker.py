import dns.resolver
from modules.recording import Log

def checkDNS(domain:str, type_record:str):
    """Проверям MX"""
    status_dns, err = checkRecords(domain=domain, type_record=type_record)
    if err == None:
        status_dns.sort()
        number_mx = 0
        for record in status_dns:
            number_mx+=1
            print(f"[{number_mx}] {record}")

    else:
        print(f"Domain:\t{err[1]}\n{err[0]}")
        Log(err=err, type_record=type_record)

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


