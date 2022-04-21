# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

def arithmetic_arranger(prbs, solution=None):

        dashes = "-"
        space = " "

        line1 = []
        line2 = []
        line3 = []
        line4 = []

        # split strings (num) inside list(prbs) into value(prb)
        for num in prbs:
            prb = num.split(" ")
            num_1 = prb[0]
            op = prb[1]
            num_2 = prb[2]

            # Rules
            if len(prbs) > 5:
                return print("Error:too many problems.")

            Operator = ("+", "-")
            if op not in Operator:
                print("Error: Operator must be ´+´ or ´-´.")

            if len(num_1) > 4 or len(num_2) > 4:
                return print("Error: Numbers cannot be more than four digits")

            if num_1.isdigit and num_2.isdigit == False:
                print("Error: Numbers must contain digits.")

        # lines input
            spaces_to_fill = (max(len(x) for x in prb))
            answers = (str(eval(num)))

            line1.append(num_1.rjust(spaces_to_fill + 2) + space * 4)
            line2.append(op + space + num_2.rjust(spaces_to_fill) + space * 4)
            line3.append(dashes * (spaces_to_fill + 2) + space * 4)
            line4.append(answers.rjust(spaces_to_fill + 2) + space * 4)

        # convert line to string
        line1="".join(str(item) for item in (line1))
        line2="".join(str(item) for item in (line2))
        line3="".join(str(item) for item in(line3))
        line4="".join(str(item) for item in (line4))

        #print option if True
        t=((line1) + "\n" + (line2) + "\n" + (line3) + "\n" + (line4))
        f=((line1) + "\n" + (line2) + "\n" + (line3))

        if solution == True:
            print (t)

        if solution == None:
            print(f)