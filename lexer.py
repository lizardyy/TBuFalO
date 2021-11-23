import regex as re
import lexer_rules as rule


class Lexer(object):
    def __init__(self, rules):
        self.rules = rules

    # Dari text, tiap token masukin ke self.tokens
    def token_parser(self, text):
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
                    if tag:
                        token = (val, tag)
                        # Tambahin token ke Kumpulan Token
                        self.tokens.append(token)
                    break
            if not match:
                print(f"Syntax Error at position {position}:")
                print(text)
                print(" " * position + "^")
                break
            else:
                # Posisi regex sekarang di akhir token
                position = match.end(0)

    # Convert text ke string, semuanya sudah disubstitusi
    def toString(self, text):
        self.token_parser(text)
        string = ""
        for token in self.tokens:
            string += token[1] + " "
        return string

    # Generator token
    def toToken(self, text):
        self.token_parser(text)
        for i in self.tokens:
            yield i


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
                    print(lx.toString(line))
        if mode == "2":
            txt = ""
            while(txt != "exit"):
                # Ini minta input konsol
                txt = input("> ")
                for i in lx.toToken(txt):
                    print(i)
