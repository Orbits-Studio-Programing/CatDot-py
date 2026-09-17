def abmf(module_input, func, *args, **kwargs):   

    import importlib
    import types

    if isinstance(module_input, str):
        try:
            module_obj = importlib.import_module(module_input)
        except ImportError as e:
            raise ValueError(f"Module '{module_input}' could not be imported.") from e
    elif isinstance(module_input, types.ModuleType):
        module_obj = module_input
    else:
        raise TypeError("module_input must be a string or a module object.")
    name = func.__name__ if callable(func) else str(func)

    if hasattr(module_obj, name) and not name.startswith('_'):
        target_func = getattr(module_obj, name)

        if callable(target_func):
            return target_func(*args, **kwargs)

    raise ValueError(f"'{name}' is not a valid callable in module '{getattr(module_obj, '__name__', module_input)}'")



def full_file(exec_func, target, towa=None):
    if exec_func=="w":
        with open(target, "w") as file:
            if towa==None:
                raise ValueError("inappropriate string for exec_func " + '"' + "w" + '"')
            else:
                return file.write(towa)
    if exec_func=="a":
        with open(target, "a") as file:
            if towa==None:
                raise ValueError("inappropriate string for exec_func " + '"' + "a" + '"')
            else:
                return file.write(towa)
    if exec_func=="r":
        with open(target, "r") as file:
            if towa!=None:
                raise ValueError("string not accepted for exec_func " + '"' + "r" + '"')
            else:
                return file.read(towa)
    else:
        raise ValueError("Invalid exec_func")