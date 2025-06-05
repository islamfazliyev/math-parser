class Program
{
    static void Main()
    {
        var tokenizer = new Tokenizer();
        var tokens = tokenizer.Tokenize("2 + (3 * 4)");
        var parser = new Parser(tokens);
        var result = parser.Expr();

        Console.WriteLine("Tokens:");
        foreach (var token in tokens)
        {
            Console.WriteLine(token);
        }

        Console.WriteLine($"\nResult: {result}");
    }
}