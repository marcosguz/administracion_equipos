import wmi


def get_antivirus_info(ip):
    antivirus_info = []

    # Conexión WMI a la máquina remota
    try:
        conn = wmi.WMI(computer=ip)
        # Consulta para obtener la información sobre los programas instalados
        query = "SELECT * FROM Win32_Product"
        for program in conn.query(query):
            if program.Name and (
                    "Trend Micro Deep Security Agent" in program.Name or "Symantec Endpoint Protection" in program.Name):
                antivirus_info.append([program.Name, program.Version])
    except wmi.x_wmi as e:
        print(f"No se pudo obtener información del antivirus para la dirección IP '{ip}': {e}")
    return antivirus_info
