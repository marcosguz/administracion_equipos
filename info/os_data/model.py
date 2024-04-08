import wmi


def get_model(ip_address):
    try:
        conn = wmi.WMI(computer=ip_address)
        cs = conn.Win32_ComputerSystem()
        if cs:
            return cs[0].Model
    except wmi.x_wmi as e:
        print(f"No se pudo obtener el modelo de la máquina remota.")
    return "Modelo no disponible"
