def CalcExpression():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(" ")
    if y == "+":
        return float(int(x)+int(z))
    elif y == "-":
        return float(int(x)-int(z))
    elif y == "*":
        return float(int(x)*int(z))
    elif y == "/":
        if int(z) == 0:
            return "cannot divide by 0"
        else:
            return float(int(x)/int(z))
print("%.1f" % CalcExpression())
