"""
Static method knows nothing about the class and just deals with the parameters
Class method works with the class since its parameter is always the class itself.
"""


class Singleton:
    # static variables
    __unique_instance = object()
    __count = 0  # count would be consistent among all instantiation of the singleton

    def __init__(self, instance):
        assert(instance == Singleton.__unique_instance), "objects must be created using Singleton.get_instance"

    @classmethod
    def get_instance(cls):
        if isinstance(cls.__unique_instance, Singleton):
            print("instance created before")
            return cls.__unique_instance
        print("first time instantiation")
        cls.__unique_instance = Singleton(cls.__unique_instance)
        return cls(cls.__unique_instance)

    @classmethod
    def increase(cls):
        cls.__count += 1

    @classmethod
    def get_count(cls):
        return cls.__count


if __name__ == '__main__':
    sg1 = Singleton.get_instance()
    sg2 = Singleton.get_instance()
    sg3 = Singleton.get_instance()

    sg1.increase()
    sg2.increase()
    sg3.increase()
    sg1.increase()

    print(sg1.get_count(), sg2.get_count(), sg3.get_count())



