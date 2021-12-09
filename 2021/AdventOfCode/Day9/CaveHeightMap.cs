namespace AdventOfCode.Day9
{
    using System.Collections.Generic;
    using System.Linq;

    public class CaveHeightMap
    {
        private List<List<int>> grid = new();
        private int height;
        private int width;

        public CaveHeightMap(IEnumerable<IEnumerable<int>> map)
        {
            foreach (var row in map)
            {
                this.grid.Add(row.ToList());
            }

            this.height = this.grid.Count;
            this.width = this.grid[0].Count;
        }

        public int Basins() => this.LowPoints()
                .Select(this.BasinSize)
                .OrderByDescending(x => x)
                .Take(3)
                .Aggregate(1, (acc, val) => acc * val);

        public int RiskLevel() => this.LowPoints()
            .Sum(x => this.grid[x.Row][x.Column] + 1);

        private List<(int Row, int Column)> LowPoints()
        {
            List<(int, int)> lowPoints = new();
            for (int i = 0; i < this.height; i++)
            {
                for (int j = 0; j < this.width; j++)
                {
                    if (this.GetNeighbors(i, j).All(x => x > this.grid[i][j]))
                    {
                        lowPoints.Add((i, j));
                    }
                }
            }

            return lowPoints;
        }

        private int BasinSize((int Row, int Column) point)
        {
            var size = 1;
            var value = this.grid[point.Row][point.Column];
            this.grid[point.Row][point.Column] = 9;

            if (point.Column > 0)
            {
                var top = this.grid[point.Row][point.Column - 1];
                if (top != 9 && top > value)
                {
                    size += this.BasinSize((point.Row, point.Column - 1));
                }
            }

            if (point.Row > 0)
            {
                var left = this.grid[point.Row - 1][point.Column];
                if (left != 9 && left > value)
                {
                    size += this.BasinSize((point.Row - 1, point.Column));
                }
            }

            if (point.Column < this.width - 1)
            {
                var bottom = this.grid[point.Row][point.Column + 1];
                if (bottom != 9 && bottom > value)
                {
                    size += this.BasinSize((point.Row, point.Column + 1));
                }
            }

            if (point.Row < this.height - 1)
            {
                var right = this.grid[point.Row + 1][point.Column];
                if (right != 9 && right > value)
                {
                    size += this.BasinSize((point.Row + 1, point.Column));
                }
            }

            return size;
        }

        private List<int> GetNeighbors(int row, int column)
        {
            var neighbors = new List<int>();
            if (column > 0)
            {
                neighbors.Add(this.grid[row][column - 1]);
            }

            if (row > 0)
            {
                neighbors.Add(this.grid[row - 1][column]);
            }

            if (column < this.width - 1)
            {
                neighbors.Add(this.grid[row][column + 1]);
            }

            if (row < this.height - 1)
            {
                neighbors.Add(this.grid[row + 1][column]);
            }

            return neighbors;
        }
    }
}
