class Client:
    def __init__(self, idd: str, phone: int):
        self.__idd = idd
        self.__phone = phone

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone: int):
        self.__phone = phone

    def get_id(self):
        return self.__idd
    
    def set_id(self, idd: str):
        self.__idd = idd

    def __str__(self):
        return f"{self.__idd}:{self.__phone}"
    

class Theater:
    def __init__(self, capacity: int):
        self.__seats: list[Client | None] = [None] * capacity

    def _verify_index(self, index: int):
        if index < 0 or index >= len(self.__seats):
            raise Exception("fail: cadeira nao existe")

    def _find_client(self, idd: str):
        for i, client in enumerate(self.__seats):
            if client is not None and client.get_id() == idd:
                return i
        return -1
    
    def reserve(self, idd: str, phone: int, index: int):
        self._verify_index(index)

        if self.__seats[index] is not None:
            raise Exception("fail: cadeira ja esta ocupada")

        if self._find_client(idd) != -1:
            raise Exception("fail: cliente ja esta no cinema")

        self.__seats[index] = Client(idd, phone)

    def cancel(self, idd: str):
        index = self._find_client(idd)

        if index == -1:
            raise Exception("fail: cliente nao esta no cinema")

        self.__seats[index] = None

    def get_seats(self):
        return self.__seats
    
    def __str__(self):
        out = []
        for client in self.__seats:
            if client is None:
                out.append("-")
            else:
                out.append(str(client))
        return "[" + " ".join(out) + "]"


def main():
    theater: Theater = []
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "init":
            theater = Theater(int(args[1]))
        elif args[0] == "show":
            print(theater)
        elif args[0] == "reserve":
            try:
                theater.reserve(str(args[1]), int(args[2]), int(args[3]))
            except Exception as e:
                print(e)
        elif args[0] == "cancel":
            try:
                theater.cancel(str(args[1]))
            except Exception as e:
                print(e)
        elif args[0] == "end":
            break
        else:
            print("fail: comando invalido")
main()
