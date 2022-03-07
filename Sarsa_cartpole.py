import os
import gym
import pickle
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("CartPole-v1")
ROOT_DIR = os.path.dirname(__file__)
LOAD_PRETRAINED = False
VALIDATING = True
LEARNING_RATE = 0.45
DISCOUNT = 0.95
EPISODES = 300000
SHOW_EVERY = 10000
STATS_EVERY = 100
epsilon = 1
EPSILON_THRESHOLD = 0.1
epsilon_decay_value = 0.99999
if VALIDATING:
    EPISODES = 10
    SHOW_EVERY = 1
    LOAD_PRETRAINED = True


# Since Observation is infinitely large we are limiting it.
observation_space_high = np.array([env.observation_space.high[0], 4, env.observation_space.high[2], 4])
observation_space_low = np.array([env.observation_space.low[0], -4, env.observation_space.low[2], -4])

# Making discrete observation space
DISCRETE_OS_SIZE = [31, 31, 31, 31]
discrete_os_win_size = (observation_space_high - observation_space_low) / [i - 1 for i in DISCRETE_OS_SIZE]
if LOAD_PRETRAINED:
    q_table = np.load(os.path.realpath(os.path.join(ROOT_DIR, 'qtable.npy')))
else:
    q_table = np.random.uniform(low = 0, high = 0, size = (DISCRETE_OS_SIZE + [env.action_space.n]))

# defining action space
action_space = [i for i in range(env.action_space.n)]

ep_rewards = []
aggr_ep_rewards = {'ep': [], 'avg': [], 'max': [], 'min': []}

def get_discrete_state(state):
    ds = (state - observation_space_low) / discrete_os_win_size
    return tuple(ds.astype(np.int32))


if VALIDATING:
    epsilon = 0

for episode in range(EPISODES):
    episode_reward = 0
    discrete_state = get_discrete_state(env.reset())
    done = False
    if np.random.random() > epsilon:
        # Get action from Q table
        action = np.argmax(q_table[discrete_state])
    else:
        # Get random action
        action = np.random.choice(action_space)
    while not done:
        new_state, reward, done, _ = env.step(action)
        episode_reward += reward
        new_discrete_state = get_discrete_state(new_state)
        if episode % SHOW_EVERY == 0:
            env.render()

        if np.random.random() > epsilon:
            # Get action from Q table
            new_action = np.argmax(q_table[new_discrete_state])
        else:
            # Get random action
            new_action = np.random.choice(action_space)

        if not VALIDATING:
            if not done:
                # And here's our equation for updating table
                q_table[discrete_state + (action,)] = q_table[discrete_state + (action,)] + LEARNING_RATE * (
                        reward + (DISCOUNT * q_table[new_discrete_state + (new_action,)]) - q_table[discrete_state + (action,)])

        discrete_state = new_discrete_state
        action = new_action
    if not VALIDATING:
        # Decaying is being done every episode if episode number is within decaying range
        if epsilon >= EPSILON_THRESHOLD:
            epsilon *= epsilon_decay_value
        ep_rewards.append(episode_reward)
        if not episode % STATS_EVERY:
            average_reward = sum(ep_rewards[-STATS_EVERY:]) / STATS_EVERY
            aggr_ep_rewards['ep'].append(episode)
            aggr_ep_rewards['avg'].append(average_reward)
            aggr_ep_rewards['max'].append(max(ep_rewards[-STATS_EVERY:]))
            aggr_ep_rewards['min'].append(min(ep_rewards[-STATS_EVERY:]))
            print(f'Episode: {episode:>5d}, average reward: {average_reward:>4.1f}, current epsilon: {epsilon:>1.2f}')
        if episode % 10 == 0:
            np.save(os.path.realpath(os.path.join(ROOT_DIR, 'qtable.npy')), q_table)

env.close()

if not VALIDATING:
    filehandler = open("statistics", 'wb')
    pickle.dump(aggr_ep_rewards, filehandler)

    plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label = "average rewards")
    plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label = "max rewards")
    plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label = "min rewards")
    plt.legend(loc = 4)
    plt.savefig(os.path.realpath(os.path.join(ROOT_DIR, "Statistics.png")))
    plt.show()
