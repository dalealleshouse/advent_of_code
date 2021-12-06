namespace AdventOfCode
{
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Text.RegularExpressions;
    using AdventOfCode.Day5;
    using AdventOfCode.Submarine;

    public static class InputParser
    {
        public static IEnumerable<int> Parse(string path) => Parse(path, int.Parse);

        public static IEnumerable<SubCommand> ParseCommands(string path) => Parse(path, SubCommand.Parse);

        public static IEnumerable<string> ParseString(string path) => Parse(path, x => x);

        public static IEnumerable<(int BitCount, BitArray Bits)> ParseBinaryString(string path) => Parse(path, x =>
        {
            return (x.Length, new BitArray(new int[] { Convert.ToInt32(x, 2) }));
        });

        public static IEnumerable<int> ParseDelimited(string path)
        {
            if (string.IsNullOrEmpty(path))
            {
                throw new ArgumentException($"'{nameof(path)}' cannot be null or empty.", nameof(path));
            }

            if (!File.Exists(path))
            {
                throw new ArgumentException($"'{path}' not found.", nameof(path));
            }

            return File.ReadLines(path).First().Split(',').Select(int.Parse);
        }

        public static Bingo ParseBingo(string path)
        {
            var first = true;
            var board = -1;
            List<int> numbers = null;
            List<List<int>> boards = new();

            foreach (string line in File.ReadLines(path))
            {
                if (first)
                {
                    numbers = line.Split(',')
                        .Select(int.Parse)
                        .ToList();
                    first = false;
                    continue;
                }

                if (line == string.Empty)
                {
                    boards.Add(new());
                    board++;
                    continue;
                }

                boards[board].AddRange(
                        line
                        .Split(new char[0], StringSplitOptions.RemoveEmptyEntries)
                        .Select(int.Parse));
            }

            return new Bingo(numbers, boards);
        }

        public static IEnumerable<LineSegment> ParseSegments(string path)
        {
            var rx = new Regex(@"(?<x1>\d+),(?<y1>\d+) -> (?<x2>\d+),(?<y2>\d+)");
            return Parse(path, x =>
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

        public static IEnumerable<T> Parse<T>(string path, Func<string, T> parser)
        {
            if (string.IsNullOrEmpty(path))
            {
                throw new ArgumentException($"'{nameof(path)}' cannot be null or empty.", nameof(path));
            }

            if (!File.Exists(path))
            {
                throw new ArgumentException($"'{path}' not found.", nameof(path));
            }

            foreach (string line in File.ReadLines(path))
            {
                yield return parser(line);
            }
        }
    }
}
