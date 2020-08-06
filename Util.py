import matplotlib.pyplot as plt
from Environment import MazeEnvironment
import numpy as np

def print_maze(maze_masess):
    for masses_low in maze_masess:
        for mass in masses_low:
            print(int(mass), " ", end="")
        print()
 
def q_table_of_each_goal_draw(Q_table, action_space, width, height, states = None):
    plt.clf()
    ax = plt.gca()
    for i in range(width):
        for j in range(height):
            for action in action_space:
                #plt.text(j + 0.5, (width - i) - 0.5, 'S' + str(i * len(q_table_row) + j), size=14, ha='center',
                #        va='center')
                action_name = ''
                state = (i, j)
                if state in Q_table.keys():
                    Q_value_action = Q_table[state][action]
                else:
                    Q_value_action = 0
                action_position = 0.1
                if action == MazeEnvironment.ACTION_UP_KEY:
                    action_position = 0.1
                    action_name ='↑'
                elif action == MazeEnvironment.ACTION_DOWN_KEY:
                    action_position = 0.85
                    action_name = '↓'
                elif action == MazeEnvironment.ACTION_LEFT_KEY:
                    action_position = 0.35
                    action_name = '←'
                elif action == MazeEnvironment.ACTION_RIGHT_KEY:
                    action_position = 0.6
                    action_name = '→'
                plt.text(j + 0.5, i + action_position, '{}: {:.2g}'.format(action_name, Q_value_action),
                         size=14, ha='center', va='center', )
    if states:
        for state in states:
            x = np.arange(state[0], state[0]+1, 0.01)
            plt.fill_between(x, state[1], state[1]+1, facecolor='y', alpha=0.5)
    # 描画範囲の設定と目盛りを消す設定
    ax.set_xlim(0, width)
    ax.set_ylim(height, 0)
    plt.tick_params(axis='both', which='both', bottom='off', top='off',
                    labelbottom='off', right='off', left='off', labelleft='off')

    # 現在値S0に緑丸を描画する
    # line, = ax.plot([0.5], [2.5], marker="o", color='g', markersize=60)
    # plt.rcParams["grid.linewidth"] = 2.0
    # 5刻みに目盛り表示
    plt.xticks(list(range(width)))
    # 0.1刻みに目盛り表示
    plt.yticks(list(range(height)))
    plt.grid()
    # グラフ描画
    plt.pause(0.000001)
    plt.draw()
#    plt.show()
