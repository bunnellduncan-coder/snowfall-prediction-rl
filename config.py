# Configuration settings for the Reinforcement Learning environment

# Set the learning rate
LEARNING_RATE = 0.001

# Set the number of episodes
NUM_EPISODES = 1000

# Set maximum steps per episode
MAX_STEPS_PER_EPISODE = 100

# Define the discount factor
DISCOUNT_FACTOR = 0.99

# Set exploration rate
EXPLORATION_RATE = 1.0

# Set the minimum exploration rate
MIN_EXPLORATION_RATE = 0.01

# Set the decay rate for exploration
EXPLORATION_DECAY_RATE = 0.001

# Define rewards
REWARDS = {
    'win': 1,
    'lose': -1,
    'draw': 0
}