from __future__ import annotations
from distutils.errors import CCompilerError
from typing import Any
import os
import sys
import subprocess
import random
import string
import usr_exceptions as ue

def generate_random_name() -> str:
    return "temp_" + ''.join(random.choices(string.digits, k=10))

class Sort_args:
    def __init__(self, argv: list[str]):
        self.options: set[str] = set()
        self.compiler_options: list[str] = []
        self.compiler_name: str = ""
        self.path: str = ""
        self.exec_name: str = generate_random_name()
        
        arg_values = iter(argv[1:])

        unsplit_options: str = "" 
        for arg in arg_values:
            if arg.startswith('-') == False:
                self.path = arg
                break
            
            if arg != "-n":
                unsplit_options += arg
            else:
                self.exec_name = next(arg_values)


        if not os.path.exists(self.path):
            sys.stderr.write(f"comprun: error: unable to find file at path '{self.path}'")
            raise RuntimeError("Invalid file path")

        self.options = {*unsplit_options.split('-')}

        try:
            self.compiler_name = next(arg_values)
        except:
            sys.stderr.write("comprun: error: compiler name is nonexistent")
            raise RuntimeError("Compiler name invalid")

        if len(self.options) == 1:
            self.options.add('r')

        self.compiler_options = [*arg_values]
        

    def get_compile_command(self) -> list[str]:
        return [self.compiler_name, "-o", self.exec_name, self.path, *self.compiler_options]
        # return f"{self.compiler_name} -o {self.name} {self.path} {self.compiler_options}"

    def get_exec_path(self) -> str:
        dir_path = self.path.split('/')[:-1]
        return "./" + '/'.join(dir_path + [self.exec_name])

    def compile_program(self) -> None:
        try:
            subprocess.run(self.get_compile_command())
        except:
            sys.stderr.write(f"comprun: error: unrecognized compiler '{self.compiler_name}'\n")
            raise RuntimeError("Trouble compiling")


    def remove_exec(self) -> None:
        os.remove(self.get_exec_path())

    def get_binary(self) -> str:
        with open(self.get_exec_path(), mode="rb") as exec_file:
            return exec_file.read()
    
    def run_binary(self) -> subprocess.CompletedProcess:
        try:
            return subprocess.run([self.get_exec_path()])
        except:
            pass
            # sys.stderr.write(f"comprun: error: trouble compiling '{' '.join(self.get_compile_command())}'\n")

def program_help() -> None:
    print('''
        
    ''')