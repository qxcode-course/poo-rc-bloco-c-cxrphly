class Slot:
    def __init__(self, name:str = "empty", qtd:int = 0, price:float = 0.0):
        self.name = name
        self.qtd = qtd
        self.price = price
    
    def get_name(self) -> str:
        return self.name
    def get_qtd(self) -> int:
        return self.qtd
    def get_price(self) -> float:
        return self.price
    
    def set_name(self, name:str) -> None:
        self.name = name
    def set_qtd(self, qtd:int) -> None:
        self.qtd = qtd
    def set_price(self, price:float) -> None:
        self.price = price

    def __str__(self) -> str:
        if self.name == "empty":
            return f"[   {self.name:5} : {self.qtd} U : {self.price:.2f} RS]"
        else:
            return f"[ {self.name:7} : {self.qtd} U : {self.price:.2f} RS]"
    
class Machine:
    def __init__(self, capacity:int = 0):
        self.slots = [Slot() for _ in range(capacity)]
        self.cash = 0.0
        self.capacity = capacity

    def get_slots(self, index:int) -> list:
        if 0 <= index < self.capacity:
            return self.slots[index]
        print("fail: indice nao existe")

        return None
    
    def set_slots(self, index:int, name:str, qtd:int, price:float):
        if not (0 <= index < self.capacity):
            print("fail: indice nao existe")
            return
        slot = self.slots[index]
        slot.set_name(name)
        slot.set_qtd(qtd)
        slot.set_price(price)

    def clear(self, index:int):
        if not (0 <= index < self.capacity):
            print("fail: indice nao existe")
            return
        
        self.slots[index] = Slot()

    def insert_cash(self, amount:float):
        if amount <= 0:
            print("fail: valor invalido")
            return
        self.cash += amount

    def buy(self, index:int):
        if not (0 <= index < self.capacity):
            print("fail: indice nao existe")
            return
        
        slot = self.slots[index]
        if slot.get_name() == "empty":
            print("fail: slot vazio")
            return
        
        if slot.get_qtd() == 0:
            print("fail: espiral sem produtos")
            return
        
        if self.cash < slot.get_price():
            print("fail: saldo insuficiente")
            return
        slot.set_qtd(slot.get_qtd() - 1)
        self.cash -= slot.get_price()

        print(f"voce comprou um {slot.get_name()}")

    def exchange_cash(self) -> float:
        if self.cash == 0:
            print("fail: sem saldo")
            return
        
        print(f"voce recebeu {self.cash:.2f} RS")
        self.cash = 0
        

    def __str__(self) -> str:
        lines = []
        lines.append(f"saldo: {self.cash:.2f}")
        for i, slot in enumerate(self.slots):
            lines.append(f"{i} {slot}")
        return "\n".join(lines)
    
def main():
    machine: Machine = Machine()
    while True:
        line = input()
        args = line.split()
        print(f"${line}")
        if args[0] == "end":
            break
        elif args[0] == "init":
            machine = Machine(int(args[1]))
        elif args[0] == "show":
            print(machine)
        elif args[0] == "set":
            machine.set_slots(int(args[1]), args[2], int(args[3]), float(args[4]))
        elif args[0] == "limpar":
            machine.clear(int(args[1]))
        elif args[0] == "dinheiro":
            machine.insert_cash(float(args[1]))
        elif args[0] == "troco":
            machine.exchange_cash()
        elif args[0] == "comprar":
            machine.buy(int(args[1]))
        else:
            print("fail:comando invalido")

main()
