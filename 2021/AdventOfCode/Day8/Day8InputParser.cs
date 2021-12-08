namespace AdventOfCode.Day8
{
    using System.Collections.Generic;

    public static class Day8InputParser
    {
        public static IEnumerable<SevenSegmentDigitSignal> ParseSegments(string path)
        {
            return InputParser.Parse(path, x =>
            {
                var parts = x.Split('|');
                return new SevenSegmentDigitSignal(parts[0].Trim().Split(), parts[1].Trim().Split());
            });
        }
    }
}
