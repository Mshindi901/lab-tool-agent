import psutil

def collect_network_info():
    interfaces = psutil.net_if_addrs()
    result = {}

    for interface, addresses in interfaces.items():
        result[interface] = []
        for addr in addresses:
            result[interface].append({
                'ip_address': addr.address,
                'netmask': addr.netmask,
            })

    return result