# https://www.sfu.ca/~ssurjano/griewank.html

import numpy
import peqnp as cnf

class GriewankFunctionHESS:

	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def oracle(self, xs):
		return numpy.sum([(x ** 2) / 4000 for x in xs]) - numpy.prod([numpy.cos(x / numpy.sqrt(i + 1)) for i, x in enumerate(xs)]) + 1

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
		return cnf.hess_abstract(xs, self.oracle, self.f, self.g, self.log, target=0)
	
n = 100
gf = GriewankFunctionHESS(n ** -2, n ** 2)
print(gf.run(n))
