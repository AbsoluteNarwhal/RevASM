from time import gmtime, strftime
import info_common

ELF_OS_TARGETS = {
    0x00: "System V (Unix)",
    0x01: "HP-UX",
    0x02: "NetBSD",
    0x03: "Linux",
    0x04: "GNU Hurd",
    0x06: "Solaris",
    0x07: "AIX (Monterey)",
    0x08: "IRIX",
    0x09: "FreeBSD",
    0x0A: "Tru64",
    0x0B: "Novell Modesto",
    0x0C: "OpenBSD",
    0x0D: "OpenVMS",
    0x0E: "NonStop Kernel",
    0x0F: "AROS",
    0x10: "FenixOS",
    0x11: "Nuxi CloudABI",
    0x12: "Stratus Technologies OpenVOS"
}

ELF_ISET_TARGETS = {
    0x03: "x86",
    0x08: "MIPS",
    0x28: "Arm 32-bit",
    0x3E: "AMD x86-64",
}

def get_all(file, ext):
    print("File information:")
    info_common.get_type(ext)
    info_common.get_size(file)
    info_common.get_ctime(file)
    info_common.get_atime(file)
    info_common.get_mtime(file)
    print()
    print("Binary information:")
    get_abi()
    get_os(file)
    get_iset(file)
    get_endian(file)

def get_abi():
    print("    ABI format: Executable and Linkable Format (ELF)")

def get_os(file):
    with open(file, "rb") as nfile:
        content = nfile.read()
        print("    Target system: " + ELF_OS_TARGETS[content[7]])

def get_iset(file):
    with open(file, "rb") as nfile:
        content = nfile.read()
        data = content[18]
        if data in ELF_ISET_TARGETS:
            print("    Target instruction set: " + ELF_ISET_TARGETS[data])
        else:
            print(f"    Target instruction set: Unknown (Unsupported value '{data}')")

def get_endian(file):
    with open(file, "rb") as nfile:
        content = nfile.read()
        if content[5] == 1: print("    Endianness: Little endian")
        elif content[5] == 2: print("    Endianness: Big endian")
        else: print(f"    Endianness: Unknown (Unsupported value '{content[5]}')")