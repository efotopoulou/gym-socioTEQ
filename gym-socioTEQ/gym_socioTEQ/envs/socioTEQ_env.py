import gym
from gym import error, spaces, utils
from random import randrange
import numpy as np

class SocioTEQEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
        self.state = [randrange(50),randrange(50),randrange(50),randrange(50)]
        self.counter = 0
        self.done = 0
        self.info = "init info"
        self.reward = 0
  def step(self, action):
    if self.done == 1:
        print("Game Over")
        return [self.state, self.reward, self.done, self.info]
    else:
        action_id = ACTION_LOOKUP[action][0]
        action_propability = ACTION_LOOKUP[action][2]
        old_state = self.state
        self.state = [old_state[0]+old_state[0]*action_propability , old_state[1]+old_state[1]*action_propability , old_state[2]+old_state[2]*action_propability , old_state[3]+old_state[3]*action_propability]
        print("action_propability",action_propability)
        self.info = "applied propability "+str(action_propability)
        self.counter += 1
        if(self.counter == 9):
            self.done = 1;
        self.render()
        self.reward = np.mean(self.state)

    return [self.state, self.reward, self.done, self.info]
    

  def reset(self):
    self.state = [randrange(50),randrange(50),randrange(100),randrange(50)]
    self.counter = 0
    self.done = 0
    self.reward = 0
    self.info = "sample info"
    return self.state


  def render(self, mode='human', close=False):
    print(self.state)
    print("")


ACTION_LOOKUP = [
    [0 ,"Activity0",0.1],
    [1 ,"Activity1",-0.15],
    [2 ,"Activity2",0.2],
    [3 ,"Activity3",0.25],
    [4 ,"Activity4",0.5],
    [5 ,"Activity5",0.8],
    [6 ,"Activity6",0.65],
    [7 ,"Activity7",-0.4],
    [8 ,"Activity8",0.5],
    [9 ,"Activity9",0.6],
    [10 ,"Activity10",0.7],
    [11 ,"Activity11",-0.8],
    [12 ,"Activity12",0],
    [13 ,"Activity13",0.91],
    [14 ,"Activity14",1],
    [15 ,"Activity15",-0.45],
]
