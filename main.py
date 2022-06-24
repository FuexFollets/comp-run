# Simple script for compiling, running, and deleting the binary for any compiler
# Can output the binary to STDOUT

# Arguements:
# comprun <mode> <path> <compiler> [compiler flags... ]
# mode:
#   -r Only compiles and runs the script. Deletes binary

#   -p Compiles and prints binary to STDOUT

#   -k Keeps binary

#   arguements -arg1arg2arg3 can be used rather than -arg1 -arg2 -arg3

from __future__ import annotations
import sys
from os import system

from click import command

import handlers


def main():
    argv: list[str] = sys.argv
    
    print(argv)

    if len(argv) == 1:
        handlers.program_help()
        return

    if argv[1] == "--help":
        handlers.program_help()
        return
    
    command: handlers.Sort_args = handlers.Sort_args(argv)

    command.compile_program()

    if 'r' in command.options:
        command.run_binary()
    
    if 'p' in command.options:
        print(command.get_binary())
    
    if not ('k' in command.options):
        command.remove_exec()


if __name__ == "__main__":
    main()

