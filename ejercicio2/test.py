from antlr4 import *
from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser

def main():
    code = """
    i = 0;
    while (i < 10) {
      if (i == 5) {
        break;
      }
      i = i + 1;
      continue;
    }
    """
    lexer = WhileLangLexer(InputStream(code))
    tokens = CommonTokenStream(lexer)
    parser = WhileLangParser(tokens)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
