namespace AdventOfCode.Day5
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class Grid
    {
        private int gridSize;
        private int[,] grid;

        public Grid(int gridSize)
        {
            this.gridSize = gridSize;
            this.grid = new int[gridSize, gridSize];
        }

        public void LoadLineSegments(IEnumerable<LineSegment> segments)
        {
            foreach (var seg in segments)
            {
                (int X, int Y) start = seg.Begin;
                (int X, int Y) end = seg.End;

                // No need for complex math here...
                /* var slope = (start.X == end.X) ? 0 : (end.Y - start.Y) / (end.X - start.X); */
                var xdir = (start.X == end.X) ? 0 : (start.X < end.X) ? 1 : -1;
                var ydir = (start.Y == end.Y) ? 0 : (start.Y < end.Y) ? 1 : -1;

                int count = 0;
                var point = start;
                while ((point.X != end.X + xdir || point.Y != end.Y + ydir) && count < this.gridSize)
                {
                    this.IncrementPoint(point);
                    point.X += xdir;
                    point.Y += ydir;

                    count++;
                }
            }
        }

        public void LoadHVLineSegments(IEnumerable<LineSegment> segments)
        {
            foreach (var seg in segments)
            {
                if (seg.Begin.X == seg.End.X)
                {
                    var ybegin = Math.Min(seg.Begin.Y, seg.End.Y);
                    var yend = Math.Max(seg.Begin.Y, seg.End.Y);

                    while (ybegin <= yend)
                    {
                        this.IncrementPoint((seg.Begin.X, ybegin));
                        ybegin++;
                    }
                }

                if (seg.Begin.Y == seg.End.Y)
                {
                    var xbegin = Math.Min(seg.Begin.X, seg.End.X);
                    var xend = Math.Max(seg.Begin.X, seg.End.X);

                    while (xbegin <= xend)
                    {
                        this.IncrementPoint((xbegin, seg.Begin.Y));
                        xbegin++;
                    }
                }
            }
        }

        public int CountOverlaps()
        {
            return this.Flatten(this.grid).Where(x => x > 1).Count();
        }

        public IEnumerable<T> Flatten<T>(T[,] map)
        {
            for (int row = 0; row < map.GetLength(0); row++)
            {
                for (int col = 0; col < map.GetLength(1); col++)
                {
                    yield return map[row, col];
                }
            }
        }

        private void IncrementPoint((int X, int Y) point)
        {
            this.grid[point.Y, point.X]++;
        }

        private void PrintGrid()
        {
            for (int i = 0; i < this.gridSize; i++)
            {
                for (int j = 0; j < this.gridSize; j++)
                {
                    Console.Write($"{this.grid[i, j]} ");
                }

                Console.WriteLine();
            }
        }
    }
}
