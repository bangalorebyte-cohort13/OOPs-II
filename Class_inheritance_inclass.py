#!usr/bin/env python3.6
__author__ = 'udaykeith'

class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        self.label = input("What gate name would you like?")
        return self.label
# we can delcare a function that is yet undefined
# and define its logic later
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

#using label from LogicGate
class BinaryGate(LogicGate):
	# The constructors in both sub-classes start with an explicit call 
	# to the constructor of the parent class using the parent’s __init__

    def __init__(self,n):
        LogicGate.__init__(self,n) # makes BinaryGate a child of LogicGate

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
 

	


class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

class AndGate(BinaryGate):

	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):
		a = self.getPinA() 
		b = self.getPinB() 

        print("hello")

        if a == 1 and b == 1:
			return 1
		else:
			return 0


#class OrGate

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA() 
        b = self.getPinB() 

        if a == 1 or b ==1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):

       a = self.getPin()

       if a == 1:
        return 0
       else:
        return 1
    
#pin1 = BinaryGate("Gate 1").getPinA()
#pin2 = BinaryGate("Gate 1").getPinB()
    
# And Gate 1   
g1 = AndGate("g1") #
g1_output = g1.getOutput()
print(g1_output)



#g3 = NotGate('g3')
#print(g3.getOutput())
