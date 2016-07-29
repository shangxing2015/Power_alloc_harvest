__author__ = 'shangxing'

from env import Environment
from qtable import QAgent
from config import *
import random
import time



env = Environment(POW_DIS, CHAN_DIS, QMAX, CHAN_STATE, STATE_SIZE)

init_state = env.get_state()

action_id = random.randint(0, len(ALL_ACTIONS[init_state])-1)
action = ALL_ACTIONS[init_state][action_id]

brain = QAgent(init_state, action, ALL_ACTIONS)





total  = 0

file = 'log'

f = open(file, 'w')

start_time = time.time()

for i in range(T_THRESHOLD):

    count = i+1

    observation, reward = env.step(action)

    total += reward

    action = brain.observe_and_act(observation, action, i)


    if count % PERIOD == 0:

        avg_reward = total/float(count)

        duration = time.time() - start_time
        f.write('Index %d: avg_reward is %f, observation is %s, action is: %s and time duration is %f' % (
            count, avg_reward, str(observation), str(action), duration))
        f.write('\n')


f.close()




