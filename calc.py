def do_math(op, a, b):
    if op == "sum":
        return a + b
    elif op == "multiply":
        return a * b
    elif op == "subtract":
        return a - b
    elif op == "divide":
        if b == 0:
            return "除数不能为0"
        return a / b
    else:
        return "未知的操作"