
class Shop:

    def __init__(self):
        self.iterator = 500
        self.users = {}
        self.accounts = {}

    def make(self):

        info = {}

        while True:

            i_n = False
            name = input("esme khod ra vard khonid:")

            for i in name:
                if i.isdigit():
                    i_n = True

            if i_n == True:
                print("dar esme adad vogod nadard.")
                continue

            i_f = False
            family = input("family khod ra vard khonid:")

            for i in family:
                if i.isdigit():
                    i_f = True

            if i_f == True:
                print("dar esme adad vogod nadard.")
                continue

            age = input("sen khod ra vard khonid:")

            if int(age) < 10:
                print("shoma nemitavanid dar in barname sabt nam khonid.")
                return None
            else:
                user1 = name[:len(name)//2:] + family[:len(family)//2:] + age
                user2 = name[:len(name)//2:] + family[len(family)//2::] + age

            while True:

                choice = input(f"beyn in do username yeki ra entekhab khonid\n1.{user1},2.{user2}:")

                if choice not in ("1", "2"):
                    continue
                elif choice == "1":
                    user = user1
                elif choice == "2":
                    user = user2

                print(f"{user} baray username shma set shote.")
                info["user"] = user
                break

            while True:

                password = input("dar pasword  mord nazar bayad horof bozorg va kochik,adad,symbol estefade khonid. \npassword mord nazar khod ra vard khonid:")

                up = False
                low = False
                num = False
                symbol = False

                if len(password) >= 4:

                    if " " in password:
                        print("te akhe chera:")
                        continue

                    for i in password:

                        if i.isupper():
                            up = True
                        elif i.islower():
                            low = True
                        elif i.isdigit():
                            num = True
                        else:
                            symbol = True

                    if up == True and low == True and num == True and symbol == True:
                        print(f"{password} baray password shma set shote.")
                        info["password"] = password
                        break
                    else:
                        continue
                else:
                    continue

            self.accounts[user] = password

            return info

    def check(self):

        i = 0

        while True:

            if i == 3:
                raise NameError("chera akhe:((")
            else:
                username = input("username khod ra vard khonid:")
                passeord = input("password khod ra vard khonid:")

                if username in self.accounts and self.accounts[username] == passeord:
                    print("login!")
                    return username
                else:
                    print("username ya password eshtebah ast.")
                    i += 1

    def user(self, username):

        self.iterator += 1
        id = self.iterator
        self.users[id] = {}

        return id

    def shop(self, id):

        while True:

            meno = input("1.supermarket,2.shoyande,3.protoein,0.cansel:")

            match meno:

                case "1":

                    m_supermarket = input("1.chip(130000),2.pafak(150000),3.mast(200000),4.tokhme(300000),5.bastanii(100000):")

                    match m_supermarket:

                        case "1":
                            item = "chips"
                            geymat = 130000

                        case "2":
                            item = "pafak"
                            geymat = 150000

                        case "3":
                            item = "mast"
                            geymat = 200000

                        case "4":
                            item = "tokhme"
                            geymat = 300000

                        case "5":
                            item = "bastanii"
                            geymat = 100000

                        case _:
                            print("gozine eshtebah ast.")
                            continue

                    tedad = int(input("chand adad niyaz darid?"))

                    self.users[id][f"{item} tedad:{tedad}"] = geymat * tedad

                case "2":

                    m_shoyande = input("1.shampo sar(500000),2.maye dast(250000),3.khamir dandon(200000):")

                    match m_shoyande:

                        case "1":
                            item = "shampo sar"
                            geymat = 500000

                        case "2":
                            item = "maye dast"
                            geymat = 250000

                        case "3":
                            item = "khamir dandon"
                            geymat = 200000

                        case _:
                            print("gozine eshtebah ast.")
                            continue

                    tedad = int(input("chand adad niyaz darid?"))

                    self.users[id][f"{item} tedad:{tedad}"] = geymat * tedad

                case "3":

                    m_protoein = input("1.gosht(2000000),2.morgh(4000000),3.mahi(400000):")

                    match m_protoein:

                        case "1":
                            item = "gosht"
                            geymat = 2000000

                        case "2":
                            item = "morgh"
                            geymat = 4000000

                        case "3":
                            item = "mahi"
                            geymat = 400000

                        case _:
                            print("gozine eshtebah ast.")
                            continue

                    tedad = int(input("chand adad niyaz darid?"))

                    self.users[id][f"{item} tedad:{tedad}"] = geymat * tedad

                case "0":

                    print("kharid tamam shode.")
                    break

                case _:

                    print("gozine eshtebah ast.")

    def factor(self, id):

        ragham = 0

        with open("factor.txt", "w", encoding="utf-8") as file:

            print(f"id moshtari:{id}")
            file.write(f"id moshtari:{id}\n")

            print("*" * 20)
            file.write("*" * 20 + "\n")

            for i, j in self.users[id].items():

                print(f"{i}:{j}")
                print("*" * 20)

                file.write(f"{i}:{j}\n")
                file.write("*" * 20 + "\n")

                ragham += j

            print(f"ragham kol:{ragham}")
            file.write(f"ragham kol:{ragham}\n")


shop = Shop()

while True:

    choice = input("1.sabt nam,2.login,0.exit:")

    if choice == "1":

        shop.make()

    elif choice == "2":

        username = shop.check()

        res = shop.user(username)

        shop.shop(res)

        shop.factor(res)

    elif choice == "0":

        raise NameError("barname baste shod")

    else:

        print("gozine eshtebah ast.")

