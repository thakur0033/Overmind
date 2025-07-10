
import json
import os

def load_agents():
    from agent import Agent
    path = "data/agents_db.json"
    if not os.path.exists(path):
        return []
    with open(path) as f:
        data = json.load(f)
    return [Agent.from_dict(d) for d in data]

def save_agents(agents):
    from agent import Agent
    data = [agent.to_dict() for agent in agents]
    with open("data/agents_db.json", "w") as f:
        json.dump(data, f, indent=2)
