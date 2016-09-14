class UnitTest(object):
    def __init__(self, func, args, kwargs, res):    # make test
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.res = res


    def __call__(self):   
        try:
            print "num_rechecks", self.kwargs['num_rechecks']
            ret = self.func(self.args[0], self.args[1], self.kwargs['num_rechecks'])
        except:
            return False
        return ret == self.res




