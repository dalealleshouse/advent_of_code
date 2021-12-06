namespace AdventOfCode.Day5
{
    using System.Collections.Generic;
    using System.IO;
    using System.Text.RegularExpressions;

    public static class Day5InputParser
    {
        public static IEnumerable<LineSegment> ParseSegments(string path)
        {
            var rx = new Regex(@"(?<x1>\d+),(?<y1>\d+) -> (?<x2>\d+),(?<y2>\d+)");
            return InputParser.Parse(path, x =>
            {
                var m = rx.Match(x);

                if (!m.Success)
                {
                    throw new InvalidDataException($"Unable to parse input = {x}");
                }

                return new LineSegment(
                        (int.Parse(m.Groups["x1"].Value), int.Parse(m.Groups["y1"].Value)),
                        (int.Parse(m.Groups["x2"].Value), int.Parse(m.Groups["y2"].Value)));
            });
        }
    }
}
