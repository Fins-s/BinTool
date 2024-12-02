# coding = utf-8

class Env(dict):
    """
    exper execute environment
    """         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def define(self, name:str, value:any):
        """
        define a variable, if the variable already exists, raise ValueError

        Args:
            name(str): variable name
            value(any): variable value

        Returns:
            None
        """
        if name in self:
            raise KeyError(f"{name} already defined")
        else:
            self[name] = value
    def undefine(self, name:str):
        """
        undefine a variable, if the variable does not exist, raise KeyError

        Args:
            name(str): variable name

        Returns:
            None
        """
        if name not in self:
            raise KeyError(f"{name} not defined")
        else:
            del self[name]
    def exec(self, string:str):
        """
        execute a string with variable substitution

        Args:
            string(str): string to be executed

        Returns:
            any: the result of the execution
        """
        var_string = ""
        ast_string = ""
        i = 0
        while i < len(string):
            if string[i] == '$':
                i += 1
                # var name can be alphanumeric or underscore
                while (i < len(string)) and (string[i].isalnum() or string[i] == '_'):
                    var_string += string[i]
                    i += 1
                if var_string not in self:
                    raise KeyError(f"{var_string} not defined")
                else:
                    ast_string += f"self['{var_string}']"
            else:
                ast_string += string[i]
                i += 1
        return eval(ast_string)