import math
def roots(a, b, c):
    discriminante = ((b**2)-4*a*c)
    if discriminante >0:
        x1= (((-b)+math.sqrt(discriminante))/(2*a))
        x2= (((-b)-math.sqrt(discriminante))/(2*a))
        return f"({x1}, {x2})"
    elif discriminante ==0:
        x1= (((-b)+math.sqrt(discriminante))/(2*a))
        return f"({x1})"
    else: 
        return f"( )"
def value_y(a, b, c, x):
    y=a*(x**2)+b*x+c
    return y
def to_string(a, b, c):
    if a==0 or b==0 or c==0:
        if a==0:
           if b==0:
               if c==0:
                   return f"f(x) = 0"
               else:
                   return f"f(x) = {c}"
           else:
                if c==0:
                   return f"f(x) = {b} * X"
                else:
                   return f"f(x) = {b} * X + {c}"
        else:
            if b==0:
                if c==0:
                    return f"f(x) = {a} * X^2"
                else:
                    return f"f(x) = {a} * X^2 + {c}"
            else:
                return f"f(x) = {a} * X^2 + {b} * X"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    return (f"f(x) = {a} * X^2 + {b} * X + {c}")
def derivation(a, b, c):
    if a==0 or b==0:
        if a==0:
            if b==0:
                return f"f'(x) = 0"
            else:
                return f"f'(x) = {b}"
        else:
                aderi=a*2
                return f"f'(x) = {aderi} * X"
    else:
        aderi=a*2
        return f"f'(x) = {aderi} * X + {b}"
