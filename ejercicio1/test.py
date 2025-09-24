from antlr4 import *
from IfElseLangLexer import IfElseLangLexer
from IfElseLangParser import IfElseLangParser

def main():
    code = """
    a = 10;
    b = 20;
    if (a > b) {
      max = a;
    } else {
      if (a == b) {
        max = a;
      } else {
        max = b;
      }
    }
    """
    lexer = IfElseLangLexer(InputStream(code))
    tokens = CommonTokenStream(lexer)
    parser = IfElseLangParser(tokens)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()

