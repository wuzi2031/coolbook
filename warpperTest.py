import functools,time
class DefWapper:

    def timeit1(func):
        @functools.wraps(func)
        def wapper(*args,**kwargs):
            start=time.clock()
            func(*args,**kwargs)
            end=time.clock()
            print("time:"+str(end-start))
        return wapper

    def timeit2(lev='info'):
        def timeit1(func):
            @functools.wraps(func)
            def wapper(*args, **kwargs):
                start = time.clock()
                func(*args, **kwargs)
                end = time.clock()
                print('lev:'+lev+" "+func.__name__)
                print("time:" + str(end - start))
                # return func(*args,**kwargs)
            return wapper
        return timeit1