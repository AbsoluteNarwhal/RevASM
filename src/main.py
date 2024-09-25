import sys
import os
import help
import vars
import hexdump
import info_common
import elf

"""
Dual file extensions:

No extension: Unix executable or text file
.bin: Unix executable or generic binary
"""

def main():
    filetype = None
    args = sys.argv

    # Input error checks, --help and --version
    if len(args) > 4:
        print("Error: Too many arguments")
        return
    if args[1] == "--help" or args[1] == "-h":
        if len(args) == 2:
            help.select("")
            return
        help.select(args[2])
        return
    if args[1] == "--version" or args[1] == "-v":
        print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal\n")
        return
    if len(args) < 3:
        print("Error: No file provided")
        return
    if not os.path.exists(args[2]):
        print(f"Error: File '{args[2]}' does not exist")
        return

    # Hexdump
    if args[1] == "hexdump":
        with open(args[2], "rb") as file:
            hexdump.hex_format(file.read())
        return
    
    # Resolve file type
    _, ext = os.path.splitext(args[2])
    with open(args[2], "rb") as file:
        file_contents = file.read()
        if file_contents[:4] == b"\x7FELF" and (ext in info_common.ELF_EXTENSIONS or ext == ""):
            filetype = "ELF"
            if ext == "": ext = "$ELF_NOEXT"
        elif file_contents[:2] == b"MZ":
            filetype = "PE"
        else:
            filetype = "TEXT"
            if ext == "": ext = "$TXT_NOEXT"
    
    # Do file-specific commands
    match filetype:
        case "ELF":
            if args[1] == "info":
                if len(args) < 4: 
                    elf.select_elf_info(args[2], "")
                    return
                elf.select_elf_info(args[2], args[-1])
                return
        case "PE":
            print("PE not supported yet")
        case "TEXT":
            print("Text not supported yet")

main()