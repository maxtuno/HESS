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

import numpy
import gym

n = 2
m = 4

env = gym.make('MountainCarContinuous-v0')

while True:
    neutral_point = numpy.reshape([-1.212396912579444264e+00, 5.771101602032016942e+00, -3.506713229392263820e+00, -5.610492336268912972e-02, 1.627993469028583107e+00, 1.831139126435835207e+00, 1.839116204070150307e+00, 1.754359158335776048e+00], newshape=(m, n))
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
