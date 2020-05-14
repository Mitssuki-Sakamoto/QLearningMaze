from abc import *
import numpy as np

class Environment(metaclass=ABCMeta):

    """アクション対して，次状態，終了判定，報酬を返す"""
    @abstractmethod
    def step(self, actions):
        pass

    """可能な行動を返す"""
    @abstractmethod
    def actions(self):
        pass

    """環境をリセットする, 状態を返す"""
    @abstractmethod
    def reset(self):
        pass

class MazeEnvironment(Environment):
    STATUS_BLANK = 0 # 何もなし
    STATSU_WALL = 1 # 壁　使う予定なし
    STATUS_START = 2 # スタート地点
    STATUS_GOAL = 3 # ゴール地点
    ACTION_UP = (-1, 0)
    ACTION_DOWN = (1, 0)
    ACTION_RIGHT = (0, 1)
    ACTION_LEFT = (0, -1)
    ACTION_UP_KEY = "up"
    ACTION_DOWN_KEY  = "down"
    ACTION_RIGHT_KEY  = "right"
    ACTION_LEFT_KEY  = "left"
    ACTIONS = {ACTION_UP_KEY:ACTION_UP, ACTION_DOWN_KEY:ACTION_DOWN, ACTION_RIGHT_KEY:ACTION_RIGHT, ACTION_LEFT_KEY:ACTION_LEFT}

    def __init__(self, width = 8, height = 8, max_steps = 20, start_postion = (0,0), goal_postion = None, goal_reward = 10):
        self.width = width
        self.height = height
        self.max_steps = max_steps
        self.masses = np.zeros((width, height))
        self.start_position = start_postion
        self.goal_postion = goal_postion
        self.goal_reward = goal_reward
        self.agent_position = (0,0)
        self.nsteps = 0

        if self.goal_postion is None:
            self.goal_postion = (self.width - 1, self.height -1)

        self.masses[self.start_position[0]][self.start_position[1]] = MazeEnvironment.STATUS_START
        self.masses[self.goal_postion[0]][self.goal_postion[1]] = MazeEnvironment.STATUS_GOAL

        self.reset()

    def actions(self):
        return self.ACTIONS.keys()
    
    def reset(self):
        self.agent_position = self.start_position
        self.nsteps = 0
        return self.agent_position
    
    def step(self, action):
        self.nsteps += 1
        self.agent_position = MazeEnvironment.transition(self.masses, self.agent_position , action)
        reward = MazeEnvironment.get_reward(self.agent_position, self.goal_postion, self.goal_reward)
        finished = MazeEnvironment.is_finished(reward, self.nsteps, self.max_steps)
        return self.agent_position, finished, reward

    @staticmethod
    def transition(masses, current_postion, action_key):
        current_mass = masses[current_postion]
        if current_mass is MazeEnvironment.STATSU_WALL:
            return current_postion
        else :
            next_x = current_postion[0] + MazeEnvironment.ACTIONS[action_key][0]
            next_y = current_postion[1] + MazeEnvironment.ACTIONS[action_key][1]
            next_x = MazeEnvironment.clip(next_x, 0, masses.shape[0]-1)
            next_y = MazeEnvironment.clip(next_y, 0, masses.shape[1]-1)
            return (next_x, next_y)

    @staticmethod
    def get_reward(agent_postion, goal_postion, reward):
        if agent_postion == goal_postion:
            return reward
        return 0 # 移動ごとに負の報酬を与えても良い

    @staticmethod
    def is_finished(reward, nsteps, max_steps):
        if reward > 0:
            return True
        if nsteps >= max_steps:
            return True
        return False

    # 最小，最大内に収める
    @staticmethod
    def clip(value, min_, max_):
        if value < min_:
            value = min_
        elif value > max_:
            value = max_
        return value

