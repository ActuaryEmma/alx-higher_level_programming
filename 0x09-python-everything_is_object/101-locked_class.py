#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attr, value):
        if not hasattr(self, attr) and attr != 'first_name':
            raise AttributeError(f"'{self.__class__.__name__}' object\
has no attribute '{attr}'")
        else:
            self.__dict__[attr] = value
