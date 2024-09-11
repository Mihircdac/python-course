
var = 10 # global

def f(inp_f):
    var = 20 # enclosed to f1 and local to f
    
    def get_var_from_f():
        return var
    
    def f1(inp_f1):
        # global var # please use global scpoed variable 
        
        var = 30 # local to f1
        # nonlocal var # please use enclosed scope variable
        # print(inp_f1)
        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        print("local to f1:",var)
        print("enclosed to  f1:", get_var_from_f())
        print("globals to  f1:", globals()['var'])
    f1(100)    
    
f(10)
