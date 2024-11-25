# coding = utf-8


import argparse
import json
import os
import importlib
import sys

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



class BinTool:
    def __init__(self, utilities):
        self.data = [] # file data array       [byte, byte, byte, ...]
        self.env = {} # environment variables  {"env_name", data}
        self.utilities = utilities # utilities {"utilitie_name", python_lib}
    def handle(self):
        return

log = Logger('BinTool')

def import_all_utilities(directory):
    utilities = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            # if is a directory, recursively import all modules in it
            utilities.update(import_all_utilities(filepath))
        elif filename.endswith('.py') and filename != '__init__.py':
            # if is a python file, import it as a module
            module_name = filename[:-3]
            module_path = os.path.relpath(filepath, os.path.dirname(__file__))
            module_path = module_path.replace(os.sep, '.')
            module_path = module_path[:-3]
            utilitiy = importlib.import_module(module_path)
            utilities[module_name] = utilitiy
    return utilities

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='An useful tool for ".bin" file')
    parser.add_argument('-v', '--version', action='version', version='BinTool 1.0')
    parser.add_argument('-i', '--input', help='input file')
    parser.add_argument('-c', '--config', help='BinTool json config file')
    parser.add_argument('-o', '--output', help='output file')
    log.print('BinTool 1.0')
    log.error('BinTool 1.0')
    log.warning('BinTool 1.0')
    log.info('BinTool 1.0')
    log.critical('BinTool 1.0')
    
    utilities = import_all_utilities("./Utilities")
    log.print('-----Utilities imported-----')
    for key, value in utilities.items():
        log.print(f"{key}: {value}")
    bt = BinTool(utilities)
