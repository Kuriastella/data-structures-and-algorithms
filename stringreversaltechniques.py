str = "Greetings"

#slicing method
def reverse_slicing(s): 
    return s[::-1]
print(reverse_slicing(str))
 

#reversed() + join() method
def reverse_builtin(s):
     return''.join(reversed(s))
print(reverse_builtin(str)) 

#Loop method
def reverse_loop(s): 
    result = "" 
    for char in s: 
        result = char + result 
        return result
print(reverse_loop(str))

#Recursion Method
def reverse_recursive(s):
    if len(s) <= 1: 
        return s 
        return reverse_recursive(s[1:]) + s[0]
print(reverse_recursive(str)) 

