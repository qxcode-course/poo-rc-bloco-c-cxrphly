class Person:
    def __init__(self, name:str):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def __str__(self):
        return self.__name
    
class Market:
    def __init__(self, qtd_counters:int):
        self.__counters:list[Person|None] = [None]*qtd_counters
        self.__waiting:list[Person] = []


    def add_person(self, person:Person):
        self.__waiting.append(person)

    def call_next(self, index:int ):
        if 0 <= index < len(self.__counters):
            if self.__counters[index] is None:
                if len(self.__waiting) > 0:
                    next_person = self.__waiting.pop(0)
                    self.__counters[index] = next_person
                else:
                    print("fail: sem clientes")
            else:
                print("fail: caixa ocupado")
        else:
            print("fail: caixa invalido")


    def finish_service(self, counter_index:int):
        if 0 <= counter_index < len(self.__counters):
            if self.__counters[counter_index] is None:
                print("fail: caixa vazio")
            else:
                self.__counters[counter_index] = None
        else:
            print("fail: caixa inexistente")

    def __str__(self):
        counters_str = ", ".join([str(Person) if Person else "-----" for Person in self.__counters])
        waiting_str = ", ".join([str(Person) for Person in self.__waiting])
        return f"Caixas: [{counters_str}]\nEspera: [{str(waiting_str)}]"

def main():
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "init":
            market = Market(int(args[1]))
        elif args[0] == "show":
            print(market)
        elif args[0] == "arrive":
            person = Person(str(args[1]))
            market.add_person(person)
        elif args[0] == "call":
            market.call_next(int(args[1]))
        elif args[0] == "finish":
            market.finish_service(int(args[1]))
        elif args[0] == "end":
            break
        else:
            print("fail: comando invalido")

main()