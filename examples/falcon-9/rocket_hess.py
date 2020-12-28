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

import multiprocessing

import gym
import hess
import numpy
# Rocket Lander
# https://github.com/sdsubhajitdas/Rocket_Lander_Gym
import rocket_lander_gym

glb = -numpy.inf
n = 10
m = 3
batch = 10

env = gym.make('RocketLander-v0')


def oracle(xs):
    global glb
    neutral_point = numpy.reshape(xs, newshape=(m, n))
    loc = 0
    for _ in range(batch):
        observation = env.reset()
        ll = []
        while True:
            action = numpy.matmul(neutral_point, observation)
            observation, reward, done, info = env.step(action)
            ll += [reward]
            if done:
                break
        loc += numpy.mean(ll) * numpy.std(ll)
    return -loc


def f(i, j, xs):
    xs[i], xs[j] = xs[j] / 2, xs[i] / 2
    xs[i:j] = xs[i:j][::-1]
    xs[i], xs[j] = xs[j] + 1, xs[i] + 1


def g(i, j, xs):
    xs[i], xs[j] = xs[j] - 1, xs[i] - 1
    xs[i:j] = xs[i:j][::-1]
    xs[i], xs[j] = xs[j] * 2, xs[i] * 2


def log(top, opt):
    print(top)
    numpy.savetxt('neutral_point_{}.txt'.format(top), opt)


def apply(seed):
    numpy.random.seed(seed)
    xs = numpy.random.standard_cauchy(size=m * n)
    hess.abstract(xs, oracle, f, g, log)


if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        p.map(apply, numpy.random.randint(0, 2 ** 16, size=n * m))
        env.close()
