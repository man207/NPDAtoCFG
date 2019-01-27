import itertools as it


class pushdownautomata():
    def __init__(self,states = [],symbols = [],initialstate = "",finalstates = [],stsymbols = []):
        self.states = states
        self.symbols = symbols
        self.stsymbols = stsymbols
        self.initialstate = initialstate
        self.finalstates = finalstates
        self.transitions = []
    def addsymbol(self , symbol):
        if symbol not in self.symbols:
            self.symbols.append(symbol)
    def addstacksymbol(self , symbol):
        if symbol not in self.stsymbols:
            self.stsymbols.append(symbol)
    def addstate(self , state):
        if state not in self.states:
            self.states.append(state)
    def addfinalstate(self,finalstate):
        if finalstate not in self.finalstates:
            self.finalstates.append((finalstate))

    def setinitialstate(self,initialstate):
        self.initialstate = (initialstate)
        if initialstate not in self.states:
            self.states.insert(0,initialstate)
        else:
            self.states.remove(initialstate)
            self.states.insert(0,initialstate)

    def addtransition(self,transition):
        if transition not in self.transitions:
            self.transitions.append(transition)

        if transition[0] not in self.states:
            self.states.append((transition[0]))

        if transition[3] not in self.states:
            self.states.append((transition[3]))

        if transition[2] not in self.stsymbols:
            if transition[2] != "λ":
                self.stsymbols.append((transition[2]))

        if transition[4] not in self.stsymbols:
            if transition[4] != "λ":
                self.stsymbols.append((transition[4]))

        if transition[1] not in self.symbols:
            if transition[1] != "λ":
                self.symbols.append((transition[1]))

        if transition not in self.transitions:
            self.transitions.append(transition)
    def standardlize(self):
        todo = []
        for transition in self.transitions:
            if transition[2] == "λ":
                for alphabet in self.stsymbols:
                    newalphabet = transition[4] + (alphabet)
                    todo.append([transition[0],transition[1],alphabet,transition[3],newalphabet])
        for that in todo:
            self.addtransition(that)

    def toCFG(self):
        dacgf = []
        self.standardlize()
        for state in self.finalstates:
            rule = ["S",(self.initialstate,"λ",state)]
            dacgf.append(rule)

        for state in self.states:
            rule = [(state,"λ",state),"λ"]
            dacgf.append(rule)

        for transition in self.transitions:
            prodcuts = it.product(self.states,repeat = len(transition[4]))
            for stuff in prodcuts:
                rule = [(transition[0],transition[2],stuff[-1])]
                if transition[1] != "λ":
                    rule.append(transition[1])
                stuff = list(stuff)
                stuff.insert(0,transition[3])
                for i,item in enumerate(transition[4]):
                    rule.append((stuff[i],item,stuff[i+1]))
                dacgf.append(rule)
        return dacgf

        
#ff = pushdownautomata()
#ff.addtransition(["s","l","λ","s","X"])
#ff.addtransition(["s","r","X","s","λ"])
#ff.setinitialstate("s")
#ff.addfinalstate("s")
#jj = ff.toCFG()
#for i in jj:
#        i.insert(1,"→")
#        temp1 = ' '.join(map(str, i))
#        temp1 = temp1.replace("\'","")
#        temp1 = temp1.replace("(","<")
#        temp1 = temp1.replace(")",">")
#        print(temp1)
#print(ff.symbols)
#print(ff.stsymbols)
#print(ff.finalstates)
#for s in jj:
#    print(s)
#