namespace AdventOfCode.Day13
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class InstructionManual
    {
        private List<Point> points = new();
        private List<Fold> folds = new();
        private int maxX;
        private int maxY;
        private char[,] grid;

        public InstructionManual(IEnumerable<string> data)
        {
            foreach (var d in data)
            {
                if (d == string.Empty)
                {
                    continue;
                }

                if (d.StartsWith("fold along"))
                {
                    var f = d.Split(" ");
                    f = f[2].Split("=");
                    this.folds.Add(new Fold(f[0], int.Parse(f[1])));
                    continue;
                }

                var p = d.Split(",");
                this.points.Add(new Point(int.Parse(p[0]), int.Parse(p[1])));
            }

            this.maxX = this.points.Max(x => x.X) + 1;
            this.maxY = this.points.Max(x => x.Y) + 1;

            this.grid = new char[this.maxY, this.maxX];
            foreach (var p in this.points)
            {
                this.SetGridValue(p.X, p.Y);
            }
        }

        public int FirstFold()
        {
            this.FoldManual(this.folds.First());

            var count = 0;
            for (int x = 0; x < this.maxX; x++)
            {
                for (int y = 0; y < this.maxY; y++)
                {
                    if (this.grid[y, x] == '#')
                    {
                        count++;
                    }
                }
            }

            return count;
        }

        public void AllFolds()
        {
            foreach (var f in this.folds)
            {
                this.FoldManual(f);
            }

            this.PrintGrid();
        }

        private void FoldManual(Fold fold)
        {
            var oldGrid = this.grid;
            var oldMaxY = this.maxY;
            var oldMaxX = this.maxX;

            if (fold.Direction == "y")
            {
                this.maxY /= 2;
            }
            else
            {
                this.maxX /= 2;
            }

            this.grid = new char[this.maxY, this.maxX];

            for (int x = 0; x < this.maxX; x++)
            {
                for (int y = 0; y < this.maxY; y++)
                {
                    this.grid[y, x] = oldGrid[y, x];
                }
            }

            if (fold.Direction == "y")
            {
                for (int x = 0; x < this.maxX; x++)
                {
                    for (int y = 0; y < this.maxY; y++)
                    {
                        var oldy = oldMaxY - y - 1;
                        if (oldGrid[oldy, x] == '#')
                        {
                            this.SetGridValue(x, y);
                        }
                    }
                }
            }
            else
            {
                for (int x = 0; x < this.maxX; x++)
                {
                    for (int y = 0; y < this.maxY; y++)
                    {
                        var oldx = oldMaxX - x - 1;
                        if (oldGrid[y, oldx] == '#')
                        {
                            this.SetGridValue(x, y);
                        }
                    }
                }
            }
        }

        private void SetGridValue(int x, int y) => this.grid[y, x] = '#';

        private char GridValue(int x, int y) => this.grid[y, x] == default(char) ? '.' : this.grid[y, x];

        private void PrintGrid()
        {
            Console.WriteLine($"{this.maxX}-{this.maxY}");
            for (int y = 0; y < this.maxY; y++)
            {
                for (int x = 0; x < this.maxX; x++)
                {
                    Console.Write($"{this.GridValue(x, y)}");
                }

                Console.WriteLine();
            }
        }

        public record Point(int X, int Y);

        public record Fold(string Direction, int Val);
    }
}
