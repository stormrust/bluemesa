import os
from bluemesa.redis import symboltable

if __name__ == "__main__":
    sdy_set = symboltable.get_symbols_from_set("symbol-set-sdy")
    sp500_set = symboltable.get_symbols_from_set("symbol-set-sp500")
    intersection = sdy_set.intersection(sp500_set)
    print("These symbols are in the sp500")
    print(intersection)
    print(len(intersection))

    difference = sdy_set.difference(intersection)
    print("These symbols are not in the sp500")
    print(difference)
    print(len(difference))

    print(len(sdy_set))