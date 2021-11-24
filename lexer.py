import regex as re
# import re
import lexer_rules as rule


class Lexer(object):
    def __init__(self, rules):
        self.rules = rules
        self.multiline_mode = False

    # Dari text, tiap token masukin ke self.tokens
    def token_parser(self, text, line_num):
        # Posisi mulai regex
        position = 0
        # Kumpulan token
        self.tokens = []
        while position < len(text):
            match = None
            for re_rule in self.rules:
                pattern, tag = re_rule
                regex = re.compile(pattern)
                match = regex.match(text, position)
                if match:
                    val = match.group(0)
                    if tag == "'MCOMMENT'":
                        self.multiline_mode = not self.multiline_mode
                    if tag in ["'MCOMMENT'", "'ICOMMENT'"] or self.multiline_mode:
                        token = (val, "'COMMENT'")
                        # Tambahin token ke Kumpulan Token
                        self.tokens.append(token)
                    elif tag:
                        token = (val, tag)
                        # Tambahin token ke Kumpulan Token
                        self.tokens.append(token)
                    break
            if not match:
                print(f"[{line_num}] Unidentified Syntax at position {position}:")
                print(text)
                print(" " * position + "^")
                break
            else:
                # Posisi regex sekarang di akhir token
                position = match.end(0)

    # Convert text ke string, semuanya sudah disubstitusi
    def toList(self, text, line_num):
        self.token_parser(text, line_num)
        string = []
        tab_num = 0
        skip = True
        for token in self.tokens:
            if token[1] == "'TAB'":
                tab_num += 1
            if (token[1] != "'TAB'" and token[1] != "'COMMENT'"):
                skip = False
                string.append(token[1])
        if skip:
            print(f"[{line_num}] Empty Line! Skipping line...")
            return (0, [])
        elif string[0] == "'COMMENT'":
            print(f"[{line_num}] Error! Program InLine with Comment:", text.strip())
            return (0, [])
        else:
            return (tab_num, string)


if __name__ == "__main__":
    lx = Lexer(rule.lx_rules)

    mode = ""
    while(mode != "3"):
        print("Mode Lexer")
        print("> 1. File")
        print("> 2. Console")
        print("> 3. Exit")
        mode = input("Pilih Mode: ")
        if mode == "1":
            filename = input("Nama File: ")
            with open(filename) as file:
                for line in file:
                    level, lx_line = lx.toString(line)
                    if lx_line != []:
                        print(level, " ".join(lx_line))
        if mode == "2":
            print("Entering Console Mode, input exit to Quit Mode")
            txt = ""
            while(txt != "exit"):
                # Ini minta input konsol
                txt = input(">>> ")
                for i in lx.toToken(txt):
                    print(i)
