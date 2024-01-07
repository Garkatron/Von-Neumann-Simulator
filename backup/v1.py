
# *
def IntToByte(value:int) -> int:
    binary_representation = bin(value)
    return int(binary_representation,2)

def StrToByte(value:str) -> int:
    return int(value,2)


class Errors:
    MO4B:str="Increase exceeds 4 bits of memory"
    
# * -------------------------------- * #
class ALU:
    def __init__(self) -> None:
        self.A=format(0,"08b")
        self.B=format(0,"08b")
        self.Operand=None
    
    def SUM(self,value)->int:
        print(f"SUM: {value}")
        self.Operand = "+"
        self.B = self.A
        self.A = format(value,"08b")
        return format(int(self.A,2) + int(self.B,2),"08b")
    
    def SUB(self,value):
        print(f"SUB: {value}")
        self.Operand = "-"
        self.B = self.A
        self.A = format(value,"08b")
        return format(int(self.A,2) - int(self.B,2),"08b")
    
    def LOD(self,value):
        print(f"LOD: {value}")
        self.A = format(value,"08b")

    def DIV(self,value):
        print(f"DIV: {value}")
        self.Operand = "/"
        self.B = self.A
        self.A = format(value,"08b")
        return format(int(self.A,2) / int(self.B,2),"08b")
    
    def DVE(self,value):
        print(f"DVE: {value}")
        self.Operand = "//"
        self.B = self.A
        self.A = format(value,"08b")
        return format(int(self.A,2) // int(self.B,2),"08b")
    

class REGISTER:
    def __init__(self) -> None:
        self.ProgramCounter = format(0,"04b")
        self.Accumulator = None
        self.CurrentInstructionRegister = None
        self.Directions = format(0,"04b")
        self.Data = format(0,"08b")

    def AddProgramCounter(self):
        # Convierte el ProgramCounter actual a entero y luego incrementa en 1
        new_value = int(self.ProgramCounter, 2) + 1
        
        # Comprueba si el nuevo valor excede los 4 bits
        if new_value >= 2**4:
            raise ValueError(Errors.MO4B)
        else:
        # Convierte el nuevo valor a una cadena binaria de 4 bits y actualiza el ProgramCounter
            self.ProgramCounter = format(new_value, "04b")

    def AcumulatorStore(self,info:str):
        self.Accumulator = format(int(info,2),"08b")

    def StoreInstruction(self,instruction):
        self.CurrentInstructionRegister = instruction
        
class CONTROL_UNIT:
    def __init__(self) -> None:
        pass

    def DECODE(self,instruction):
        # ? Code for decode instruction
        return [instruction[0:4],instruction[4:8]]

class RAM:
    def __init__(self) -> None:
        self.memory={}
        for i in range(16):
            print(f"RAM: Formating memory: {format(i, '04b')}")
            self.memory[format(i, '04b')] = "00000000"

    def STORE_DATA(self,addr,value):
        self.memory[addr]=value
        
    def READ_DATA(self,addr):
        return self.memory[addr]

    def __str__(self) -> str:
        string=""
        for index, data in enumerate(self.memory):
            if data != "":
                string+=f"\n{index}: {data}"
        return string

class HDD:
    def __init__(self) -> None:
        self.memory={}
        for i in range(16):
            print(f"HDD: Formating memory: {format(i, '04b')}")
            self.memory[format(i, '04b')] = "00000000"

    def STORE_DATA(self,addr,value):
        self.memory[addr]=value
        
    def READ_DATA(self,addr):
        return self.memory[addr]

    def __str__(self) -> str:
        string=""
        for index, data in self.memory.items():
            if data != "":
                string+=f"\nIndex: {index} || Data: {data}"
        return string
        

class CPU:
    def __init__(self, ram, hdd) -> None:
        self.ControlUnit = CONTROL_UNIT()
        self.Alu = ALU()
        self.Register = REGISTER()
        self.Ram: RAM =ram
        self.Hdd: HDD =hdd
        
        self.PSEUDO_ASSAMBLY:dict = {
            
            # Other
            "0000": lambda args: self.Alu.LOD(StrToByte(args)), # LOD: VALUE
            
            # Operands
            "0001": lambda args: self.Register.AcumulatorStore(self.Alu.SUM(StrToByte(args))), # SUM
            "0010": lambda args: self.Register.AcumulatorStore(self.Alu.SUB(StrToByte(args))), # SUB
            "0011": lambda args: self.Register.AcumulatorStore(self.Alu.DIV(StrToByte(args))), # DIV
            "0100": lambda args: self.Register.AcumulatorStore(self.Alu.DVE(StrToByte(args))), # DVE
            
            # Memory works
            "0101" : lambda args: self.Register.AcumulatorStore(self.Ram.READ_DATA(StrToByte(args))), # RR
            "0110" : lambda args: self.Register.AcumulatorStore(self.Hdd.READ_DATA(StrToByte(args))), # RH
            
            # Memory works 2
            "0111": lambda args: self.Ram.STORE_DATA(args,self.Register.Accumulator), # WRR
            "1000" : lambda args: self.Hdd.STORE_DATA(args,self.Register.Accumulator),# WRH
            
            # Acumulator works
            "1001": lambda args: self.Alu.LOD(self.Ram.memory[args]), # LOD: VALUE IN MEMORY
            
            # Program break
            "1111": lambda args: print("PROGRAM BREAK") # BRK
        }
        
    def run(self): 
        for index, data in self.Hdd.memory.items():
            print(f"Chargin memory, Index: {index} Data: {data}")
            self.Ram.STORE_DATA(index,data)
        
        for i in self.Ram.memory:
            
            self.Register.Directions = self.Register.ProgramCounter
            
            self.Register.Data = self.Ram.memory[self.Register.Directions]
            
            self.Register.StoreInstruction(self.Register.Data)
            
            instruction = self.ControlUnit.DECODE(self.Register.CurrentInstructionRegister)
            
            print(f"[ Value: {instruction[0]} || Instruccion: {instruction[1]} ]")
            
            if instruction[0] in self.PSEUDO_ASSAMBLY:
                self.PSEUDO_ASSAMBLY[instruction[1]](instruction[0])
            else:
                print(f"Instruction not found; {instruction[1]}")
            
            self.Register.AddProgramCounter()
            
            if instruction[1]=="1111" or self.Register.ProgramCounter == "1111":
                break
        
        print("____________________________________________________________________________________")
        print("Accumulator data:")   
        print(f'Accumulator: {self.Register.Accumulator} :: Program counter: {self.Register.ProgramCounter}')
        
        print("____________________________________________________________________________________")
        print("Data and position in the hdd")
        print(self.Hdd)

if __name__=="__main__":
    
    hdd=HDD()
    
    hdd.STORE_DATA("0000","11110000") # LOD
    hdd.STORE_DATA("0001","00010001") # ADD
    
    hdd.STORE_DATA("0010","01001000") # WR
    hdd.STORE_DATA("0011","01000101") # RD
    
    hdd.STORE_DATA("0011","00001111") # BRK
    
    c=CPU(RAM(),hdd)
    c.run()
