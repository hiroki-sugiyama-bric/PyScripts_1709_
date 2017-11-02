import numpy as np

def dict_recursive(func):
    def wrapper(d, *args, **kwargs):
        if not isinstance(d, dict):
            return d

        for k, v in d.items():
            if isinstance(v, dict):
                d[k] = wrapper(v, *args, **kwargs)
            else:
                d[k] = func(v, *args, **kwargs)

        return d

    return wrapper




