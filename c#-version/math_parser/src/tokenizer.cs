enum TokenType
{
    NUMBER,
    PLUS,
    MINUS,
    MULTIPLY,
    DIVIDE,
    LPAREN,
    RPAREN,
    EOF
}

class Token
{
    public TokenType Type { get; }
    public string Value { get; }

    public Token(TokenType type, string value)
    {
        Type = type;
        Value = value;
    }

    public override string ToString() => $"Token({Type}, {Value})";
}

class Tokenizer
{

    public List<Token> Tokenize(string input)
    {
        List<Token> tokens = new List<Token>();
        int i = 0;
        while (i < input.Length)
        {
            if (char.IsWhiteSpace(input, i))
            {
                i++;
                continue;
            }
            if (char.IsDigit(input, i))
            {
                string value = "";
                while (i < input.Length && char.IsDigit(input, i))
                {
                    value += input[i];
                    i++;
                }
                tokens.Add(new Token(TokenType.NUMBER, value));
                continue;
            }

            switch (input[i])
            {
                case '+':
                    tokens.Add(new Token(TokenType.PLUS, "+")); break;
                case '-':
                    tokens.Add(new Token(TokenType.MINUS, "-")); break;
                case '*':
                    tokens.Add(new Token(TokenType.MULTIPLY, "*")); break;
                case '/':
                    tokens.Add(new Token(TokenType.DIVIDE, "/")); break;
                case '(':
                    tokens.Add(new Token(TokenType.LPAREN, "(")); break;
                case ')':
                    tokens.Add(new Token(TokenType.RPAREN, ")")); break;

                default:
                    throw new Exception($"Unexpected character: {input[i]}");
            }

            i++;
        }

        return tokens;
    }
}