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

PE_EXTENSIONS = {
    ".exe": "Windows executable file",
    ".dll": "Windows dynamic link library (Shared library)",
    ".drv": "Windows driver",
    ".sys": "Windows system file",
    ".efi": "Firmware interface file"
}

TEXT_EXTENSIONS = {
    "$TXT_NOEXT": "Text file",
    ".txt": "Text file",
    ".md": "Markdown text file",
    # Source files
    ".s": "Source code file",
    ".asm": "Assembly source file",
    ".c": "C source file",
    ".h": "C header source file",
    ".cpp": "C++ source file",
    ".hpp": "C++ header source file",
    ".rs": "Rust source file",
    ".go": "Go source file",
    ".zig": "Zig source file",
    ".java": "Java source file",
    ".cs": "C# source file",
    ".html": "HTML source file",
    ".css": "CSS stylesheet",
    ".js": "JavaScript source file",
    ".ts": "TypeScript source file",
    ".jsx": "ReactJS source file",
    ".tsx": "ReactJS TypeScript source file",
    ".py": "Python source file",
    ".lua": "Lua source file",
    ".nim": "Nim source file",
    # Config files
    ".json": "JavaScript object configuration file",
    ".csv": "CSV configuration file",
    ".xml": "XML markup file",
    ".gitignore": "Git configuration file",
    ".gitmodules": "Git configuration file",
    ".cmake": "CMake configuration file",
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
    elif ext in ELF_EXTENSIONS: 
        print(f"    Type: {ELF_EXTENSIONS[ext]} ({ext})")
    elif ext in TEXT_EXTENSIONS:
        print(f"    Type: {TEXT_EXTENSIONS[ext]} ({ext})")
    else:
        print(f"    Type: Unknown file type ({ext})")

def get_size(file):
    print(f"    Size: {format_file_size(os.path.getsize(file))}")

def get_atime(file):
    print(f"    Last accessed: {strftime('%Y-%m-%d %H:%M:%S', gmtime(os.path.getatime(file)))}")

def get_ctime(file):
    if os.name == "nt": print(f"    Created: {strftime('%Y-%m-%d %H:%M:%S', gmtime(os.path.getctime(file)))}")
    else: print(f"    Last modified metadata: {strftime('%Y-%m-%d %H:%M:%S', gmtime(os.path.getctime(file)))}")

def get_mtime(file):
    print(f"    Last modified: {strftime('%Y-%m-%d %H:%M:%S', gmtime(os.path.getmtime(file)))}")