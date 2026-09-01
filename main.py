from agent.identity import get_agent_id
from agent.services.heartbeat import send_heartbeat

def main():

    agent_id = get_agent_id()
    if not agent_id:
        print("Agent ID not found. Please register the agent first.")
        return

    print(f"Agent ID: {agent_id}")

    send_heartbeat()


if __name__ == "__main__":
    main()