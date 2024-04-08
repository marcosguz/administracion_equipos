import time
from tabulate import tabulate
import wmi

from info.roles import get_roles
from info.hostname_user import hostname
from info.network import network_user, check_network_user


def roles(ips):

    for ip_address in ips:
        # Obtener el nombre del host
        hostname_user = hostname.get_hostname(ip_address)

        try:
            # Intentar conectar con la IP
            conn = wmi.WMI(computer=ip_address)
        except Exception as e:
            print(f"\nNo se pudo conectar a la dirección IP '{ip_address}'")
            continue

        start_time = time.time()  # Captura el tiempo de inicio

        print(f"\nEstamos consultando la información requerida en: {hostname_user} ({ip_address})...")
        time.sleep(1)  # Simulamos una pequeña espera antes de comenzar la consulta

        # Obtener el usuario de red conectado en la PC remota
        user = network_user.get_network_user(ip_address)

        # Verificar si el usuario de red está en las carpetas Usuarios o Grupos
        network_user_in_users_groups = check_network_user.check_network_user_in_users_groups(user, hostname_user)

        # Obtener roles de todos los usuarios en el equipo remoto
        users_roles = get_roles.get_user_roles(hostname_user)

        end_time = time.time()  # Captura el tiempo de finalización
        elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido

        if users_roles:
            print(f"\nRoles para el host: {hostname_user} ({ip_address})\n")

            # Formatear usuarios
            users_data = []
            for username, data in users_roles.items():
                users_data.append(
                    [user, ip_address, hostname_user, username, data['status'], '\n'.join(data['roles']),
                     network_user_in_users_groups])

            print(f"DATOS DE ROLES -> {hostname_user}:")
            print(tabulate(users_data,
                           headers=["Usuario de Red", "IP", "Hostname", "Usuario", "Estado", "Grupo", "Administrador"],
                           tablefmt="grid"))

            print(f"\nTiempo de espera fue de: {elapsed_time:.2f} segundos")
        else:
            print(f"No se encontraron roles en el equipo remoto.")