import chardet
import vars
import info_common

def select_text(args, ext):
    if args[1] == "info":
        if len(args) < 4: 
            select_text_info(args[2], "", ext)
        else:
            select_text_info(args[2], args[-1], ext)

def select_text_info(file, infotype, ext):
    print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal")
    print()
    if not infotype in ["", "--meta"]: print("File: " + file)
    match infotype:
        case "": get_all(file, ext)
        case "--meta": info_common.get_meta(file, ext)
        case "--type": info_common.get_type(ext)
        case "--size": info_common.get_size(file)
        case "--atime": info_common.get_atime(file)
        case "--ctime": info_common.get_ctime(file)
        case "--mtime": info_common.get_mtime(file)
        case "--linebr": get_linebr(file)
        case "--enc": get_enc(file)
        case _: print(f"Error: File data '{infotype}' is not available for this file type.")
    print()

def get_all(file, ext):
    print("File information:")
    info_common.get_type(ext)
    info_common.get_size(file)
    info_common.get_ctime(file)
    info_common.get_atime(file)
    info_common.get_mtime(file)
    get_linebr(file)
    get_enc(file)

def get_linebr(file):
    with open(file, 'r') as f:
        content = f.read()
        if '\r\n' in content:
            print("    Newlines: Windows CRLF")
        elif '\n' in content:
            print("    Newlines: Unix LF")
        else:
            print("    Newlines: No newline characters used")

def get_enc(file):
    with open(file, 'rb') as f:
        result = chardet.detect(f.read())
        charenc = result['encoding']
        print(f"    Encoding: {charenc}")