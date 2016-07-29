__author__ = 'shangxing'

import random
import math



class Environment:

    def __init__(self, pow_dis, chan_dis, q_max, chan_state, state_size):

        self.state_space = [i for i in range(state_size)]

        self.chan_state = chan_state

        self.current_state = random.randint(0, state_size-1)

        self.pow_dis = pow_dis

        self.chan_dis = chan_dis

        self.q_max = q_max

        count = 0

        for i in range(len(self.pow_dis)):
            count += self.pow_dis[i]
            self.pow_dis[i] = count

        count = 0

        for i in range(len(self.chan_dis)):
            count += self.chan_dis[i]
            self.chan_dis[i] = count


        print self.pow_dis
        print self.chan_dis


    def _state_transit(self, action):

        temp, check = random.random(), False

        for i in range(len(self.pow_dis)-1):

            if temp >= self.pow_dis[i] and temp < self.pow_dis[i+1]:
                check = True
                break

        if check:

            p_t = self.state_space[i+1]

        else:

            p_t = self.state_space[0]


        self.current_state = min(self.current_state+p_t-action, self.q_max)



    def get_state(self):

        return self.current_state

    def step(self, action):

        temp, check = random.random(), False

        for i in range(len(self.chan_dis)-1):

            if temp >= self.chan_dis[i] and temp < self.chan_dis[i+1]:
                check = True
                break

        if check:
            x_t = self.chan_state[i+1]


        else:

            x_t = self.chan_state[0]



        reward = math.log(1+action*x_t,2)

        self._state_transit(action)

        observation = self.current_state

        return observation, reward