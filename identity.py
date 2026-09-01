from pathlib import Path


directory = Path.home() / '.agent'
agent_id_file = directory / ".agent_id"
def get_agent_id():
    if not agent_id_file.exists():
        return RuntimeError("Agent ID file does not exist.");
    return agent_id_file.read_text().strip()

def save_agent_id(id):
    directory.mkdir(exist_ok=True)
    agent_id_file.write_text(id)