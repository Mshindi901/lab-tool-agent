import psutil

memory = psutil.virtual_memory()

def collect_memory_info():
    return {
        'ram_total': memory.total,
        'ram_available': memory.available,
        'ram_usage_percent': memory.percent,
        'ram_used': memory.used,
    }