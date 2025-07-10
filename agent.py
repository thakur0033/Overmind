
class Agent:
    def __init__(self, id, role):
        self.id = id
        self.role = role
        self.strategy_weights = {}

    def to_dict(self):
        return {
            "id": self.id,
            "role": self.role,
            "strategy_weights": self.strategy_weights
        }

    @staticmethod
    def from_dict(data):
        agent = Agent(data["id"], data["role"])
        agent.strategy_weights = data.get("strategy_weights", {})
        return agent
