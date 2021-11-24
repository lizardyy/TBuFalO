import grammar_converter as gc


def split_grammar(grammar):
    terminals = []
    variables = []
    for i in grammar:
        if len(i) == 2 and i[1][0] == '\'':
            terminals.append(i)
        else:
            variables.append(i)
    return terminals, variables


def print_table(table):
    for i in table:
        print(i)


def list_product(l1, l2):
    product = []
    for i in l1:
        for j in l2:
            product.append([i, j])
    return product


def CYK(input_list, terminals, variables):
    input_len = len(input_list)
    table = [[[] for _ in range(input_len - i)] for i in range(input_len)]

    for i in range(input_len):
        for term in terminals:
            if term[1] == input_list[i]:
                if term[0] not in table[0][i]:
                    table[0][i].append(term[0])

    for row_p in range(1, input_len):
        for column_p in range(input_len - row_p):
            for first_len in range(1, row_p + 1):
                first_list = table[first_len - 1][column_p]
                second_list = table[row_p - first_len][column_p + first_len]
                combinations = list_product(first_list, second_list)
                # print(first_list, second_list)
                for rule in variables:
                    for comb in combinations:
                        if rule[1:] == comb and rule[0] not in table[row_p][column_p]:
                            table[row_p][column_p].append(rule[0])

    print_table(table)


if __name__ == "__main__":
    grammar = gc.read_grammar("grammar.txt")
    CNF = gc.convert_grammar(grammar)
    t, v = split_grammar(CNF)
    input_p = ["'IDENTIFIER'", "'ASSIGN'", "'NUM'"]
    CYK(input_p, t, v)

    for i in t:
        print(i)
    print("Variables")
    for j in v:
        print(j)
