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
        self.__waiting:list[Person | None] = []


    def add_person(self, person:Person):
        self.__waiting.append(person)

    def call_next(self):
        for i in range(len(self.__counters)):
            if self.__counters[i] is None and self.__waiting:
                self.__counters[i] = self.__waiting.pop(0)
    
    def finish_service(self, counter_index:int):
        if 0 <= counter_index < len(self.__counters):
            self.__counters[counter_index] = None

    def __str__(self):
        counters_str = [str(Person) if Person else "-----" for Person in self.__counters]
        waiting_str = [str(Person) for Person in self.__waiting]
        return f"Counters: {counters_str}\nWaiting: {waiting_str}"

def main():
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "init":
            market = Market(int(args[1]))
        elif args[0] == "show":
            print(market)
        elif args[0] == "enter":
            person = Person(str(args[1]))
            market.add_person(person.get_name())
        elif args[0] == "call":
            market.call_next()
        elif args[0] == "finish":
            market.finish_service(int(args[1]))
        elif args[0] == "end":
            break
        else:
            print("fail: comando invalido")

main()