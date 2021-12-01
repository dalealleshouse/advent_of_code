namespace AdventOfCode
{
    using System;
    using System.Collections.Generic;
    using System.IO;

    public static class InputParser
    {
        public static IEnumerable<int> Parse(string path)
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
                yield return int.Parse(line);
            }
        }
    }
}
