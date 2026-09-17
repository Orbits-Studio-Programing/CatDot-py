try:
    TEST = "PaSsWoRd"  

    from . import KEYKEYKEYKEY
    KEYKEYKEYKEY.Key = TEST
    KEYKEYKEYKEY.Key = ""

    from . import CrackDown 
    from . import SeaKrait 
    from . import StopSign 
    
    __all__ = ["CrackDown", "SeaKrait", "StopSign"]
except ModuleNotFoundError:
    __all__ = []
except AttributeError:
    __all__ = []
except ImportError:
    __all__ = []

__VERSION__ = "26.6.0"