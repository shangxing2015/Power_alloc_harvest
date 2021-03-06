__author__ = 'shangxing'


PERIOD = 100  # for writing to the file
T_THRESHOLD = 300000  # 5000000# num of plays; 80000000
T_EVAL = 50000
T_CVG = 15000


OBSERVE = 500  # timesteps to observe before training
EXPLORE = 10000  # frames over which to anneal epsilon #700000
FINAL_EPSILON = 0.1  # final value of epsilon: for epsilon annealing
INITIAL_EPSILON = 1  # starting value of epsilon
INITIAL_ALPHA = 0.3

ALL_ACTIONS= [[0], [1], [1,2], [1,2,3], [1,2,3,4]]


CHAN_DIS = [0.2, 0.8]
CHAN_STATE = [10, 0]

POW_DIS = [0.2, 0.2, 0.2, 0.2, 0.2]

STATE_SIZE = 5
QMAX = 4