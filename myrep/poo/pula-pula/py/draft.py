class Kid:
    def __init__(self, name:str, age:int):
        self.__name = name
        self.__age = age
    def __str__(self):
        return f"{self.__name}:{self.__age}"
    def get_age(self):
        return self.__age
    def set_age(self, new_age:int):
        if new_age >= 0:
            self.__age = new_age
        else:
            raise ValueError("fail: idade invalida")
    def get_name(self):
        return self.__name
    def set_name(self, name:str):
        self.__name = name

class Trampoline:
    def __init__(self):
        self.__playing_kids: list[Kid] = []
        self.__waiting_kids: list[Kid] = []
    def arrive(self, kid:Kid):
        self.__waiting_kids.append(kid)

        self.__waiting_kids.sort(key=lambda k: k.get_age())
    
    def enter(self):
        if not self.__waiting_kids:
            raise ValueError("fail: fila de espera vazia")
        else:
            self.__playing_kids.append(self.__waiting_kids.pop(-1))
            self.__playing_kids.sort(key=lambda k: k.get_age())

    def leave(self):
        if self.__playing_kids:
            self.__waiting_kids.insert(0,self.__playing_kids.pop(-1))
        
            
    def remove(self, name:str):
        for lista in (self.__playing_kids, self.__waiting_kids):
            for kid in lista:
                if kid.get_name() == name:
                    return lista.remove(kid)
        raise ValueError(f"fail: {name} nao esta no pula-pula")
        
        
    def __str__(self):
        playing = ", ".join([str(kid) for kid in self.__playing_kids])
        waiting = ", ".join([str(kid) for kid in self.__waiting_kids])
        return f"[{waiting}] => [{playing}]"
    
def main():
    trampoline = Trampoline()
    while True:
        try:
            line = input()
            arg = line.split()
            print("$" + line)
            comando = arg[0]
            if comando == "end":
                break
            elif comando== "arrive":
                name = arg[1]
                age = int(arg[2])
                kid = Kid(name, age)
                trampoline.arrive(kid)
            elif comando == "enter":
                trampoline.enter()
            elif comando == "leave":
                trampoline.leave()
            elif comando == "remove":
                trampoline.remove(arg[1])
            elif comando == "show":
                print(trampoline)
            else:
                print("fail: comando invalido")
        except Exception as e:
            print(e)

main()