import socket
import psutil
import platform


def get_so_name():
    # função pra retorna o nome do sistema, Exemplo: windows
    return platform.system()


def get_cpu_usage():
    # Mede o uso da CPU com intervalo de 1 segundo
    return psutil.cpu_percent(interval=1)


def memory_total():
    # retorna o maximo de memoria ram em MB
    return int(psutil.virtual_memory().total / (1024 ** 2))


def memory_used():
    # retorna a memoria ram usada em MB. so fiz essa função pra calcular a free.
    return int(psutil.virtual_memory().used / (1024 ** 2))


def memory_free():
    # faz um calculo da memoria total com a usada para retorna a disponivel.
    return memory_total() - memory_used()


def get_memory_usage():
    return {
        "total_mb": memory_total(),
        "used_mb": memory_used(),
        "free_mb": memory_free(),
        "percent_used": psutil.virtual_memory().percent
    }


def get_disk_usage():
    # retorna o total, usado e disponivel do disco em MB.
    disk = psutil.disk_usage('/')
    return {
        "Total_MB": int(disk.total / (1024 ** 2)),
        "Usado_MB": int(disk.used / (1024 ** 2)),
        "Livre_MB": int(disk.free / (1024 ** 2)),
        "Percentual_usado": disk.percent
    }


def ip_address():
    # retorna o IP da maquina
    return socket.gethostbyname(socket.gethostname())


def get_system_info():
    return {
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "IP_address": ip_address()
    }


def collect_system_data():
    # Esse serviço consolidado está retornando todos os dados no formato de dicionário
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "system_info": get_system_info()
    }
