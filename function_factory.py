def own_print(x):
    def inner(y):
        return x + " it's " + y
    return inner