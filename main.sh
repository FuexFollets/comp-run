#!/bin/bash

# Simple script for compiling, running, and deleting the binary for any compiler
# Can output the binary to STDOUT

# Arguements:
# comprun <mode> <path> <compiler> [compiler flags... ]
# mode:
#   -r Only compiles and runs the script. Deletes binary

#   -p Compiles and prints binary to STDOUT

#   -k Keeps binary

#   use -arg1arg2arg3 rather than -arg1 -arg2 -arg3


rfn=temp$RANDOM$RANDOM

mode=$1

comp_args=${@:4}

compiler=$3

compile_comm="$compiler -o $rfn $comp_args $2"

eval $compile_comm

echo $compile_comm

if grep -q p <<< mode
then
    cat $rfn
fi

if grep -q r <<< mode
then
    ./$rfn
fi

if grep -q k <<< mode
then
    echo removing temp
else
    rm $rfn
fi

