import httpx

from agent.config import API_URL, requestTimeout, heartbeatInterval
from agent.identity import get_agent_id

class APIClient:
    def __init__(self):
        self.base_url = API_URL
        self.agent_id = get_agent_id()

    def headers(self):
        return {
            'X-Agent-ID': self.agent_id,
            'Content-Type': 'application/json'
        }

    def _send_machine_info(self, memory, disk, network, system):
        data = {
            'cpu': system['processor'],
            'o_s': system['os'],
            'os_version': system['os_version'],
            'architecture': system['architecture'],
            'ram_total': memory['ram_total'],
            'disk_total': disk['disk_total'],
            'ip_address': network['ip_address'],
        }
        response = httpx.put(
            f"{self.base_url}/agent",
            json=data,
            headers=self.headers(),
            timeout=requestTimeout
        )

    def _send_heartbeat(self, cpu, memory, disk):
        data = {
            'cpu_usage': cpu['cpu_usage'],
            'ram_usage': memory['ram_usage_percent'],
            'disk_usage': disk['disk_usage_percent'],
        }
        response = httpx.post(
            f"{self.base_url}/telemetry",
            json=data,
            headers=self.headers(),
            timeout=requestTimeout
        )