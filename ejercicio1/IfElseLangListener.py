# Generated from IfElseLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IfElseLangParser import IfElseLangParser
else:
    from IfElseLangParser import IfElseLangParser

# This class defines a complete listener for a parse tree produced by IfElseLangParser.
class IfElseLangListener(ParseTreeListener):

    # Enter a parse tree produced by IfElseLangParser#program.
    def enterProgram(self, ctx:IfElseLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#program.
    def exitProgram(self, ctx:IfElseLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#statement.
    def enterStatement(self, ctx:IfElseLangParser.StatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#statement.
    def exitStatement(self, ctx:IfElseLangParser.StatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#assignment.
    def enterAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#assignment.
    def exitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#ifStatement.
    def enterIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#ifStatement.
    def exitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#condition.
    def enterCondition(self, ctx:IfElseLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#condition.
    def exitCondition(self, ctx:IfElseLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#MulDiv.
    def enterMulDiv(self, ctx:IfElseLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#MulDiv.
    def exitMulDiv(self, ctx:IfElseLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#AddSub.
    def enterAddSub(self, ctx:IfElseLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#AddSub.
    def exitAddSub(self, ctx:IfElseLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#Parens.
    def enterParens(self, ctx:IfElseLangParser.ParensContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#Parens.
    def exitParens(self, ctx:IfElseLangParser.ParensContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#Num.
    def enterNum(self, ctx:IfElseLangParser.NumContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#Num.
    def exitNum(self, ctx:IfElseLangParser.NumContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#Id.
    def enterId(self, ctx:IfElseLangParser.IdContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#Id.
    def exitId(self, ctx:IfElseLangParser.IdContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#operator.
    def enterOperator(self, ctx:IfElseLangParser.OperatorContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#operator.
    def exitOperator(self, ctx:IfElseLangParser.OperatorContext):
        pass



del IfElseLangParser