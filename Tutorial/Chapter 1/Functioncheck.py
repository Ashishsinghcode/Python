def example(k):
    
    if k > 0 :
        
        result = k+ example(k-1)
        print(k,result)
    else:
        result = 0
    return result


example(4)

# def example(x):
#     pass
# print(example(5))