# coding = utf-8


import argparse
import json
import os
import importlib
import sys

class logger:
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

log = logger('BinTool')

def import_utilities(path, module):
    utilities = {}
    json_utilities_file = "Utilities.json"
    json_utilities = None
    old_cwd = os.getcwd()
    os.chdir(path)
    sys.path.append(os.getcwd())
    os.chdir(os.path.join(os.getcwd(), module))
    try:
        with open(json_utilities_file) as f:
            json_utilities = json.load(f)
        if 'utilities' not in json_utilities:
            log.error('lack of "utilities" field, Utility.json')
            return utilities
        for utility in json_utilities['utilities']:
            if 'name' not in utility:
                log.error('lack of "name" field, Utility.json')
                continue
            if  'path' not in utility:
                log.error('lack of "path" field, Utility.json')
                continue
            submodule_path = module+'.'+utility['path']
            spec = importlib.util.find_spec(submodule_path)
            if spec == None:
                log.error(f'path {utility['path']} not exists, Utility.json')
                continue
            log.debug(f'importing {utility["name"]}, path {utility["path"]}')
            lib = importlib.import_module(submodule_path)
            utilities[utility['name']] = lib
        return utilities
    finally:
        os.chdir(old_cwd)

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
    utilities = import_utilities("./", "Utilities")
    bt = BinTool(utilities)
