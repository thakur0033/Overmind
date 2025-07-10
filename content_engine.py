
import random

def generate_post(topic):
    templates = [
        f"Let's talk about {topic}! 🤖",
        f"New breakthroughs in {topic} are reshaping the world.",
        f"What does {topic} mean for the future of humanity?",
        f"🔥 Hot topic: {topic}. Here's what you need to know.",
        f"{topic} is evolving rapidly — stay informed!"
    ]
    return random.choice(templates)
