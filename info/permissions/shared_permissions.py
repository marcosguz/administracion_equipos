import wmi
from tabulate import tabulate
from info.hostname_user import hostname


def get_permissions(ip_list):
    result_dict = {}
    for ip in ip_list:
        name_host = hostname.get_hostname(ip)
        if name_host:
            try:
                shares = wmi.WMI(computer=name_host).Win32_Share()
                if shares:
                    data = []
                    for share in shares:
                        if not share.Name.endswith('$'):
                            share_name = share.Name
                            try:
                                share_security = \
                                    wmi.WMI(computer=name_host).Win32_LogicalShareSecuritySetting(Name=share.Name)[0]
                                security_descriptor = share_security.GetSecurityDescriptor()
                                descriptor = security_descriptor[0]
                                acl = descriptor.DACL
                                everyone_full_control = "NO"
                                for ace in acl:
                                    trustee = ace.Trustee
                                    if trustee.Name == "Everyone" or trustee.Name == "Todos":
                                        if ace.AccessMask == 2032127:  # Full Control
                                            everyone_full_control = "SI"
                                        break
                                data.append([share_name, "SI" if everyone_full_control == "SI" else "NO",
                                             "SI" if everyone_full_control == "SI" else "NO"])
                            except Exception as e:
                                print(
                                    f"No se pudieron obtener los permisos para el recurso compartido {share_name} en {name_host}: {str(e)}")
                    result_dict[ip] = data
                else:
                    print(f"No se encontraron recursos compartidos en {name_host}.")
            except Exception as e:
                print(f"No se pudo obtener la información sobre las carpetas compartidas en {name_host}")
        else:
            print(f"No se pudo resolver el hostname para la dirección IP {ip}")
    return result_dict


def imprimir_permisos_compartidos(result_dict):
    for ip, data in result_dict.items():
        print(f"Permisos de recursos compartidos en {ip}:")
        if data:
            print(tabulate(data, headers=["Recurso Compartido", "Everyone", "Full Control"], tablefmt="grid"))
        else:
            print("No se encontraron recursos compartidos.")