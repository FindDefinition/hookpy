import hookpy 

def main():
    print(5)
    a = 5
    b = 3 
    with hookpy.hold(verbose=True):

        print(b)
        


if __name__ == "__main__":
    main()