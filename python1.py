# imports
import colorama
from colorama import Fore
import sys
# comparation operators
multiply = 'MULTIPLY'
divide = 'DIVIDE'
add = 'ADD'
substract = 'SUBSTRACT'
# name variables
ein1 = str(sys.argv[1])
zwei1 = str(sys.argv[2])
drei1 = str(sys.argv[3])
# convert all to uppercase
ein = ein1.upper()
zwei = zwei1.upper()
drei = drei1.upper()
# color control
COLORRED = Fore.RED
COLORGREEN = Fore.GREEN

# operation functions


def addfunc(add1, add2):

    ans = float(add1)+float(add2)
    anschecktype = ans.is_integer()
    if anschecktype == True:
        return int(ans)
    elif anschecktype == False:
        return ans
    else:
        return 'err'


def subfunc(sub1, sub2):
    ans = sub1+sub2
    anschecktype = ans.is_integer()
    if anschecktype == True:
        return int(ans)
    elif anschecktype == False:
        return ans
    else:
        return 'err'


def divfunc(div1, div2):
    ans = div1+div2
    anschecktype = ans.is_integer()
    if anschecktype == True:
        return int(ans)
    elif anschecktype == False:
        return ans
    else:
        return 'err'


def mulfunc(mul1, mul2):
    ans = mul1+mul2
    anschecktype = ans.is_integer()
    if anschecktype == True:
        return int(ans)
    elif anschecktype == False:
        return ans
    else:
        return 'err'

# main function


def calfunc(num1, num2, typeofcalc):
    #
    if typeofcalc == multiply:
        return mulfunc(num1, num2)
    elif typeofcalc == divide:
        return divfunc(num1, num2)

    elif typeofcalc == add:
        return addfunc(num1, num2)
    elif typeofcalc == substract:
        return subfunc(num1, num2)
# error message
    else:
        print('')
        print(COLORRED + "sorry, this calculator can not perform such calculations")
        print(COLORRED + "try these types:")
        print(COLORRED + "        add")
        print(COLORRED + "        substract")
        print(COLORRED + "        divide")
        print(COLORRED + "        multiply")
        print(COLORGREEN + "btw, they are not case sensitive")

        return ''

# format function


# final formating steps
finale = calfunc(ein, zwei, drei)
# finaleReadable = f'{finale:,}'
finaleReadable = finale

print(COLORGREEN + str(finaleReadable))


# junk extra script

# def calfunc(num1, num2, typeofcalc):
#     num1type = type(num1)
#     if typeofcalc == multiply:
#         ans = newnum1 * newnum2
#         return ans
#     elif typeofcalc == divide:
#         ans = newnum1 / newnum2
#         return ans
#     elif typeofcalc == add:
#         ans = newnum1 + newnum2
#         return ans
#     elif typeofcalc == substract:
#         ans = newnum1 - newnum2
#         return ans
#     else:
#         print("sorry, this calculator can not perform such calculations, try these words: add,substract,divide,multiply, btw, they are not case sensitive")
#         ans = 0
#         return TypeError


# print(calfunc(ein, zwei, drei))
# ein = str(ein)
# zwei = str(zwei)
# drei = str(drei)
