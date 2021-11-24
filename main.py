import lexer as lx
import lexer_rules as lx_rule
import cyk_main as cyk


def print_result(status, line, line_num):
    global line_error
    if status == "ACCEPTED":
        print("[{:0>3d}] Line Accepted".format(line_num))
    elif status == "REJECTED":
        print("[{:0>3d}] Line Rejected: {}".format(line_num, line.strip()))
        line_error += 1
    elif status == "SKIP":
        print("[{:0>3d}] Indentation Error! Skipping line...".format(line_num))
        line_error += 1
    elif status == "IFREJECTED":
        print("[{:0>3d}] Error! ELIF/ELSE comes before IF!".format(line_num))
        line_error += 1
    else:
        print("[{:0>3d}] Unknown Error".format(line_num))
        line_error += 1


def change_if_mode(level, mode):
    global if_mode

    while(level + 1 > len(if_mode)):
        if_mode.append(False)
    if mode == "'IF'":
        if_mode[level] = True
        i = level + 1
        while (i < len(if_mode)):
            if_mode[i] = False
            i += 1
    elif mode in ["'ELIF'", "'ELSE'"] and not if_mode[level]:
        return "IFREJECTED"
    elif mode == "'ELSE'":
        if_mode[level] = False
        i = level + 1
        while (i < len(if_mode)):
            if_mode[i] = False
            i += 1
    elif mode == "'ELIF'":
        i = level + 1
        while (i < len(if_mode)):
            if_mode[i] = False
            i += 1
    return "IFACCEPTED"


def process_line(line, line_num):
    global lexer
    global CYK
    global tab_level

    level, lexer_line = lexer.toList(line, line_num)
    # Gak Kosong
    if lexer_line:
        if level < tab_level:
            tab_level = level
        if level > tab_level:
            status = "SKIP"
        elif lexer_line[0] in ["'IF'", "'ELSE'", "'ELIF'"]:
            status = change_if_mode(level, lexer_line[0])
            if status == "IFACCEPTED":
                status = CYK.process(lexer_line)
        else:
            status = CYK.process(lexer_line)
        if lexer_line[-1] == "'COLON'":
            tab_level += 1
        print_result(status, line, line_num)


if __name__ == "__main__":

    lexer = lx.Lexer(lx_rule.lx_rules)
    CYK = cyk.CYKAlgo("grammar.txt", True)

    filename = input("Nama File: ")
    tab_level = 0
    if_mode = [False]
    line_num = 1
    line_error = 0
    try:
        with open(filename) as file:
            for line in file:
                process_line(line, line_num)
                line_num += 1
                # if lexer_line[0] == "'IF'":
                #     if_mode = True
                # elif lexer_line[0] == "'ELSE'" and if_mode:
                #     if_mode = False
                # elif lexer_line[0] == "'ELSE'":
                #     print("Error")
                #     break
                # elif lexer_line[0] == "'ELIF'" and not if_mode:
                #     print("Error")
                #     break

                # result = CYK.process(lexer_line)
                # print_result(result, line)
        print("Final Result:")
        print("Processed: {} Line".format(line_num - 1))
        print("Error    : {} Line".format(line_error))
    except:
        print("Cannot open File!")
    # mode = ""
    # while(mode != "3"):
    #     print("Mode Lexer")
    #     print("> 1. File")
    #     print("> 2. Console")
    #     print("> 3. Exit")
    #     mode = input("Pilih Mode: ")
    #     if mode == "1":
    #         filename = input("Nama File: ")
    #         with open(filename) as file:
    #             for line in file:
    #                 level, lexer_line = lexer.toList(line)
    #                 if lexer_line != []:
    #                     result = CYK.process(lexer_line)
    #                     if not result:
    #                         print("Not Accepted: ", lexer_line)
    #     if mode == "2":
    #         print("Entering Console Mode, input exit to Quit Mode")
    #         txt = ""
    #         while(txt != "exit"):
    #             # Ini minta input konsol
    #             txt = input(">>> ")
    #             _, lexer_line = lexer.toList(txt)
    #             print("Yang diparse mesin:", lexer_line)
    #             CYK.process(lexer_line, True)
