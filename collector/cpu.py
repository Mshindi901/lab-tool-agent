import psutil

def collect_cpu_info():
    return {
        'usage': psutil.cpu_percent(interval=1),
        'cores': psutil.cpu_count(logical=False),
        'logical_processors': psutil.cpu_count(logical=True),
    }