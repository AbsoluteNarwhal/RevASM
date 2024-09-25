import os
import colorama

LINE_LENGTH = 16
NUM_ALIGNMENT = 8

# there are two hard things in programming: cache invalidation, naming things and off-by-one errors.
def hex_format(contents):
    colorama.init()
    byte_pos = 0
    byte_buffer = ""
    while byte_pos < len(contents):
        print("{:0{}d}".format((byte_pos//12), NUM_ALIGNMENT) + ": ", end="")
        for _ in range(min(LINE_LENGTH, len(contents) - byte_pos)):
            print(format_byte(contents[byte_pos]), end="")
            byte_buffer += format_translate_byte(contents[byte_pos])
            byte_pos += 1
        print(byte_buffer)
        byte_buffer = ""

def format_byte(byte: int):
    res = format(byte, "x").upper()
    if len(res) == 1:
        return f"0{res} "
    else:
        return f"{res} "
    
def format_translate_byte(byte):
    if byte >= 32 and byte <= 126:
        return colorama.Fore.CYAN + chr(byte) + colorama.Style.RESET_ALL
    elif byte == 10:
        return colorama.Fore.YELLOW + "." + colorama.Style.RESET_ALL
    else:
        return "."