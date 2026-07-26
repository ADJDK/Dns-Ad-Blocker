def load_blocklist(filename="blocklist.txt"):
    print("Function called")
    blocked =set()

    try:
        with open(filename,"r") as file:
            for line in file:
                domain=line.strip().lower()

                if domain and not domain.startswith("#"):
                    blocked.add(domain)

    except FileNotFoundError:
        print("BlockedList file doesnt exist")


    return blocked

if __name__=="__main__":
    blocked=load_blocklist()
    print(blocked)