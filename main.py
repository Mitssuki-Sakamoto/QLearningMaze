import argparse
from Environment import MazeEnvironment
from Agent import QLearningAgent
from Train import train
import Util
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gamma', type=float, default=0.9, help='discount factor for rewards')
    parser.add_argument('--alpha', type=float, default=0.1, help='learning rate')
    parser.add_argument('--epsilon', type=float, default=0.3)
    parser.add_argument('--num_steps', type=int, default=50, help='number of steps in each episode (default: 50)')
    parser.add_argument('--max_w', type=int, default=5, help='maze width (default: 5)')
    parser.add_argument('--max_h', type=int, default=5, help='maze height (default: 5)')
    parser.add_argument('--nepisodes', type=int, default=5000,
                        help='number of training episodes (default: 5000)')
    args = parser.parse_args()

    envirornment = MazeEnvironment(width = args.max_w, height = args.max_h, max_steps = args.num_steps)
    action_space = envirornment.actions()

    agent = QLearningAgent(alpha=args.alpha, gamma=args.gamma, epsilon=args.epsilon, action_space = action_space)

    train(envirornment, agent, args.nepisodes)
    fig = plt.figure(figsize=(envirornment.width, envirornment.height))
    Util.print_maze(envirornment.masses)
    #Util.q_table_of_each_goal_show(agent.Q_table, action_space, envirornment.width, envirornment.height)

if __name__ == "__main__":
    main()