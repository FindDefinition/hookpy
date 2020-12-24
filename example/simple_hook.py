import functools
import inspect
import json
import threading
import time
from pathlib import Path
from typing import Union

import hookpy
from hookpy import compat, funcid

_LOCK = threading.Lock()

_FUNC_TRACES = []

class FuncTraceSave(hookpy.Hook):
    def __init__(self, save_path: Union[Path, str]):
        self.impl = None
        self.save_path = Path(save_path)

    def create_impl(self, func_meta: funcid.FuncMetadata, func) -> bool:
        isasyncgen = False or (compat.Python3_6AndLater and inspect.isasyncgenfunction(func))
        if not inspect.iscoroutinefunction(
                func) and not isasyncgen:
            func_id = func_meta.func_id
            @functools.wraps(func)
            def wrapped(*args, **kw):
                with _LOCK:
                    _FUNC_TRACES.append((time.time(), func_id))
                return func(*args, **kw)
            self.impl = wrapped
            return True
        return False

    def get_impl(self):
        return self.impl

    def enabled(self) -> bool:
        # called before run this hook. 
        # this hook may not run if return True.
        return True

    def is_enabled(self, enabled: bool):
        # called if run this hook
        return

    def handle_exit(self):
        with _LOCK:
            with self.save_path.open("w") as f:
                json.dump(_FUNC_TRACES, f)
