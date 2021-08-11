import time
# https://twitter.com/maxtuno/status/1425372049367830532
# https://github.com/qgallouedec/panda-gym
# https://analyticsindiamag.com/exploring-panda-gym-a-multi-goal-reinforcement-learning-environment/
import panda_gym
import gym
import numpy


def transform(xs):
    return xs / numpy.linalg.norm(xs)


if __name__ == '__main__':
    m, n = 3, 6

    env = gym.make('PandaReach-v1', render=True)

    while True:
        neutral_point = [1.08647e+252, 2.3465e+287, 3.03701e+296, 6.84933e+284, 6.07909e+282, 1.21218e+279, 4.57363e+229, 4.49605e+236, 4.50756e+284, 5.13649e+301, 2.12983e+259, 6.44219e+243, 3.75221e+296, 9.24223e+294, 2.9631e+281, 3.83031e+229, 1.92892e+281, 7.76857e+281]
        total_rewards = 0
        observation = env.reset()
        observation, achieved_goal, desired_goal = observation['observation'], observation['achieved_goal'], observation['desired_goal']
        while True:
            time.sleep(0.02)
            action = transform(desired_goal - achieved_goal) - transform(numpy.matmul(numpy.reshape(neutral_point, newshape=(m, n)), observation))
            observation, reward, done, info = env.step(action)
            observation, achieved_goal, desired_goal = observation['observation'], observation['achieved_goal'], observation['desired_goal']
            total_rewards += reward
            if done:
                break
        print(total_rewards)
