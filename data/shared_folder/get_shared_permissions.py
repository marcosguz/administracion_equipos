from info.permissions import shared_permissions


def shared_permissions_folders(ips):
    permissions = shared_permissions.get_permissions(ips)
    return shared_permissions.imprimir_permisos_compartidos(permissions)
