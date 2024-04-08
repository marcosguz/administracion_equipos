import wmi


def get_os_info(ip):
    try:
        conn = wmi.WMI(computer=ip)
        os_info = conn.Win32_OperatingSystem()
        if os_info:
            return os_info[0].Caption
    except wmi.x_wmi as e:
        print(f"No se pudo obtener la información del sistema operativo")
    return "Información del sistema operativo no disponible"
