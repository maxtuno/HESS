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

optimal = [-2.979900022517839031e-01,-1.031334334454611312e+00,-8.795610680105480084e-01,1.075001153457021186e+00,-8.430827719194636805e-01,8.116600408806783351e-01,-2.213790115073606124e+00,7.376142702380087401e-01,-9.519107256178731546e-01,7.660094576698798230e-01,-7.891411686032975270e-01,-8.048057099593830532e-01,2.310800345188298299e-01,4.570687718213536366e-01,-1.973531180112320094e-01,-1.808498150883082467e-02,-8.298738368124513043e-01,-1.040207432273779098e+00,-1.453352508055222758e+00,1.173243343639656322e+00,2.312873102136226322e+00,2.124604600260161291e+00,-7.151381238602967372e-01,2.711675602851499001e+00,-1.764096076087023457e+00,2.696535323121830308e-01,1.024116697471825432e+00,-4.807824074978712114e-01,6.502785132352384423e-01,-5.796947659210504034e-01,-5.750966731881582694e-01,2.452123730885408914e+00,-7.673992813742445129e-01,-1.689377344957293303e+00,6.144062682382437496e-02,-1.707652988246791903e+00,9.500683681183449414e-01,2.733117686075986263e+00,7.101772678050011223e-02,1.834381367483431058e+00,-1.351284006348216327e+00,4.318795146587343647e-01,2.102527911994487297e-01,3.102795928512842027e-01,-8.315565820727999213e-01,5.899447098415032675e-01,8.995160159217143736e-01,1.638188939654869225e+00,2.978545978797729754e-01,8.808061074244724065e-01,1.630675456446602833e+00,1.850898318052996316e+00,1.023750303983424148e+00,-1.543809354596165972e+00,1.643881330661338402e-01,-1.747434972892311089e+00,-5.938783367476409003e-01,4.699679875321114975e-01,-1.243013767909446843e+00,-5.938616939160176189e-01,-3.309226032282187591e-01,1.643455705266412270e+00,3.788391330051786576e-02,1.059436329564332757e+00,1.598891642748642150e+00,-1.141365825190526984e+00,-9.665386010003530481e-01,-1.902094093993628721e-01,2.435038932350081620e+00,2.350782712494194349e-01,-2.662860340421757122e-01,-5.738391605893478076e-01,7.771358919425781497e-01,5.750407548481792364e-02,-9.449256254595335136e-01,-5.677602784865256602e-01,5.616632416608821066e-01,-1.945138910077940930e-01,1.155235865801490736e+00,-8.951072509412538736e-02,-1.017562317306189845e+00,-1.748415543568163422e+00,-5.204414958378713596e-01,-2.508036406135583651e-01,6.729672217272232304e-01,-9.514415264400688521e-01,-3.185790514412001895e-01,-5.986752455080953661e-01,-5.925223197171281680e-02,-6.136228775084379139e-01,1.578414990183061750e+00,5.516271026674899325e-01,2.031644769437693121e+00,-5.348552817837963769e-01,1.669355116425471408e+00,-2.389316312679156951e-01,-5.382968620138219862e-01,3.436264580346477082e+00,8.326451606240854453e-01,-4.147727903942284855e-01,1.803809892099993650e+00,5.134696333741655128e-01,-1.627348434910269037e-01,3.704700816193752522e-02,-1.311062813203962119e+00,-1.485457491638368099e-01,-1.008353274995713145e+00,1.004720370980423327e+00,1.042670638392622973e+00,4.081149220429005076e-01,-6.336354797905729974e-02]

def test():
    global env
    observation = env.reset()
    while True:
        env.render()
        action = np.dot(optimal, observation)
        observation, reward, done, info = env.step(action)
        if done:
            break


if __name__ == '__main__':
    env = gym.make('Ant-v2')
    for _ in range(10):
        test()
    env.close()