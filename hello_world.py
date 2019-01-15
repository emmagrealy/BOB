def hello(name=''):
    if not name:
        say = "Hello, World!"
    else:
        say = "Hello, " + name + "!"
    return say