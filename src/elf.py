import elf_info
import vars
import info_common

def select_elf(args, ext):
    if args[1] == "info":
        if len(args) < 4: 
            select_elf_info(args[2], "", ext)
        else:
            select_elf_info(args[2], args[-1], ext)

def select_elf_info(file, infotype, ext):
    print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal")
    print()
    if not infotype in ["", "--meta"]: print("File: " + file)
    match infotype:
        case "": elf_info.get_all(file, ext)
        case "--meta": info_common.get_meta(file, ext)
        case "--type": info_common.get_type(ext)
        case "--size": info_common.get_size(file)
        case "--atime": info_common.get_atime(file)
        case "--ctime": info_common.get_ctime(file)
        case "--mtime": info_common.get_mtime(file)
        case "--abi": elf_info.get_abi()
        case "--os": elf_info.get_os(file)
        case "--iset": elf_info.get_iset(file)
        case "--endianness": elf_info.get_endian(file)
        case _: print(f"Error: File data '{infotype}' is not available for this file type.")
    print()

def elf_dependencies(file):
    pass

def elf_exports(file):
    pass