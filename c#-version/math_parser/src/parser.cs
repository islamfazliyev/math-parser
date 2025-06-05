class Parser
{
    private List<Token> tokens;
    private int pos;

    public Parser(List<Token> tokens)
    {
        this.tokens = tokens;
        this.pos = 0;
    }

    public bool IsAtEnd()
    {
        return pos >= tokens.Count;
    }

    public Token currentToken()
    {
        if (IsAtEnd())
        {
            return new Token(TokenType.EOF, "");
        }
        return this.tokens[this.pos];
    }

    void Eat(TokenType tokenType)
    {
        if (currentToken().Type == tokenType)
        {
            pos++;
        }
        else
        {
            throw new Exception($"Expected {tokenType}, got {currentToken().Type}");
        }
    }

    public double Factor()
    {
        Token token = currentToken();
        if (token.Type == TokenType.NUMBER)
        {
            Eat(TokenType.NUMBER);
            return double.Parse(token.Value);
        }
        else if (token.Type == TokenType.MINUS)
        {
            Eat(TokenType.MINUS);
            return -Factor();
        }
        else if (token.Type == TokenType.LPAREN)
        {
            Eat(TokenType.LPAREN);
            double result = Expr();
            Eat(TokenType.RPAREN);
            return result;
        }
        else
        {
            throw new Exception("Unexpected token in factor");
        }
    }

    public double Expr()
    {
        double result = Term(); 
        while (currentToken().Type == TokenType.PLUS || currentToken().Type == TokenType.MINUS)
        {
            Token token = currentToken();
            if (token.Type == TokenType.PLUS)
            {
                Eat(TokenType.PLUS);
                result += Term();
            }
            else if (token.Type == TokenType.MINUS)
            {
                Eat(TokenType.MINUS);
                result -= Term();
            }
        }
        return result;
    }

    public double Term()
    {
        double result = Factor(); 
        while (currentToken().Type == TokenType.MULTIPLY || currentToken().Type == TokenType.DIVIDE)
        {
            Token token = currentToken();
            if (token.Type == TokenType.MULTIPLY)
            {
                Eat(TokenType.MULTIPLY);
                result *= Factor();
            }
            else if (token.Type == TokenType.DIVIDE)
            {
                Eat(TokenType.DIVIDE);
                result /= Factor();
            }
        }
        return result;
    }

}