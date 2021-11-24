
#  ini inputan benar
def funcsomething(x):
    """
    Multiline mode
    """
    if x == 0:
        x += 6
        return 0
    elif x * 5 == 1:
        x = 44
        if True:
            return True
        else:
            return 2
    elif (x ==5*4):
        return funcsomething(x + 8)
    else:
        return (0)

