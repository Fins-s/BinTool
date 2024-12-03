# coding = utf-8

import ast
import argparse
import os
import importlib
import sys
import yaml

from bintoollib import Logger
from bintoollib import Env

class BinTool:
    def __init__(self, utilities, logger):
        self.log = logger       # logger
        self.data = []             # file data array       [byte, byte, byte, ...]
        self.env = Env()           # environment variables  {"env_name", data}
        self.utilities = utilities # utilities {"utilitie_name", python_lib}
    def define(self, name, expr):
        try:
            data = self.env.exec(expr)
            self.env.define(name, data)
        except Exception as e:
            self.log.error(f'{e}')
        finally:
            self.log.print(f'Var: {{\'{self.log.limit(name)}\': "{self.log.limit(expr)}" = {self.log.limit(str(data))}}}')
    def build(self, yaml_project):
        return
    def astExe(self, ast):
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
            code = None
            with open(filepath, 'r') as f:
                code = f.read()
            try:
                ast.parse(code)
            except SyntaxError:
                log.error(f'{module_name} syntax error')
                continue
            module_env = {'global_env': {}, 'local_env': {}}
            exec(code, module_env['global_env'], module_env['local_env'])
            utilities[module_name] = module_env
    return utilities

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='BinTool', description='An useful tool for binary file')
    parser.add_argument('output',  help='output file name')
    parser.add_argument('-v', '--version', action='version', version='BinTool 1.0')
    parser.add_argument('-p', '--project', default='project.yaml' , help='project ".yaml" file')
    parser.add_argument('-d', '--define', action= 'append', nargs=2, metavar=('NAME', 'EXPR'), help='define environment variable')
    args = parser.parse_args()
    log.print('BinTool 1.0')

    log.print('-----Utilities imported-----')
    utilities = import_all_utilities("./Utilities")
    for key, value in utilities.items():
        log.print(f"{key}")

    log.print(f'-----Load project -----')
    project_path = args.project
    if os.path.exists(project_path):
        log.print(f'Project file "{project_path}" found')
    else:
        log.error(f'Project file "{project_path}" not found')
        exit(1)
    with open(project_path, 'r') as project_file:
        project = yaml.safe_load(project_file)

    
    bt = BinTool(utilities, log)

    log.print('-----Environment variable per define -----')
    if args.define:
        for var in args.define:
            bt.define(var[0], var[1])

    log.print(f'-----Building-----')
    bt.build(project)
