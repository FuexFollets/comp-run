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
import usr_exceptions as ue

def main():
    argv: list[str] = sys.argv

    if len(argv) == 1:
        handlers.program_help()
        return

    if argv[1] == "--help":
        handlers.program_help()
        return

    command: handlers.Sort_args | None.__class__ = None

    try:
        command = handlers.Sort_args(argv)
    except Exception:
        #raise Exception
        return
        # sys.stderr.write(f"comprun: error: error processing comprun arguments. \nuse '--help' for more info.")

    try:
        command.compile_program()
    except:
        sys.stderr.write(f"unable to compile '{' '.join(command.get_compile_command())}' expected at '{command.path}'")
        return

    if ('run' in command.options) or ('r' in command.options):
        try:
            command.run_binary().returncode
        except:
            sys.stderr.write(f"comprun: error: trouble executing file expected at '{command.get_exec_path()}' compiled wtih '{' '.join(command.get_compile_command())}'\n")
            return
    
    if ('printbin' in command.options) or ('pb' in command.options) or ('p' in command.options):
        try:
            sys.stdout.buffer.write(command.get_binary())
        except:
            sys.stderr.write(f"comprun: error: trouble reading file expected at '{command.get_exec_path()}'")

    if not (('keep' in command.options) or ('k' in command.options)):
        command.remove_exec()

    if ('getcommand' in command.options) or ('c' in command.options):
        print(command.get_compile_command())


if __name__ == "__main__":
    main()

