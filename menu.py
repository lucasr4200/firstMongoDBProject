def menu():
    def menu():
        while True:
            print("1.search articles")
            print("2.search authors")
            print("3.list venues")
            print("4.add articles")
            print("5.exit")
            ch = int(input("Enter choice: "))
            if ch == 1:
                artist_search()
            elif ch == 2:
                pass
            elif ch == 3:
                pass
            elif ch == 4:
                add()
            else:
                exit()
