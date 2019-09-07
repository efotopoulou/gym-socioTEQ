#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:39:39 2019

@author: eleni
"""

import gym
import gym_socioTEQ
env = gym.make('socioTEQ-v0')


for i_episode in range(2):
    observation = env.reset()
    for t in range(9):
        env.render()
        print("observation",observation)
        #action = env.action_space.sample()
        action = t
        print("action",action)
        observation, reward, done, info = env.step(action)
        print("new observation",observation)
        print("reward",reward)
        print("done",done)
        print("info",info)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
