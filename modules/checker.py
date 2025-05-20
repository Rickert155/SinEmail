import dns.resolver

def checkDNS(domain:str):
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

def checkMX(domain:str):
    records = []
    err = None
    try:
        for x in dns.resolver.resolve(domain, 'MX'):
            records.append(x.to_text())
    except Exception as dns_error:
        records = None
        err = [dns_error, domain]
    return records, err


