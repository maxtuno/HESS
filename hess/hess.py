# ///////////////////////////////////////////////////////////////////////////////
# //        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
# //                        oscar.riveros@peqnp.science                        //
# //                                                                           //
# //   without any restriction, Oscar Riveros reserved rights, patents and     //
# //  commercialization of this knowledge or derived directly from this work.  //
# ///////////////////////////////////////////////////////////////////////////////
def sequence(n, oracle, fast=True, cycles=1, target=0):
    """
    HESS Algorithm is a Universal Black Box Optimizer (sequence version).
    :param n: The size of sequence.
    :param oracle: The oracle, this output a number and input a sequence.
    :param fast: More fast less accuracy.
    :param cycles: How many times the HESS algorithm is executed.
    :param target: Any value less than this terminates the execution.
    :return optimized sequence.
    """
    xs = list(range(n))
    glb = oracle(xs) + 1
    opt = xs[:]

    def __inv(a, b, xs):
        i, j = min(a, b), max(a, b)
        while i < j:
            xs[i], xs[j] = xs[j], xs[i]
            i += 1
            j -= 1

    top = glb
    for _ in range(cycles):
        glb = top + 1
        if fast:
            while True:
                anchor = glb
                for i in range(len(xs) - 1):
                    for j in range(i + 1, len(xs)):
                        __inv(i, j, xs)
                        loc = oracle(xs)
                        if loc < glb:
                            glb = loc
                            if glb < top:
                                top = glb
                                opt = xs[:]
                                if top <= target:
                                    return opt
                        elif loc > glb:
                            __inv(i, j, xs)
                if anchor == glb:
                    break
        else:
            while True:
                anchor = glb
                for i in range(len(xs)):
                    for j in range(len(xs)):
                        __inv(i, j, xs)
                        loc = oracle(xs)
                        if loc < glb:
                            glb = loc
                            if glb < top:
                                top = glb
                                opt = xs[:]
                                if top <= target:
                                    return opt
                        elif loc > glb:
                            __inv(i, j, xs)
                if anchor == glb:
                    break

    return opt


# ///////////////////////////////////////////////////////////////////////////////
# //        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
# //                        oscar.riveros@peqnp.science                        //
# //                                                                           //
# //   without any restriction, Oscar Riveros reserved rights, patents and     //
# //  commercialization of this knowledge or derived directly from this work.  //
# ///////////////////////////////////////////////////////////////////////////////
def binary(n, oracle, fast=True, cycles=1, target=0):
    """
    HESS Algorithm is a Universal Black Box Optimizer (binary version).
    :param n: The size of bit vector.
    :param oracle: The oracle, this output a number and input a bit vector.
    :param fast: More fast some times less accuracy.
    :param cycles: How many times the HESS algorithm is executed.
    :param target: Any value less than this terminates the execution.
    :return optimized sequence.
    """
    xs = [False] * n
    glb = oracle(xs) + 1
    opt = xs[:]

    def __inv(i, j, xs):
        if xs[i] == xs[j]:
            xs[i] = not xs[j]
        else:
            aux = xs[i]
            xs[i] = not xs[j]
            xs[j] = aux

    top = glb
    for _ in range(cycles):
        glb = top + 1
        if fast:
            while True:
                anchor = glb
                for i in range(len(xs) - 1):
                    for j in range(i + 1, len(xs)):
                        __inv(i, j, xs)
                        loc = oracle(xs)
                        if loc < glb:
                            glb = loc
                            if glb < top:
                                top = glb
                                opt = xs[:]
                                if top <= target:
                                    return opt
                        elif loc > glb:
                            __inv(i, j, xs)
                if anchor == glb:
                    break
        else:
            while True:
                anchor = glb
                for i in range(len(xs)):
                    for j in range(len(xs)):
                        __inv(i, j, xs)
                        loc = oracle(xs)
                        if loc < glb:
                            glb = loc
                            if glb < top:
                                top = glb
                                opt = xs[:]
                                if top <= target:
                                    return opt
                        elif loc > glb:
                            __inv(i, j, xs)
                if anchor == glb:
                    break
    return opt


# ///////////////////////////////////////////////////////////////////////////////
# //        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
# //                        oscar.riveros@peqnp.science                        //
# //                                                                           //
# //   without any restriction, Oscar Riveros reserved rights, patents and     //
# //  commercialization of this knowledge or derived directly from this work.  //
# ///////////////////////////////////////////////////////////////////////////////
def abstract(xs, oracle, f, g, log=None, fast=False, cycles=1, target=0):
    """
    HESS Algorithm is a Universal Black Box Optimizer (abstract version).
    :param xs: The initial vector.
    :param oracle: The oracle, this output a number and input a vector.
    :param f: The f(i, j, xs).
    :param g: The g(i, j, xs).
    :param log: The log(top, opt).
    :param fast: More fast some times less accuracy.
    :param cycles: How many times the HESS algorithm is executed.
    :param target: Any value less than this terminates the execution.
    :return optimized vector over the oracle over and f, g.
    """
    glb = oracle(xs) + 1
    opt = xs[:]

    top = glb
    for _ in range(cycles):
        glb = top + 1
        if fast:
            while True:
                anchor = glb
                for i in range(len(xs) - 1):
                    for j in range(i + 1, len(xs)):
                        f(i, j, xs)
                        loc = oracle(xs)
                        if loc < glb:
                            glb = loc
                            if glb < top:
                                top = glb
                                opt = xs[:]
                                if log is not None:
                                    log(top, opt)
                                if top <= target:
                                    return opt
                        elif loc > glb:
                            g(i, j, xs)
                if anchor == glb:
                    break
        else:
            while True:
                anchor = glb
                for i in range(len(xs)):
                    for j in range(len(xs)):
                        f(i, j, xs)
                        loc = oracle(xs)
                        if loc < glb:
                            glb = loc
                            if glb < top:
                                top = glb
                                opt = xs[:]
                                if log is not None:
                                    log(top, opt)
                                if top <= target:
                                    return opt
                        elif loc > glb:
                            g(i, j, xs)
                if anchor == glb:
                    break
    return opt
