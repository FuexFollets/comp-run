from __future__ import annotations
from typing import Any
import os
import subprocess
import random
import string

def generate_random_name() -> str:
    return "temp_" + ''.join(random.choices(string.ascii_lowercase, k=10))

class Sort_args:
    def __init__(self, argv: list[str]):
        self.options: set[str] = set()
        self.compiler_options: list[str] = []
        self.compiler_name: str = ""
        self.path: str = ""
        self.exec_name: str = generate_random_name()
        
        arg_values = iter(argv[1:])

        unsplit: str = "" 
        for arg in arg_values:
            if arg.startswith('-') == False:
                self.path = arg
                break
                
            unsplit += arg

        for val in unsplit:
            if val != '-':
                self.options.add(val)

        self.compiler_name = next(arg_values)

        self.compiler_options = [*arg_values]
    
    def get_compile_command(self) -> list[str]:
        return [self.compiler_name, "-o", self.exec_name, self.path, *self.compiler_options]
        # return f"{self.compiler_name} -o {self.name} {self.path} {self.compiler_options}"

    def get_exec_path(self) -> str:
        dir_path = self.path.split('/')[:-5]
        return dir_path + self.exec_name

    def compile_program(self) -> subprocess.CompletedProcess:
        return subprocess.run(self.get_compile_command())

    def remove_exec(self) -> None:
        os.remove(self.get_exec_path())

    def get_binary(self) -> str:
        with open(self.get_exec_path()) as exec_file:
            return exec_file.read()
    


def program_help() -> None:
    pass