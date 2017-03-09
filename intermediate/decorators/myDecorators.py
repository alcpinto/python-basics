from functools import wraps


def add_wrapping(style=''):
    def wrapping(item):
        @wraps(item) # to return the name of original function
        def wrapped_item():
            return 'a {} wrapped up box of {}'.format(style, str(item()))
        return wrapped_item
    return wrapping


@add_wrapping(style='fake')
def new_gpu():
    return 'a new Tesla P100 GPU!'


print(new_gpu())
print(new_gpu.__name__)
