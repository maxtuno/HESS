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
import numpy

env = gym.make('LunarLanderContinuous-v2')

m = 2
n = 8

while True:
    neutral_point = numpy.reshape([1.177125615603793030e+00,
                                   -4.197932515988081370e+00,
                                   -1.347259345812264586e+00,
                                   -4.885679618220995835e+00,
                                   6.970910383777482178e-01,
                                   2.185798719938597756e+00,
                                   3.188732985068926801e-02,
                                   -9.165728166498317009e+00,
                                   -1.254973751386146086e+00,
                                   -1.816197542302808943e+00,
                                   -4.320783664145809944e+00,
                                   -1.569448432728725251e+00,
                                   2.513738406101801548e+00,
                                   8.019424215262814570e+00,
                                   -4.700683499063157411e-01,
                                   2.820100098749226403e-01], newshape=(m, n))
    observation = env.reset()
    total_reward = 0
    while True:
        env.render()
        action = numpy.matmul(neutral_point, observation)
        action /= numpy.linalg.norm(action)
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
    print(total_reward)
    env.close()
