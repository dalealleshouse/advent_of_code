namespace AdventOfCode.Day10
{
    using System.Collections.Generic;
    using System.Linq;

    public class SyntaxChecker
    {
        private readonly Stack<char> evalStack = new();

        private readonly Dictionary<char, int> points = new()
        {
            { ')', 3 },
            { ']', 57 },
            { '}', 1197 },
            { '>', 25137 },
            { '-', 0 },
        };

        private readonly Dictionary<char, int> acPoints = new()
        {
            { ')', 1 },
            { ']', 2 },
            { '}', 3 },
            { '>', 4 },
        };

        private readonly Dictionary<char, char> matches = new()
        {
            { '(', ')' },
            { '[', ']' },
            { '{', '}' },
            { '<', '>' },
        };

        private readonly IEnumerable<string> data;

        public SyntaxChecker(IEnumerable<string> data)
        {
            this.data = data;
        }

        public int CalculateIncompleteScore() => this.data.Sum(this.IncompleteScore);

        public long AutoCompleteScore()
        {
            var scores = this.data
                .Where(x => this.IncompleteScore(x) == 0)
                .Select(this.CompleteString)
                .Select(this.AutoCompleteScore)
                .OrderBy(x => x)
                .ToArray();

            return scores[scores.Count() / 2];
        }

        private long AutoCompleteScore(IEnumerable<char> input)
        {
            long total = 0;

            foreach (var c in input)
            {
                total *= 5;
                total += this.acPoints[c];
            }

            return total;
        }

        private IEnumerable<char> CompleteString(string input)
        {
            this.evalStack.Clear();

            foreach (var c in input)
            {
                if (this.matches.ContainsKey(c))
                {
                    this.evalStack.Push(c);
                    continue;
                }

                this.evalStack.Pop();
            }

            return this.evalStack.Select(x => this.matches[x]);
        }

        private int IncompleteScore(string input)
        {
            this.evalStack.Clear();
            foreach (var c in input)
            {
                if (this.matches.ContainsKey(c))
                {
                    this.evalStack.Push(c);
                    continue;
                }

                if (this.matches[this.evalStack.Peek()] == c)
                {
                    this.evalStack.Pop();
                    continue;
                }

                return this.points[c];
            }

            return 0;
        }
    }
}
