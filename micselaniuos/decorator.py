def me_DICAROTORer(func):
    def wrapper(*args, **kwargs):
        print("*****************************************************")
        result = func(*args, **kwargs)
        print("*****************************************************")
        return result
    return wrapper