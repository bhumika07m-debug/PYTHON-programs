def process(data,callback):
    res=callback(data)
    print(f"Result: {res}")
def double(x): return x*2
    process(10,double)



