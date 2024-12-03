# coding = utf-8

class Logger:
    def __init__(self, prefix, truncate_length=32):
        self.prefix = prefix
        self.truncate_length = truncate_length
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
    def limit(self, string, max_length = None):
        if max_length is None:
            max_length = self.truncate_length
        if len(string) > max_length:
            return string[:max_length-3] + "..."
        else:
            return string