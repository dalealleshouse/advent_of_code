namespace AdventOfCode.Day11
{
    using System.Collections.Generic;
    using System.Linq;

    public static class Day11InputParser
    {
        public static IEnumerable<IEnumerable<int>> ParseGrid(string path)
        {
            return InputParser.Parse<IEnumerable<int>>(path, x =>
            {
                return x.ToCharArray().Select(x => int.Parse(x.ToString()));
            });
        }
    }
}
