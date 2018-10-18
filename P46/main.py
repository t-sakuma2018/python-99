

def AND(A, B):

    buf = A + B
    if buf == 2:
        return True
    else:
        return False


def OR(A, B):
    buf = A + B
    if buf >= 1:
        return True
    else:
        return False


def NAND(A, B):
    buf = A + B
    if buf < 2:
        return True
    else:
        return False

def NOR(A, B):
    buf = A + B
    if buf == 0:
        return True
    else:
        return False


def XOR(A, B):
    buf = A + B
    if buf == 1:
        return True
    else:
        return False


def IMP(A, B):
    buf = A + B
    if B == False and buf == 1:
        return False
    else:
        return True


def EQ(A, B):
    buf = A + B
    if buf == 2 or buf == 0:
        return True
    else:
        return False


def table(lmd):
    # 引数 = lambda a, b: AND(a, OR(a, b))
    # 戻り値 = [True, True, True],
    #          [True, False, True],
    #          [False, True, False],
    #          [False, False, False]
    result = []
    # lmd.a = 1
    # lmd.b = 1
    result += [[lmd(True, True), lmd(True, True), lmd(True, True)]]
    result += [[lmd(True, True), lmd(False, False), lmd(True, True)]]
    result += [[lmd(False, False), lmd(True, True), lmd(False, False)]]
    result += [[lmd(False, False), lmd(False, False), lmd(False, False)]]

    return result

