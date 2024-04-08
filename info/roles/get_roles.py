import wmi
from tqdm import tqdm
import time


def get_user_roles(hostname):
    try:
        conn = wmi.WMI(computer=hostname, privileges=["Security"])

        # Obtener roles de usuarios
        users_roles = {}
        groups = set()  # Conjunto para almacenar los nombres de grupos únicos

        # Obtener usuarios de la carpeta Usuarios de Usuarios y grupos locales
        for user in tqdm(conn.Win32_UserAccount(LocalAccount=True), desc="Recopilando datos de usuarios", leave=False):
            username = user.Name
            user_status = "Habilitado" if user.Disabled == False else "Deshabilitado"  # Estado del usuario
            user_roles = []
            for group in user.associators(wmi_result_class="Win32_GroupUser"):
                user_roles.append(group.Name)
                groups.add(group.Name)  # Agregar el nombre del grupo al conjunto de grupos
            if not user_roles:
                user_roles.append("Grupo Local")  # Si el usuario no tiene grupo, ponle "Grupo Local"
            users_roles[username] = {'roles': user_roles, 'status': user_status}
            time.sleep(0.1)  # Simulamos una pequeña espera

        # Obtener usuarios del grupo Administradores
        administrators_group = conn.Win32_Group(Name='Administradores')
        for user in administrators_group[0].associators(wmi_result_class="Win32_UserAccount"):
            username = user.Name
            user_status = "Habilitado" if user.Disabled == False else "Deshabilitado"  # Estado del usuario
            user_roles = ['Administradores']
            users_roles[username] = {'roles': user_roles, 'status': user_status}

        return users_roles

    except Exception as e:
        return {}
