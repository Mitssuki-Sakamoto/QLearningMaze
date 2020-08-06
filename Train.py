import Util
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def train(env, agent, nepisodes):
    for i in range(nepisodes):
        observation_states = []
        observation_state = env.reset()
        observation_states.append(observation_state)
        while(True):
            action = agent.action_select(observation_state)
            next_state, finished, reward = env.step(action)
            agent.update_policy(observation_state, next_state, action, reward)
            observation_state = next_state
            observation_states.append(observation_state)
            if finished:
                if i % 100 == 0:
                    Util.q_table_of_each_goal_draw(agent.Q_table, env.actions(), env.width, env.height, observation_states)
                break
    plt.show()

