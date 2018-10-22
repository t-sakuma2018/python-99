def table(f):
    # lambda a, b: AND(a, OR(a, b))
    # lambda a, b, c: EQ(AND(a, OR(b, c)), OR(AND(a, b), AND(a, c)))
    aaa = []
    aaa += [[f(True, False), f(True, False), f(True, False)]]
    aaa += [[f(True, False), f(False, False), f(True, False)]]
    aaa += [[f(False, False), f(True, False), f(False, False)]]
    aaa += [[f(False, False), f(False, False), f(False, False)]]
    return aaa

# result += [[lmd(False, False), lmd(False, False), lmd(False, False)]]