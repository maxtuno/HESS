"""
///////////////////////////////////////////////////////////////////////////////
//        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
