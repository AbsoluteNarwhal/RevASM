import vars

def select(arg):
    match arg:
        case "": help_general()
        case _: print(f"Error: '{arg}' is not a valid command.")

def help_general():
    print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal")
    print()
    print("Commands:")
    print("    revasm info [file]")
    print("    revasm disassemble [file]")
    print("    revasm hexdump [file]")
    print("    revasm dependencies [file]")
    print("    revasm exports [file]")
    print()
    print("Use revasm --help <command> for more information on command usage.")
    print()

def help_info():
    print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal")
    print()
    print(f"Info (command):")
    print("    revasm info [file]")
    print("    revasm info [file] [flag]")
    print()
    print("Description:")
    print("    Shows non-disassembly information about the file. Information shown depends on the type of file.")
    print("    By default, shows as much information about the file as possible. Pass a flag to get a specific piece of information.")
    print("    Example: $ revasm info foo.exe --size")
    print()
    print("Flags:")
    print("  General")
    print("    --type       : Get file type")
    print("    --size       : Get size of file")
    print("    --ctime      : Creation date (windows) / Date last modified metadata (linux)")
    print("    --atime      : Date last accessed")
    print("    --mtime      : Date last modified")
    print("    --meta       : Dumps all invisible metadata")
    print("  Binaries")
    print("    --abi        : Get ABI/Binary format")
    print("    --os         : Get target operating system")
    print("    --iset       : Get target instruction set")
    print("    --endianness : Get target endianness")
    print()

def help_disassemble():
    print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal")
    print()
    print("Disassemble (command):")
    print("    revasm disassemble [file]")
    print()
    print("Description:")
    print("    Translates ELF/PE x64 binaries into assembly for analysis, along with providing a full hex dump.")
    print()

def help_hexdump():
    print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal")
    print()
    print("Hexdump (command):")
    print("    revasm hexdump [file]")
    print()
    print("Description:")
    print("    Dumps binary data of the file without full disassembly. Can be used on any file type.")
    print()

def help_dependencies():
    print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal")
    print()
    print("Dependencies (command):")
    print("    revasm dependencies [file]")
    print()
    print("Description:")
    print("    Lists shared library dependencies of binary.")
    print()

def help_exports():
    print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal")
    print()
    print("Exports (command):")
    print("    revasm exports [file]")
    print()
    print("Description:")
    print("    Lists exports of library.")
    print()

