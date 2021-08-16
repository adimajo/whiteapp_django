"""
Singleton module
"""


class Singleton(type):
    """
    Design pattern used to ensure the unity of a class.

    This class basically overrides the default behavior of the constructor to always return the same pointer.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
