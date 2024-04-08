from tabulate import tabulate
from info.process_data import get_process_data


def get_info_system(ips):
    data = get_process_data.get_data_os(ips)
    if data:
        processed_data = []
        for entry in data:
            combined_entry = entry[:5]  # Tomar los primeros 5 elementos que son IP, Hostname, SO, Usuario y Modelo
            antivirus_info = entry[5:]  # Tomar la información del antivirus
            combined_entry.extend(antivirus_info)  # Extender la lista combinada con la información del antivirus
            processed_data.append(combined_entry)  # Agregar la entrada procesada a la lista de datos procesados

        print(tabulate(processed_data,
                       headers=["IP", "Hostname", "Sistema Operativo", "Usuario de Red", "Modelo", "Antivirus",
                                "Version"], tablefmt="grid"))
    else:
        print("No se encontraron datos.")


