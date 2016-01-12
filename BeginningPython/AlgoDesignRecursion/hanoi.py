# hanoi.py
#    Recursive solution to Towers of Hanoi problem.

def moveTower(n, source, dest, temp):
    if n == 1:
        print("Move disk from", source, "to", dest+".")
    else:
        moveTower(n-1, source, temp, dest)
        moveTower(1, source, dest, temp)
        moveTower(n-1, temp, dest, source)

def hanoi(n):
    moveTower(n, "A", "C", "B")

def main():
    print("Towers of Hanoi")
    n = eval(input("How many disks? "))
    moveTower(n, "A", "C", "B")

if __name__ == '__main__': main()

        
