class CallbackTest:
    def call(self,fn,*args,**kwargs):
        print("*"*15)
        fn(*args,**kwargs)
def callback(tag):
    print(tag*5)
if __name__=='__main__':
    call=CallbackTest()
    call.call(callback,'&')