namespace AdventOfCode.Day4
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;

    public static class Day4InputParser
    {
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
    }
}
