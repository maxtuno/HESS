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

# video https://twitter.com/maxtuno/status/1312278639485087745

import numpy
import gym
import rocket_lander_gym

env = gym.make('RocketLander-v0')

# sub-optimal solution
neutral_point = [[-0.7698760981379379, -0.26427996182377783, 0.4463323778700458, -0.5177312510310029, -1.7754691520095647, 0.2535078637970811, -0.838641803575626, -0.6503342749455817, -0.9678349293737798, 1.6691200510079733], [0.059188425297189665, 0.234285827021381, 1.5146199891809016, 0.3368704439473176, -0.6514198681046239, -2.4847039860387983, -0.30236870196778015, 0.17680894649065493, -0.18372453368830574, -0.09528632594099248], [0.4207405283608752, -0.5387197708014494, -0.2662149259177863, 1.2393998588645518, 0.737056190505862, 0.6938626422156343, -0.815530330059005, 0.3876804541976694, 0.10653700578986429, -0.3145769234612008]]
while True:
    observation = env.reset()
    for _ in range(1000):
        env.render()
        action = numpy.matmul(neutral_point, observation)
        observation, reward, done, info = env.step(action)
        # if done:
        #    break
    env.close()
