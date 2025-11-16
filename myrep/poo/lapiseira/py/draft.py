class Lead:
    def __init__(self, thickness:float = 0.0, hardness:str = "", size:int = 0 ):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerPage(self):
        usage = {"HB" : 1, "2B" : 2, "4B" : 4, "6B" : 6}
        for tip in usage:
            if self.__hardness == tip:
                return usage[tip]
        return 0
    
    def getThickness(self):
        return self.__thickness
    def getHardness(self):
        return self.__hardness
    def getSize(self):
        return self.__size
    
    def setSize(self, size:int):
        self.__size = size

    def __str__(self):
        return f"{self.__thickness}:{self.__hardness}:{self.__size}"
    
class Pencil:
    def __init__(self, thickness:float = 0.0):
        self.__thickness = thickness
        self.__tip: Lead | None = None
        self.__barrel: list[Lead] = []

    def hasLead(self):
        return self.__tip is not None
    
    def insertLead(self, tip:Lead):
        if tip.getThickness() != self.__thickness:
            print("fail: calibre incompatível")
            return
        else:
            self.__barrel.append(tip)
    def removeLead(self):
        if self.__tip is None:
            print("fail: nao existe grafite")
            return
        else:
            self.__tip = None

    def pullLead(self):
        if self.__tip is not None:
            print("fail: ja existe grafite")
            return
        if len(self.__barrel) == 0:
            print("fail: nao ha grafite no estojo")
            return
        else:
            self.__tip = self.__barrel.pop(0)

    def writePage(self):

        self.__tip.setSize(self.__tip.getSize() - self.__tip.usagePerPage())
        
    def __str__(self):
        tip_str = "[]" if self.__tip is None else "["+str(self.__tip)+"]"
        barrel_str = "<"+"".join("["+str(lead)+"]" for lead in self.__barrel) + ">"
        return f"calibre: {self.__thickness}, bico: {tip_str}, tambor: {barrel_str}"


def main():
    pencil:Pencil = Pencil()
    while True:
        line = input()
        print("$"+line) 
        args:list[str]=line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            pencil = Pencil(float(args[1]))
        elif args[0] == "show":
            print(pencil)
        elif args[0] == "insert":
            tip = Lead(float(args[1]), args[2], int(args[3]))
            pencil.insertLead(tip)
        elif args[0] == "pull":
            pencil.pullLead()
        elif args[0] == "remove":
            pencil.removeLead()
        elif args[0] == "write":
            pencil.writePage()
        else:
            print("fail: comando invalido")


main()