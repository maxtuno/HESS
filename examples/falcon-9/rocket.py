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

# Rocket Lander
# https://github.com/sdsubhajitdas/Rocket_Lander_Gym

import numpy
import gym
import rocket_lander_gym

n = 10
m = 3

env = gym.make('RocketLander-v0')

while True:
    neutral_point = numpy.reshape([1.9999998776848253, 1.9259253718016147, 0.5500510039881372, 1.5065243556359218, 2.8122261569279905, 2.552202036822007, -0.1494068350833475, 0.6192405169958881, 1.0863314420468493, 4.854083961570884, -0.68214964798994, 0.12692590645620005, 3.4784048724641803, -1.7834296491311488, -0.9779903729988857, -0.920653245897249, -0.09611612591980112, 0.5956861516385292, 0.2906676132298813, -0.1650166410958379, -0.4957102642628852, -0.15575384613488308, -1.1511550455509836, -0.12073522466450148, -0.016576942857992716, -0.5581155488791617, 0.44951076438202553, 1.0780343864372304, -0.46621847950420037, -0.2082722117654251], newshape=(m, n))
    observation = env.reset()
    total_reward = 0
    while True:
        env.render()
        action = numpy.matmul(neutral_point, observation)
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
    print(total_reward)
    env.close()
