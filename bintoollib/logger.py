# coding = utf-8

class Logger:
    def __init__(self, prefix):
        self.prefix = prefix
    def print(self, *args, **kwargs):
        print(f"[{self.prefix}]:", *args, **kwargs)
    def error(self, *args, **kwargs):
        print(f"[{self.prefix}|error]:", *args, **kwargs)
    def warning(self, *args, **kwargs):
        print(f"[{self.prefix}|warning]:", *args, **kwargs)
    def info(self, *args, **kwargs):
        print(f"[{self.prefix}|info]:", *args, **kwargs)
    def debug(self, *args, **kwargs):
        print(f"[{self.prefix}|debug]:", *args, **kwargs)
    def critical(self, *args, **kwargs):
        print(f"[{self.prefix}|critical]:", *args, **kwargs)