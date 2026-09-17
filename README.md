# Welcome to CatDot-py! 🐈/🐟🛑⚡
### What is CatDot-py? 🐈/🐟🛑⚡

CatDot-py is the official rebundle and successor of `Looprlib`, `Looprlib-Mit`, `SeaKrait`, `StopSign`.. \
All future updates and new features will be released exclusively under the CatDot-py name.\
CatDot-py was made to bundle all my packages to make production easier.\
Everything from the originals are still here.\
This is the only version that will continue to update from now on.

CrackDown (Never Released) - Make code very simple to write \
SeaKrait - Adds various functions \
StopSign (Never Released) - Adds stop functions to python \



## Features

- **Simplified Math Utilities:** Quick logical and evaluation helper functions.
- **Cross Ability:** Being able to cross use function between multiple modules.
- **Lightweight & Fast:** Zero heavy third-party dependencies.
- **Cutting Down Text Clutter:** This package seems "Useless" at first but it is a life saver at simplyfing anoying to write out code





### Use Case (1)
You could use this to test positivity of an number and get a result with this:

Here is the positivity function.

    def positivity(i,pos,neg,zero):
        if i > 0:
            return pos
        elif i < 0:
            return neg
        else:
            return zero

### Example in package
    
    import CBpy.SeaKrait as seakr
    print(seakr.seamath.positivity(100,21,32,123))

#### if 100 is positive the result is 21
#### if 100 is negative the result is 32
#### if 100 is equal to 0  the result is 123

#### in this case the function will print 21 to the terminal!

This function is good becuase it lowers the count of characters to type to only a single runnable function. \ 
96 characters to 57.

### Use Case (2)
You could use this to import single use functions:

Here is the function.

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

### Example in package
    
    import CBpy.SeaKrait as seakr
    print(seakr.seaute.abmf("builtins", "print", "hi" ))

#### in this case the function will print hi to the terminal!

This function is good becuase people don't have to import functions they're gonna use once


### Other Material
SeaKrait - https://github.com/Orbits-Studio-Programing/SeaKrait \
Anaconda port will come soon :)

#### Originals
Looprlib - https://pypi.org/project/Looprlib/ \
Looprlib MIT - https://pypi.org/project/Looprlib-MIT/
