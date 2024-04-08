def read_ip_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            ip_address = [line.strip() for line in file.readlines()]
        return ip_address
    except Exception as e:
        print(f"No se pudo leer el archivo {file_path}")
        return []


def get_file_path():
    path = input("Ingresa la ruta relativa del archivo: ")
    return path
