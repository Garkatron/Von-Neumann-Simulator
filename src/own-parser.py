from main import CPU, HDD, RAM
class preprocessor:
    def __init__(self) -> None:
        self.PSEUDO_ASSAMBLY:dict = {
            
            # Other
            "LOD": "0000", # LOD: VALUE
            
            # Operands
            "ADD": "0001", # SUM
            "SUB": "0010", # SUB
            "DIV": "0011", # DIV
            "DVE": "0100", # DVE
            
            # Memory works
            "RDR" : "0101", # RR
            "RDH" : "0110", # RH
            
            # Memory works 2
            "RST": "0111", # WRR
            "HST" : "1000",# WRH
            
            # Acumulator works
            "LDR": "1001", # LOD: VALUE IN MEMORY
            
            # Program break
            "BRK": "1111"
        }
    
    def run(self,code:str) -> str:
        
        scapes = code.split("\n")
        code = map(lambda lines: lines.split(" "),scapes)
        translated=[]
        for line in list(code):
            translated.append([line[1],self.PSEUDO_ASSAMBLY[line[0]]])
        return translated
    
if __name__=="__main__":
    
    a=preprocessor()
    r=a.run("""LOD 0001
ADD 0001
HST 1000
BRK 0000""")
    
# TODO
# * MULTIPLES ARGUMENTOS POR FUNCIOn [ ]
# * FUNCIONES [ ]
# * VARIABLES [ ]
    with open("./main.vnpmc", 'w') as file:
        for c in r:
            file.write(f"{''.join(c)}\n")
