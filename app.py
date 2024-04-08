
from file import file_path
from data.roles import get_info_roles
from data.shared_folder import get_shared_permissions
from data.summary import get_info_system
#
#
#
# class App:
#     def __init__(self):
#         self.ip_file = None
#         self.headers = {
#             '1': ["Usuario de Red", "IP", "Hostname", "Usuario", "Estado", "Grupo", "Administrador"],
#             '2': ["IP", "Hostname", "Sistema Operativo", "Usuario de Red", "Modelo", "Antivirus", "Version"],
#             '3': ["Recurso Compartido", "Everyone", "Full Control", "IP", "Hostname"]
#         }
#
#     def get_ip_file_path(self):
#         while True:
#             self.ip_file = input("Ingresa la ruta del archivo que contiene las direcciones IP: ").strip()
#             if not self.ip_file:
#                 print("Por favor, ingresa una ruta válida.")
#             else:
#                 ips = file_path.read_ip_from_file(self.ip_file)
#                 print("IPS CARGADAS")
#                 return ips
#
#     def display_menu(self, options):
#         max_length = max(len(option) for option in options)
#         header = "+" + "=" * (max_length + 9) + "+"
#         print(header)
#         print("|{: ^{width}}|".format("MENU DE OPCIONES:", width=max_length + 9))
#         print("|" + " " * (max_length + 9) + "|")
#         for i, option in enumerate(options, start=1):
#             print("|   {}. {:<{width}}   |".format(i, option, width=max_length))
#         print(header)
#
#     def handle_option(self, option, ips):
#         if option in ['1', '2', '3']:
#             data = self.collect_data(option, ips)
#             if data:
#                 self.write_to_excel(data, option)
#                 print("Datos guardados en el archivo Excel.")
#             else:
#                 print("No se encontraron datos para la opción seleccionada.")
#         elif option == '4':
#             print("Saliendo del programa...")
#             exit()
#         else:
#             print("Opción no válida. Por favor, seleccione una opción del menú.")
#
#     def collect_data(self, option, ips):
#         if option == '1':
#             return get_info_roles.roles(ips) or []
#         elif option == '2':
#             return get_info_system.get_info_system(ips) or []
#         elif option == '3':
#             result_dict = shared_permissions.get_permissions(ips)
#             data = []
#             for ip, permissions in result_dict.items():
#                 for permission in permissions:
#                     row = list(permission.values())
#                     row.extend([ip, ips[ip]])
#                     data.append(row)
#             return data
#         else:
#             return []
#
#     def write_to_excel(self, data, option):
#         wb = openpyxl.Workbook()
#         ws = wb.active
#
#         # Escribir el encabezado
#         headers = self.headers[option]
#         ws.append(headers)
#
#         # Escribir los datos
#         for row in data:
#             ws.append(row)
#
#         # Ajustar el ancho de las columnas
#         for col in ws.columns:
#             max_length = 0
#             column = col[0].column_letter  # Obtener la letra de la columna
#             for cell in col:
#                 try:
#                     if len(str(cell.value)) > max_length:
#                         max_length = len(cell.value)
#                 except:
#                     pass
#             adjusted_width = (max_length + 2) * 1.2
#             ws.column_dimensions[column].width = adjusted_width
#
#         # Guardar el archivo Excel
#         wb.save(f"data_{option}.xlsx")
#
# if __name__ == "__main__":
#     app = App()
#     ips = app.get_ip_file_path()
#     menu_options = [
#         "Obtener Roles de usuario",
#         "Obtener Información del PC",
#         "Obtener Información de Carpetas compartidas",
#         "Salir"
#     ]
#     while True:
#         app.display_menu(menu_options)
#         option = input("\nIngresa una opción del menú: ").strip()
#         app.handle_option(option, ips)


# class App:
#     def __init__(self):
#         self.ip_file = None
#         self.headers = {
#             '1': ["Usuario de Red", "IP", "Hostname", "Usuario", "Estado", "Grupo", "Administrador"],
#             '2': ["IP", "Hostname", "Sistema Operativo", "Usuario de Red", "Modelo", "Antivirus", "Version"],
#             '3': ["Recurso Compartido", "Everyone", "Full Control", "IP", "Hostname"]
#         }
#
#     def get_ip_file_path(self):
#         while True:
#             self.ip_file = input("Ingresa la ruta del archivo que contiene las direcciones IP: ").strip()
#             if not self.ip_file:
#                 print("Por favor, ingresa una ruta válida.")
#             else:
#                 ips = file_path.read_ip_from_file(self.ip_file)
#                 #print("IPS CARGADAS")
#                 return ips
#
#     def display_menu(self, options):
#         max_length = max(len(option) for option in options)
#         header = "+" + "=" * (max_length + 9) + "+"
#         print(header)
#         print("|{: ^{width}}|".format("MENU DE OPCIONES:", width=max_length + 9))
#         print("|" + " " * (max_length + 9) + "|")
#         for i, option in enumerate(options, start=1):
#             print("|   {}. {:<{width}}   |".format(i, option, width=max_length))
#         print(header)
#
#     def handle_option(self, option, ips):
#         if option in ['1', '2', '3']:
#             data = self.collect_data(option, ips)
#             if data:
#                 self.write_to_excel(data, option)
#                 print("Datos guardados en el archivo Excel.")
#             else:
#                 print("No se encontraron datos para la opción seleccionada.")
#         elif option == '4':
#             print("Saliendo del programa...")
#             exit()
#         else:
#             print("Opción no válida. Por favor, seleccione una opción del menú.")
#
#     def collect_data(self, option, ips):
#         if option == '1':
#             return get_info_roles.roles(ips) or []
#         elif option == '2':
#             return get_info_system.get_info_system(ips) or []
#         elif option == '3':
#             data = get_shared_permissions.shared_permissions_folders(ips) or []
#             print(data)
#             # Agregar IP y Hostname a cada fila de datos
#             for row in data:
#                 row.append(row[0])  # IP
#                 row.append(row[1])  # Hostname
#             return data
#         else:
#             return []
#
#     def write_to_excel(self, data, option):
#         wb = openpyxl.Workbook()
#         ws = wb.active
#
#         # Escribir el encabezado
#         headers = self.headers[option]
#         ws.append(headers)
#
#         # Ajustar el ancho de las columnas antes de escribir los datos
#         for col in ws.columns:
#             max_length = 0
#             column = col[0].column_letter  # Obtener la letra de la columna
#             for cell in col:
#                 try:
#                     if len(str(cell.value)) > max_length:
#                         max_length = len(cell.value)
#                 except:
#                     pass
#             adjusted_width = (max_length + 2) * 1.2
#             ws.column_dimensions[column].width = adjusted_width
#
#         # Escribir los datos después de ajustar el ancho de las columnas
#         for row in data:
#             ws.append(row)
#
#         # Guardar el archivo Excel
#         wb.save(f"data_{option}.xlsx")
#
# if __name__ == "__main__":
#     app = App()
#     ips = app.get_ip_file_path()
#     menu_options = [
#         "Obtener Roles de usuario",
#         "Obtener Información del PC",
#         "Obtener Información de Carpetas compartidas",
#         "Salir"
#     ]
#     while True:
#         app.display_menu(menu_options)
#         option = input("\nIngresa una opción del menú: ").strip()
#         app.handle_option(option, ips)





# from tabulate import tabulate
# import openpyxl
# from openpyxl.styles import Alignment
# from file import file_path
# from data.roles import get_info_roles
# from data.shared_folder import get_shared_permissions
# from data.summary import get_info_system
#
#
# class App:
#     def __init__(self):
#         self.ip_file = None
#         self.headers = {
#             '1': ["Usuario de Red", "IP", "Hostname", "Usuario", "Estado", "Grupo", "Administrador"],
#             '2': ["IP", "Hostname", "Sistema Operativo", "Usuario de Red", "Modelo", "Antivirus", "Version"],
#             '3': ["Recurso Compartido", "Everyone", "Full Control", "IP", "Hostname"]
#         }
#
#     def get_ip_file_path(self):
#         while True:
#             self.ip_file = input("Ingresa la ruta del archivo que contiene las direcciones IP: ").strip()
#             if not self.ip_file:
#                 print("Por favor, ingresa una ruta válida.")
#             else:
#                 ips = file_path.read_ip_from_file(self.ip_file)
#                 print("IPS CARGADAS")
#                 return ips
#
#     def display_menu(self, options):
#         max_length = max(len(option) for option in options)
#         header = "+" + "=" * (max_length + 9) + "+"
#         print(header)
#         print("|{: ^{width}}|".format("MENU DE OPCIONES:", width=max_length + 9))
#         print("|" + " " * (max_length + 9) + "|")
#         for i, option in enumerate(options, start=1):
#             print("|   {}. {:<{width}}   |".format(i, option, width=max_length))
#         print(header)
#
#     def handle_option(self, option, ips):
#         if option in ['1', '2', '3']:
#             data = self.collect_data(option, ips)
#             if data:
#                 self.write_to_excel(data, option)
#                 print("Datos guardados en el archivo Excel.")
#             else:
#                 print("No se encontraron datos para la opción seleccionada.")
#         elif option == '4':
#             print("Saliendo del programa...")
#             exit()
#         else:
#             print("Opción no válida. Por favor, seleccione una opción del menú.")
#
#     def collect_data(self, option, ips):
#         if option == '1':
#             return get_info_roles.roles(ips) or []
#         elif option == '2':
#             return get_info_system.get_info_system(ips) or []
#         elif option == '3':
#             data = get_shared_permissions.shared_permissions_folders(ips) or []
#             # Agregar IP y Hostname a cada fila de datos
#             for row in data:
#                 row.append(row[0])  # IP
#                 row.append(row[1])  # Hostname
#             return data
#         else:
#             return []
#
#     def write_to_excel(self, data, option):
#         wb = openpyxl.Workbook()
#         ws = wb.active
#
#         # Escribir el encabezado
#         headers = self.headers[option]
#         ws.append(headers)
#
#         # Escribir los datos
#         for row in data:
#             ws.append(row)
#
#         # Ajustar el ancho de las columnas
#         for col in ws.columns:
#             max_length = 0
#             column = col[0].column_letter  # Obtener la letra de la columna
#             for cell in col:
#                 try:
#                     if len(str(cell.value)) > max_length:
#                         max_length = len(cell.value)
#                 except:
#                     pass
#             adjusted_width = (max_length + 2) * 1.2
#             ws.column_dimensions[column].width = adjusted_width
#
#         # Guardar el archivo Excel
#         wb.save(f"data_{option}.xlsx")
#
# if __name__ == "__main__":
#     app = App()
#     ips = app.get_ip_file_path()
#     menu_options = [
#         "Obtener Roles de usuario",
#         "Obtener Información del PC",
#         "Obtener Información de Carpetas compartidas",
#         "Salir"
#     ]
#     while True:
#         app.display_menu(menu_options)
#         option = input("\nIngresa una opción del menú: ").strip()
#         app.handle_option(option, ips)


# class App:
#     def __init__(self):
#         self.ip_file = None
#         self.headers = {
#             '1': ["Usuario de Red", "IP", "Hostname", "Usuario", "Estado", "Grupo", "Administrador"],
#             '2': ["IP", "Hostname", "Sistema Operativo", "Usuario de Red", "Modelo", "Antivirus", "Version"],
#             '3': ["Recurso Compartido", "Everyone", "Full Control"]
#         }
#
#     def get_ip_file_path(self):
#         while True:
#             self.ip_file = input("Ingresa la ruta del archivo que contiene las direcciones IP: ").strip()
#             if not self.ip_file:
#                 print("Por favor, ingresa una ruta válida.")
#             else:
#                 ips = file_path.read_ip_from_file(self.ip_file)
#                 print("IPS CARGADAS")
#                 return ips
#
#     def display_menu(self, options):
#         max_length = max(len(option) for option in options)
#         header = "+" + "=" * (max_length + 9) + "+"
#         print(header)
#         print("|{: ^{width}}|".format("MENU DE OPCIONES:", width=max_length + 9))
#         print("|" + " " * (max_length + 9) + "|")
#         for i, option in enumerate(options, start=1):
#             print("|   {}. {:<{width}}   |".format(i, option, width=max_length))
#         print(header)
#
#     def handle_option(self, option, ips):
#         if option in ['1', '2', '3']:
#             data = self.collect_data(option, ips)
#             self.write_to_excel(data, option)
#             print("Datos guardados en el archivo Excel.")
#         elif option == '4':
#             print("Saliendo del programa...")
#             exit()
#         else:
#             print("Opción no válida. Por favor, seleccione una opción del menú.")
#
#     def collect_data(self, option, ips):
#         if option == '1':
#             return get_info_roles.roles(ips) or []
#         elif option == '2':
#             return get_info_system.get_info_system(ips) or []
#         elif option == '3':
#             return get_shared_permissions.shared_permissions_folders(ips) or []
#         else:
#             return []
#
#     def write_to_excel(self, data, option):
#         wb = openpyxl.Workbook()
#         ws = wb.active
#
#         # Escribir el encabezado
#         ws.append(self.headers[option])
#
#         # Escribir los datos
#         for row in data:
#             ws.append(row)
#
#         # Ajustar el ancho de las columnas
#         for col in ws.columns:
#             max_length = 0
#             column = col[0].column_letter  # Obtener la letra de la columna
#             for cell in col:
#                 try:
#                     if len(str(cell.value)) > max_length:
#                         max_length = len(cell.value)
#                 except:
#                     pass
#             adjusted_width = (max_length + 2) * 1.2
#             ws.column_dimensions[column].width = adjusted_width
#
#         # Guardar el archivo Excel
#         wb.save(f"data_{option}.xlsx")
#
# if __name__ == "__main__":
#     app = App()
#     ips = app.get_ip_file_path()
#     menu_options = [
#         "Obtener Roles de usuario",
#         "Obtener Información del PC",
#         "Obtener Información de Carpetas compartidas",
#         "Salir"
#     ]
#     while True:
#         app.display_menu(menu_options)
#         option = input("\nIngresa una opción del menú: ").strip()
#         app.handle_option(option, ips)





class App:
    def __init__(self):
        self.ip_file = None

    def get_ip_file_path(self):
        while True:
            self.ip_file = file_path.get_file_path()
            if not self.ip_file:
                print("Por favor, ingresa una ruta válida.")
                self.get_ip_file_path()
            else:
                ips = file_path.read_ip_from_file(self.ip_file)
                # print("IPS CARGADAS")
                # print(tabulate([[ip] for ip in ips], headers=["IPS"], tablefmt="grid"))
                return ips

    def display_menu(self, options):
        max_length = max(len(option) for option in options)
        header = "+" + "=" * (max_length + 9) + "+"
        print(header)
        print("|{: ^{width}}|".format("MENU DE OPCIONES:", width=max_length + 9))
        print("|" + " " * (max_length + 9) + "|")
        for i, option in enumerate(options, start=1):
            print("|   {}. {:<{width}}   |".format(i, option, width=max_length))
        print(header)

    def handle_option(self, option, ips):
        if option == '1':
            get_info_roles.roles(ips)
        elif option == '2':
            get_info_system.get_info_system(ips)
        elif option == '3':C:\Users\MEGN6248\OneDrive - BGR\Documentos\megn6248\Seguridad\python\Automatizacion
            get_shared_permissions.shared_permissions_folders(ips)
        elif option == '4':
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")


if __name__ == "__main__":
    app = App()
    ips = app.get_ip_file_path()
    menu_options = [
        "Obtener Roles de usuario",
        "Obtener Información del PC",
        "Obtener Información de Carpetas compartidas",
        "Salir"
    ]
    while True:
        app.display_menu(menu_options)
        option = input("\nIngresa una opción del menú: ").strip()
        app.handle_option(option, ips)

# class App:
#     def __init__(self):
#         self.ip_file = None
#
#     def get_ip_file_path(self):
#         while True:
#             self.ip_file = file_path.get_file_path()
#             if not self.ip_file:
#                 print("Por favor, ingresa una ruta válida.")
#             else:
#                 ips = file_path.read_ip_from_file(self.ip_file)
#                 print("IPS CARGADAS")
#                 print(tabulate([[ip] for ip in ips], headers=["IPS"], tablefmt="grid"))
#                 return ips
#
#     def display_menu(self):
#         print("+===========================================================+")
#         print("|	SELECCIONE UNA OPCION:                                 |")
#         print("|                                                           |")
#         print("|	1. Obtener Roles de usuario                            |")
#         print("|	2. Obtener Información del PC                          |")
#         print("|	3. Obtener Información de Carpetas compartidas         |")
#         print("|	4. Salir                                               |")
#         print("+===========================================================+")
#
#     def handle_option(self, option, ips):
#         if option == '1':
#             get_info_roles.roles(ips)
#         elif option == '2':
#             get_info_system.get_info_system(ips)
#         elif option == '3':
#             print(ips)
#             get_shared_permissions.shared_permissions_folders(ips)
#         elif option == '4':
#             print("Saliendo del programa...")
#             exit()
#         else:
#             print("Opción no válida. Por favor, seleccione una opción del menú.")
#
#
# if __name__ == "__main__":
#     app = App()
#     ips = app.get_ip_file_path()
#     while True:
#         app.display_menu()
#         option = input("\nSeleccione una opción: ").strip()
#         app.handle_option(option, ips)
