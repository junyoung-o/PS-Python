formula = []

def calc_plus():
    global formula
    for element in range(len(formula)):
        if("+" in formula[element]):
            calc = list(map(int, formula[element].split("+")))
            formula[element] = sum(calc)

def set_formula():
    global formula
    formula = input()
    formula = formula.split("-")

    calc_plus()
    formula = list(map(int, formula))

def init():
    set_formula()
    return

def print_result():
    result = -sum(formula) + 2 * formula[0]
    print(result)

def main():
    print_result()
    return

if(__name__=="__main__"):
    init()
    main()
