#https://medium.com/better-programming/every-python-programmer-should-know-the-not-so-secret-threadpool-642ec47f2000
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    res = []
    with Pool(5) as p:
        res.append(p.map(f, [1, 2, 3]))

    print(res)