import gym
import numpy as np

import hess

best = 0
cursor = 0
render = False


def run_episode(seq):
    global env, best, render, cursor
    observation = env.reset()
    total_reward = 0
    while True:
        if render:
            env.render()
        action = np.dot(par[seq[:n]], observation)
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if total_reward > best:
            best = total_reward
            if best > cursor:
                cursor = best
                print(best)
                if best >= 10000:
                    render = True
        if done:
            break
    return -total_reward


if __name__ == '__main__':

    n = 111
    m = 1000
    while True:
        env = gym.make('Ant-v2')
        best = 0
        par = np.random.normal(size=n * m)
        seq = hess.sequence(n * m, oracle=run_episode, fast=False)
        env.close()
