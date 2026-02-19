def main():
    decision=[] 
    while True:
        a=input("Ur decision, 12th stream???    ")
        if(a=="y" or a=="Y"):
            s=input("=> Business & Science  ")
            if(s=="Business"):
                bs=input("=> Commerce & Busmath ")
                if(bs=="Commerce"):
                    print("U chose COMMERCE")
                else:
                    print("U chose BUSINESS MATH")
            else:
                ss=input("=> Biomath, Compmath & Biocomp    ")
                if(ss=="Biomath"):
                    print("U chose BIOMATH")
                elif(ss=="Compmath"):
                    print("U chose COMPUTER MATHS")
                else:
                    print("U chose BIOCOMPUTER")
        else:
            print("It's now or never, choose ryt now!!")
    return decision

if __name__ == "__main__":
    main()