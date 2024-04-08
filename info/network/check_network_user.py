import wmi


def check_network_user_in_users_groups(network_user, hostname):
    try:
        conn = wmi.WMI(computer=hostname, privileges=["Security"])

        # Verificar si el usuario está en la carpeta Usuarios
        for user in conn.Win32_UserAccount(LocalAccount=True):
            if user.Name.lower() == network_user.lower():
                return "SI"

        # Verificar si el usuario está en el grupo Administradores
        administrators_group = conn.Win32_Group(Name='Administradores')
        for user in administrators_group[0].associators(wmi_result_class="Win32_UserAccount"):
            if user.Name.lower() == network_user.lower():
                return "SI"

        return "NO"
    except Exception as e:
        print(f"No se pudo verificar el usuario de red en '{hostname}': {e}")
        return "NO"
