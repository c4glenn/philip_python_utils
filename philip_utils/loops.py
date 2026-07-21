from typing import Iterator
import enlighten

def progress_bars(itterator, *args, **kwargs):
    global __progress_manager_philip__
    try: 
        __progress_manager_philip__ # pyright: ignore[reportUnboundVariable, reportUnusedExpression]
    except NameError as e:
        __progress_manager_philip__ = enlighten.get_manager()
    
    man = __progress_manager_philip__
    try:
        it_len = len(itterator) # pyright: ignore[reportArgumentType]
    except:
        it_len = None
    
    try:
        ctr = None
        for i, e in enumerate(itterator):
            if i == 0:
                ctr = man.counter(*args, **{**dict(leave = False, total = it_len), **kwargs})

            yield e
            ctr.update() # pyright: ignore[reportOptionalMemberAccess]
    finally:
        if ctr is not None:
            ctr.close()
    
    