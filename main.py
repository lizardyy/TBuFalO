import lexer as lx
import lexer_rules as lx_rule
import cyk_main as cyk

if __name__ == "__main__":

    lexer = lx.Lexer(lx_rule.lx_rules)
    CYK = cyk.CYKAlgo("grammar.txt", True)

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
                    level, lexer_line = lexer.toList(line)
                    if lexer_line != []:
                        print(level, " ".join(lexer_line))
        if mode == "2":
            print("Entering Console Mode, input exit to Quit Mode")
            txt = ""
            while(txt != "exit"):
                # Ini minta input konsol
                txt = input(">>> ")
                _, lexer_line = lexer.toList(txt)
                print("Yang diparse mesin:", lexer_line)
                print("Keputusan: ", end="")
                CYK.process(lexer_line, True)
