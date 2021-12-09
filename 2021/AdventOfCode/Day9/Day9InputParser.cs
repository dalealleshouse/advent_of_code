namespace AdventOfCode.Day9
{
    using System.Collections.Generic;
    using System.Linq;

    public static class Day9InputParser
    {
        public static IEnumerable<IEnumerable<int>> ParseHeightMap(string path)
        {
            return InputParser.Parse<IEnumerable<int>>(path, x =>
            {
                return x.ToCharArray().Select(x => int.Parse(x.ToString()));
            });
        }
    }
}
