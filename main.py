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

import handlers


def main():
    argv: list[str] = sys.argv

    if len(argv) == 1:
        handlers.program_help()
        return

    if argv[1] == "--help":
        handlers.program_help()
        return
    
    command: handlers.Sort_args = handlers.Sort_args(argv)

    command.compile_program()

    if ('R' in command.options) or ('run' in command.options) or ('r' in command.options):
        command.run_binary()
    
    if ('PB' in command.options) or ('printbin' in command.options) or ('pb' in command.options) or ('p' in command.options):
        sys.stdout.buffer.write(command.get_binary())
    
    if (not ('K' in command.options)) or (not ('keep' in command.options)) or ('k' in command.options):
        command.remove_exec()

    if ('C' in command.options) or ('command' in command.options) or ('c' in command.options):
        print(command.compiler_name, command.path, *command.compiler_options)

if __name__ == "__main__":
    main()

