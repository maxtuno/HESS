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

# https://www.sfu.ca/~ssurjano/griewank.html

import numpy
import hess

class GriewankFunctionHESS:

	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def oracle(self, xs):
		return numpy.sum([(x ** 2) / 4000 for i, x in enumerate(xs)]) + numpy.prod([numpy.cos(x / numpy.sqrt(i + 1)) for i, x in enumerate(xs)]) + 1

	def f(self, i, j, xs):
		xs[i], xs[j] = self.a + xs[i] / self.b, self.a + xs[j] / self.b
		xs[i:j] = xs[i:j][::-1]

	def g(self, i, j, xs):
		xs[i:j] = xs[i:j][::-1]
		xs[i], xs[j] = self.b * xs[i] - self.a, self.b * xs[j] - self.a
		
	def log(self, top, opt):
		print(top)

	def run(self, n):
		xs = numpy.random.randint(-600, 600, size=n)
		return hess.abstract(xs, self.oracle, self.f, self.g, self.log, target=0)

if __name__ == '__main__':
	
	n = 100
	my_hess = GriewankFunctionHESS(n ** -2, n ** 2)
	print(my_hess.run(n))