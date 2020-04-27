# def merry(x):
#     print(x)
#
# merry('berry')

# def klass(y):
#     print(y)
#     klass(y)
#
# klass(15)


def multiplay(x,y):
    result = x * y
    if result > 100:
        return result

    return multiplay(result,y)


print(str(multiplay(1, 10)))

