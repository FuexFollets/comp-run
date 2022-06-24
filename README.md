# comp-run

## Description

This is a program for quick tests on compiled programs. It compiles a program with options and a compiler name, and can execute the binary. It may also remove the binary after, or print the executable binary to the standard output.

## Usage

Usage:

    -r, -run
        Executes the compiled binary
    
    -k, -keep
        Keeps the executed file rather than deleting
        Is automatically selected if the '-n' flag is used

    -n <filename>: str
        Names the newly compiled binary as <filename>
        Automatically selects the '-k' flag

    -p, -pb, -printbin
        Writes binary file contents to STDOUT

    -c, -command
        Prints the command used for compilation

    --help
        Provides extended info for usage


