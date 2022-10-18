def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    x=0
    y=0
    if a>0:
        x+=1
    else :
        y+=1
    if b>0:
        x+=1
    else :
        y+=1
    if c>0:
        x+=1
    else :
        y+=1
    if x>y:
        return "there are a lot of positive numbers"
    if y>x:
        return "there are a lot of negative numbers"
    
print(main(7,8,-8))
