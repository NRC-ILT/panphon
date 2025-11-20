"""
Minimal stub to simulate importlib.resources.files for Python 3.8
"""
try:
    from importlib.resources import files
except ImportError:
    from pathlib import Path
    def files(module):
        if module != "panphon":
            raise NotImplementedError()
        return Path(__file__).parent


__all__ = [files]
