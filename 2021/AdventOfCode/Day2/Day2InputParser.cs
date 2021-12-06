namespace AdventOfCode.Day2
{
    using System.Collections.Generic;

    public static class Day2InputParser
    {
        public static IEnumerable<SubCommand> ParseCommands(string path) =>
            InputParser.Parse(path, SubCommand.Parse);
    }
}
