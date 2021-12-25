
def make_re(f,x):
    def re(n):
        if n==1:
            return f(x)
        else:
            return f(re(n-1))
    return re
incr=make_re(lambda x:x+1,1)
print(incr(2))