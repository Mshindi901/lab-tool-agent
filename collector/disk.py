import psutil

disk = psutil.disk_usage('/')

def collect_disk_info():
    return {
        'disk_total': disk.total,
        'disk_used': disk.used,
        'disk_free': disk.free,
        'disk_usage_percent': disk.percent
    }