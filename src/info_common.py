from time import gmtime, strftime
import os

ELF_EXTENSIONS = {
    "$ELF_NOEXT": "Unix executable file",
    ".so": "Unix shared object (Shared library)",
    ".o": "C object file (Static library)",
    ".bin": "Unix executable file",
    ".elf": "ELF file",
    ".out": "Unix executable file",
    ".ko": "Linux kernel module",
    ".mod": "GRUB module"
}

TEXT_EXTENSIONS = {
    "$TXT_NOEXT": "Text file",
    ".txt": "Text file",
    ".md": "Markdown text file",
}

def format_file_size(size_bytes):
    if size_bytes < 1000:
        return f"{size_bytes}B"
    if size_bytes < 1000000:
        return f"{size_bytes/1000}KB"
    if size_bytes < 1000000000:
        return f"{size_bytes/1000000}MB"
    return f"{size_bytes/1000000000}GB"

def get_meta(file, ext):
    print("File metadata information:")
    get_type(ext)
    get_size(file)
    get_ctime(file)
    get_atime(file)
    get_mtime(file)

def get_type(ext):
    if ext == "$ELF_NOEXT":
        print("    Type: Unix executable file")
    elif ext == "$TXT_NOEXT":
        print("    Type: Text file")
    else: 
        print(f"    Type: {ELF_EXTENSIONS[ext]} ({ext})")

def get_size(file):
    print(f"    Size: {format_file_size(os.path.getsize(file))}")

def get_atime(file):
    print(f"    Last accessed: {strftime('%Y-%m-%d %H:%M:%S', gmtime(os.path.getatime(file)))}")

def get_ctime(file):
    if os.name == "nt": print(f"    Created: {strftime('%Y-%m-%d %H:%M:%S', gmtime(os.path.getctime(file)))}")
    else: print(f"    Last modified metadata: {strftime('%Y-%m-%d %H:%M:%S', gmtime(os.path.getctime(file)))}")

def get_mtime(file):
    print(f"    Last modified: {strftime('%Y-%m-%d %H:%M:%S', gmtime(os.path.getmtime(file)))}")