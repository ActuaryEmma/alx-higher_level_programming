#!/usr/bin/python3
if __name__ == '__main__':
    import importlib
    module_name = "hidden_4"
    #  import_module from importlib to import the module name
    hidden = importlib.import_module(module_name)
    #  iterates over the names using dir() and filter out names with __
    names = [name for name in dir(hidden) if not name.startswith("__")]
    #  the names are printed in sorted order
    for name in sorted(names):
        print(name)
