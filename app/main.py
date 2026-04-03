from typing import Callable, Any


def cache(func: Callable) -> Any:
    storage_of_data = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs))
        if key in storage_of_data:
            print("Getting from cache")
            return storage_of_data[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        storage_of_data[key] = result
        return result

    return wrapper
