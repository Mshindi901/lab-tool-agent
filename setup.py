from agent.identity import save_agent_id

def main():
    agentId = input("Enter the agent ID: ").strip()
    if not agentId:
        print("Agent ID cannot be empty.")
        return
    save_agent_id(agentId)

if __name__ == "__main__":
    main()