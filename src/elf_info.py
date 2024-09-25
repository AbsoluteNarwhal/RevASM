import os
from time import gmtime, strftime
import info_common

def get_all(file):
    print("File information:")
    info_common.get_type(file)
    info_common.get_size(file)
    info_common.get_ctime(file)
    info_common.get_atime(file)
    info_common.get_mtime(file)
    print()
    print("Binary information:")
    get_abi(file)
    get_os(file)
    get_iset(file)
    get_endian(file)

def get_abi(file):
    print("    Binary ABI format: Executable and Linkable Format (ELF)")

def get_os(file):
    print("    Target system: ")

def get_iset(file):
    print("    Target instruction set: ")

def get_endian(file):
    print("    Endianness: ")