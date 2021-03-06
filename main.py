from language.characteristicaLexer import characteristicaLexer
from language.characteristicaParser import characteristicaParser
from visitor import CustomVisitor
from antlr4 import FileStream, CommonTokenStream
import sys, tabulate
from internals.proofVerify import *

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("\n")
        cv = CustomVisitor()
        fst = FileStream(sys.argv[1])
        lex = characteristicaLexer(fst)
        tokenst = CommonTokenStream(lex)
        parser = characteristicaParser(tokenst)
        tree = parser.prog()
        cv.visit(tree)
        print("\n")
        truthList = []
        for stat in cv.statDict.values():
            truthList += [[stat.name, stat.isVerified]]
        print(tabulate.tabulate(truthList, headers=["Name", "Verified"]))
        tcAxList = tcList_to_tcAxList(cv.tcList)
        verify(tcAxList)
        truthList = []
        print("\n")
        for stat in cv.statDict.values():
            truthList += [[stat.name, stat.isVerified]]
        print(tabulate.tabulate(truthList, headers=["Name", "Verified"]))
        print("\n")