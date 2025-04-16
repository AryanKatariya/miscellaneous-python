# def print_out(a):
#     print("Outer:{}".format(a))
    
#     def print_in():
#         print("Inner:{}".format(a))
    
#     print_in()

# print_out("testing")

def print_outV2(a):
    print("Outer:{}".format(a))
    
    def print_inV2():
        print("Inner:{}".format(a))
        
    return print_inV2

test2 = print_outV2("testing2")
del print_outV2

print(test2())