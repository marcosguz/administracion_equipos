from info.hostname_user import hostname
from info.network import network_user
from info.antivirus import antivirus_info
from info.os_data import os_info, model


def process_data(ip):
    host = hostname.get_hostname(ip)
    user = network_user.get_network_user(ip)
    antivirus = antivirus_info.get_antivirus_info(ip)
    os_data = os_info.get_os_info(ip)
    model_pc = model.get_model(ip)

    data = [ip, host, os_data, user, model_pc]

    if antivirus:
        for name, version in antivirus:
            data.extend([name, version])
    else:
        data.extend(["N/A", "N/A"])

    return data


def get_data_os(ips):
    try:
        results = []
        for ip in ips:
            data = process_data(ip)
            results.append(data)
        return results
    except Exception as e:
        print("Ocurrio un error.")