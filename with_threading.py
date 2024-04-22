import threading
import time
import re

str_exp = ["6 + 81 / 9 * 4 * 3 - 7", "8 - 5 + 4 * 7 / 2", "1+2*3+450+42/2+3","60+48/2*5", "27 - 12 / 4 * 4 + 5"]

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b
    
def add(a,b):
    return a + b 
    
def subtract(a,b):
    return a - b
    
def check_exp(str_exp):
    start_time = time.time()
    matches = re.findall(r"(-?[\d.]+)|([*\/+-])", str_exp)
    operands = [float(x[0]) for x in matches if x[0]]
    operators = [x[1] for x in matches if x[1]]
    
    calculator = {"*":multiply, "/":divide, "+":add, "-":subtract}

    
    i = 0 
    while i < len(operators):
        if operators[i] in ["*", "/"]:
            a, b = operands[i], operands[i + 1]
            result = calculator[operators[i]](a,b)
            operands[i] = result
            del operands[i + 1]
            del operators[i]
            i -= 1 
        i += 1 
        
        
    result = operands[0]
    for op, operand in zip(operators, operands[1:]):
        result = calculator[op](result, operand)
        
    end_time = time.time()
    print(f"Result: {result}, Time taken: {end_time - start_time:.6f} seconds.")
    
    
threads = []
for str_exp in str_exp:
    t = threading.Thread(target=check_exp, args=(str_exp,))
    threads.append(t)
    t.start()
    
    
for t in threads:
    t.join()
                




