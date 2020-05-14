import random
from abc import *

class Agent(metaclass=ABCMeta):

    """アクション対して，次状態，終了判定，報酬を返す"""
    @abstractmethod
    def action_select(self, actions):
        pass

    """環境をリセットする, 状態を返す"""
    @abstractmethod
    def update_policy(self, current_state, next_state, reward):
        pass

class QLearningAgent(Agent):
    # epsilon greedy 特化　あまりよくない
    def __init__(self, alpha, gamma, epsilon, action_space):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.action_space = action_space
        self.Q_table = {}
    
    def action_select(self, observation_state):
        QLearningAgent.Q_value_exist(self.Q_table, observation_state, self.action_space)
        Q_value = self.Q_table[observation_state]
        action = QLearningAgent.epsilon_greedy_select(Q_value, self.epsilon)
        return action

    def update_policy(self, current_state, next_state, action, reward):
        QLearningAgent.Q_value_exist(self.Q_table, next_state, self.action_space)
        next_max_Q_value = max(self.Q_table[next_state].values())
        current_Q_value = self.Q_table[current_state][action]
        self.Q_table[current_state][action] = (1 - self.alpha) * current_Q_value + self.alpha * (reward + self.gamma*next_max_Q_value)

    @staticmethod
    def new_Q_Value(state, action_space):
        Q_Value = {}
        for action in action_space:
            Q_Value[action] = 0
        return Q_Value
    
    @staticmethod
    def epsilon_greedy_select(Q_value, epsilon):
        if random.random() > epsilon:
            max_val = max(Q_value.values())
            actions = [key for key in Q_value.keys() if Q_value[key] == max_val]
        else:
            actions = list(Q_value.keys())
        return random.choice(actions)
    
    @staticmethod
    def Q_value_exist(Q_table, state, action_space):
        if state not in Q_table.keys():
            Q_table[state] = QLearningAgent.new_Q_Value(state, action_space)
