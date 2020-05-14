
def train(env, agent, nepisodes):
    for i in range(nepisodes):
        observation_state = env.reset()
        while(True):
            action = agent.action_select(observation_state)
            next_state, finished, reward = env.step(action)
            agent.update_policy(observation_state, next_state, action, reward)
            observation_state = next_state
            if finished:
                break

