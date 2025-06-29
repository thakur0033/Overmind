
from content_engine import generate_post
from poster import post_to_twitter, post_to_medium
from engagement_tracker import evaluate_post
from score_updater import reinforce_agent
from agent import Agent
from utils.agent_db import load_agents, save_agents
import random
import time

TOPICS = open("campaigns/tech_topics.txt").read().splitlines()

def run_campaign():
    agents = load_agents()
    if not agents:
        print("⚠️ No agents found, creating dummy agent.")
        agent = Agent(1, "content_bot")
        agent.strategy_weights = {"aggressive": 1.0, "educational": 1.0}
        agents = [agent]

    topic = random.choice(TOPICS)
    for agent in agents:
        strategy = random.choice(list(agent.strategy_weights.keys()))
        post = generate_post(topic)
        if strategy == "aggressive":
            response = post_to_twitter(post)
        else:
            response = post_to_medium(post, f"Learn more about {topic}")
        score = evaluate_post(response)
        reinforce_agent(agent, strategy, score)
        print(f"[✓] Agent {agent.id} posted using {strategy} → score {score}")
        time.sleep(2)

    save_agents(agents)

if __name__ == "__main__":
    run_campaign()
