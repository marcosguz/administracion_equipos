import wmi


def get_network_user(ip):
    try:
        conn = wmi.WMI(computer=ip)
        for cs in conn.Win32_ComputerSystem():
            return cs.UserName.split("\\")[-1]
    except Exception as e:
        return "Usuario de red no disponible"
