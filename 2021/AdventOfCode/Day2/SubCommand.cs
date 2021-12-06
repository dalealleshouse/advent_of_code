namespace AdventOfCode.Day2
{
    public record SubCommand(string Command, int Value)
    {
        public static SubCommand Parse(string input)
        {
            if (string.IsNullOrEmpty(input))
            {
                throw new System.ArgumentException($"'{nameof(input)}' cannot be null or empty.", nameof(input));
            }

            var value = input.Split(' ');
            return new SubCommand(value[0], int.Parse(value[1]));
        }
    }
}
