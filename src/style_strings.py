from __future__ import annotations
from termcolor import colored

comprun_name: str = colored("comprun:", attrs=["bold"])

error_label: str = colored("error:", "red", attrs=["bold"])

warning_label: str = colored("warning:", "magenta", attrs=["bold"])

def bolded(inp: str) -> str:
    return colored(inp, attrs=["bold"])

def bquoted(inp: str) -> str:
    return f"'{bolded(inp)}'"
