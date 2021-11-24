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


def print_masuk(term, var):
    for i in term:
        if i[0] == 'S':
            print(i)
    for i in var:
        if i[0] == 'S':
            print(i)


def print_table(table):
    print("Tabel CYK")
    for idx, row in enumerate(table):
        print(row)


def list_product(l1, l2):
    product = []
    for i in l1:
        for j in l2:
            product.append([i, j])
    return product


class CYKAlgo(object):
    def __init__(self, source, from_file=False):
        if from_file:
            self.terms, self.vars = split_grammar(
                gc.convert_grammar(gc.read_grammar(source)))
        else:
            self.terms, self.vars = split_grammar(source)

    def fill_table(self, input_list, debug=False):
        input_len = len(input_list)
        self.table = [[[] for _ in range(input_len - i)]
                      for i in range(input_len)]

        for i in range(input_len):
            for term in self.terms:
                if term[1] == input_list[i]:
                    if term[0] not in self.table[0][i]:
                        self.table[0][i].append(term[0])

        for row_p in range(1, input_len):
            for column_p in range(input_len - row_p):
                for first_len in range(1, row_p + 1):
                    first_list = self.table[first_len - 1][column_p]
                    second_list = self.table[row_p -
                                             first_len][column_p + first_len]
                    combinations = list_product(first_list, second_list)
                    if debug:
                        print(f"Row {row_p}, Col {column_p}\n", first_list, second_list)
                    for rule in self.vars:
                        for comb in combinations:
                            if rule[1:] == comb and rule[0] not in self.table[row_p][column_p]:
                                self.table[row_p][column_p].append(rule[0])

    def process(self, input_list, debug=False):
        self.fill_table(input_list, debug)
        if debug:
            print_table(self.table)
        if len(self.table) > 0 and 'S' in self.table[-1][0]:
            return "ACCEPTED"
        else:
            return "REJECTED"
