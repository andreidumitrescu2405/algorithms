
numberslist = [[['#','#','#'],[' ',' ','#'],['#','#','#'],['#','#','#'],['#',' ','#'],['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#']],
               [['#',' ','#'],[' ',' ','#'],[' ',' ','#'],[' ',' ','#'],['#',' ','#'],['#',' ',' '],['#',' ',' '],[' ',' ','#'],['#',' ','#'],['#',' ','#']],
               [['#',' ','#'],[' ',' ','#'],['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#'],['#','#','#'],[' ',' ','#'],['#','#','#'],['#','#','#']],
               [['#',' ','#'],[' ',' ','#'],['#',' ',' '],[' ',' ','#'],[' ',' ','#'],[' ',' ','#'],['#',' ','#'],[' ',' ','#'],['#',' ','#'],[' ',' ','#']],
               [['#','#','#'],[' ',' ','#'],['#','#','#'],['#','#','#'],[' ',' ','#'],['#','#','#'],['#','#','#'],[' ',' ','#'],['#','#','#'],['#','#','#']]]

# for i in range(len(numberslist)):
#     for j in range(len(numberslist[0])):
#         print(numberslist[i][j], end=" ")
#     print()

# print(numberslist[:][:][:])

def inttolist(myint):
    mylist = [int(x) for x in str(myint)]
    return mylist
def printnumber(number):
    digitslist = inttolist(number)
    for i in range(5):
        for chidx in range(len(digitslist)):
            for idx in range(3):
                print(numberslist[i][digitslist[chidx]][idx], end=" ")
            print("  ", end='')
        print()
try:
    x = input("Enter the number you want to output: ")
    printnumber(x)
    # print(inttolist(x))
except ValueError:
    print("Please enter numerical values only.")
except:
    print("Something went wrong.")
else:
    print("Completed the program successfully.")
finally:
    print("Program finished.")
        

        


    
