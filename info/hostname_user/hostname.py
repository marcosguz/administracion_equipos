import socket


def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except Exception as e:
        return "Nombre de host no disponible"
