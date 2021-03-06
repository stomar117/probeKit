from typing import Union
from types import FunctionType
from modules.util.CommandUtils._Commands import Commands
from config import valid_modules
from modules.util.CommandUtils.ReturnStructure import RetObject


class CreateCommand:
    """
    Required Keyword Arguments:
    - arguments -> list[str]
    - option_dict -> dict[str]
    - aliases -> dict[str]
    - macros -> dict[str]
    - activated_module_list -> list[str] #list of active modules activated by the use command
    - module -> str currently activated module
    - histfile -> location of history file
    """
    def __init__(self, **kwargs) -> None:
        self.arguments = kwargs.get('arguments')
        self.option_dict = kwargs.get('option_dict')
        self.aliases = kwargs.get('aliases')
        self.macros = kwargs.get('macros')
        self.activated_module_list = kwargs.get('activated_module_list')
        self.module = kwargs.get('module')
        self.histfile = kwargs.get('histfile')

    def create_struct(self) -> RetObject:
        Struct: RetObject = RetObject()
        Struct.option_dict = self.option_dict
        Struct.aliases = self.aliases
        Struct.macros = self.macros
        Struct.activated_module_list = self.activated_module_list
        Struct.module = self.module
        Struct.histfile = self.histfile
        return Struct
    
    def run(self, command: str) -> Union[RetObject, None]:
        if command in Commands:
            ReturnObject = _RunCommand(command)(self.arguments, self.create_struct())
            ReturnObject.command_found = True
            return ReturnObject
        else:
            ReturnObject = RetObject()
            ReturnObject.command_found = False
            ReturnObject.exit_code = 1
            return ReturnObject


class _RunCommand:
    def __init__(self, command: str):
        self.command = command
    
    def __call__(self, arguments: list[str], ReturnObject: RetObject) -> RetObject:
        command = Commands.get(self.command)
        if isinstance(command, FunctionType):
            return command(arguments, ReturnObject)
        else:
            command_object = command(arguments, ReturnObject)
            return command_object.run()