def is_palindrome(x):
    if x == x[::-1]:
        #print(x)       そのまま吐
        #print(x[::-1]) 逆順で吐
        return True
    else:
        return False
