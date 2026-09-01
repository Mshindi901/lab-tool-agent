import time
from agent.collector.system import get_system_info
from agent.collector.cpu import collect_cpu_info
from agent.collector.memory import collect_memory_info
from agent.collector.disk import collect_disk_info
from agent.collector.network import collect_network_info
from agent.client.client import APIClient
from agent.config import heartbeatInterval


cpu = collect_cpu_info()
system = get_system_info()
memory = collect_memory_info()
disk = collect_disk_info()
network = collect_network_info()

def send_heartbeat():

    api_client = APIClient()
    while True:
        try:
            response = api_client._send_machine_info(cpu, system, memory, disk, network)
            print(f'System Info sent successfully. Response: {response}')

            heartbeat_response = api_client._send_heartbeat(cpu, memory, disk)
            print(f'Heartbeat sent successfully. Response: {heartbeat_response}')
        except Exception as error:
            print(f'Error sending heartbeat: {error}')
        time.sleep(heartbeatInterval)
