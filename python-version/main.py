from enum import Enum
import argparse
import math

class TokenType(Enum):
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    LPAREN = 6  
    RPAREN = 7
    SQUARE = 8
    EOF = 9

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type.name}, {self.value})"
    
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self):
        return self.tokens[self.pos]
    
    def eat(self, token_type):
        if self.current_token().type == token_type:
            self.pos += 1
        else:
            raise ValueError(f"Expected {token_type}, got {self.current_token().type}")
    
    def factor(self):
        token = self.current_token()
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return token.value
        elif token.type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            return -self.factor()
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            result = self.expr()
            self.eat(TokenType.RPAREN)
            return result
        elif token.type == TokenType.SQUARE:
            return self.func()
        else:
            raise ValueError("Unexpected token in factor")
    
    def term(self):
        result = self.factor()
        while self.current_token().type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token()
            if token.type == TokenType.MULTIPLY:
                self.eat(TokenType.MULTIPLY)
                result *= self.factor()
            elif token.type == TokenType.DIVIDE:
                self.eat(TokenType.DIVIDE)
                result /= self.factor()
        return result
    
    def expr(self):
        result = self.term()
        while self.current_token().type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token()
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
                result += self.term()
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
                result -= self.term()
        return result
    
    def func(self):
        token = self.current_token()
        if token.type == TokenType.SQUARE:
            self.eat(TokenType.SQUARE)
            self.eat(TokenType.LPAREN)
            arg = self.expr()
            self.eat(TokenType.RPAREN)
            return math.sqrt(arg)
        else:
            raise ValueError("Unknown function")


def tokenize(input_string):
    tokens = []
    i = 0

    while i < len(input_string):
        if input_string.startswith("sqrt", i):
            tokens.append(Token(TokenType.SQUARE, "sqrt"))
            i+= len("sqrt")
            continue

        if input_string[i].isdigit():
            value = ""
            while i < len(input_string) and input_string[i].isdigit():
                value += input_string[i]
                i += 1
            tokens.append(Token(TokenType.NUMBER, int(value)))
            continue
        
        if input_string[i] == "+":
            tokens.append(Token(TokenType.PLUS, "+"))
            i+=1
            continue
        if input_string[i] == "-":
            tokens.append(Token(TokenType.MINUS, "-"))
            i+=1
            continue
        if input_string[i] == "*":
            tokens.append(Token(TokenType.MULTIPLY, "*"))
            i+=1
            continue
        if input_string[i] == "/":
            tokens.append(Token(TokenType.DIVIDE, "/"))
            i+=1
            continue
        if input_string[i] == "(":
            tokens.append(Token(TokenType.LPAREN, "("))
            i+=1
            continue
        if input_string[i] == ")":
            tokens.append(Token(TokenType.RPAREN, ")"))
            i+=1
            continue
        if input_string[i].isspace():
            i += 1
            continue
        raise ValueError(f"Unexpected character: {input_string[i]}")
    tokens.append(Token(TokenType.EOF, None))
    return tokens


def evaluate_math(path):
    with open(path, "r") as file:
        expression = file.read().strip()
    tokens = tokenize(expression)
    parser = Parser(tokens)
    result = parser.expr()
    return result

if __name__ == "__main__":
    parser_arg = argparse.ArgumentParser(description="Calculate math expressions from .math files")
    parser_arg.add_argument("--math", type=str, help="Path to the .math file")

    args = parser_arg.parse_args()

    if args.math:
        output = evaluate_math(args.math)
        print(f"Result: {output}")
    else:
        print("Please provide a --math file path")