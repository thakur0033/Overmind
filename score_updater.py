
def reinforce_agent(agent, strategy, score):
    if strategy in agent.strategy_weights:
        agent.strategy_weights[strategy] += score * 0.1
