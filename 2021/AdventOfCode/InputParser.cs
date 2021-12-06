namespace AdventOfCode
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;

    public static class InputParser
    {
        public static IEnumerable<int> Parse(string path) => Parse(path, int.Parse);

        public static IEnumerable<string> ParseString(string path) => Parse(path, x => x);

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

            return Parse(path, x => x.Split(',').Select(int.Parse)).First();
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
