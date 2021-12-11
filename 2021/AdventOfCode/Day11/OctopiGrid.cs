namespace AdventOfCode.Day11
{
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;

    public class OctopiGrid
    {
        private readonly int size;
        private int[,] octopi;

        public OctopiGrid(IEnumerable<IEnumerable<int>> data, int size)
        {
            this.size = size;

            this.octopi = new int[size, size];
            var temp = data.ToArray();

            for (int i = 0; i < size; i++)
            {
                var row = temp[i].ToArray();
                for (int j = 0; j < size; j++)
                {
                    this.octopi[i, j] = row[j];
                }
            }
        }

        public int Cycle(int count)
        {
            var flashes = 0;

            for (int x = 0; x < count; x++)
            {
                // Process Flashes
                for (int i = 0; i < this.size; i++)
                {
                    for (int j = 0; j < this.size; j++)
                    {
                        this.Flash((i, j));
                    }
                }

                // Count flashes
                for (int i = 0; i < this.size; i++)
                {
                    for (int j = 0; j < this.size; j++)
                    {
                        if (this.octopi[i, j] > 9)
                        {
                            flashes++;
                            this.octopi[i, j] = 0;
                        }
                    }
                }
            }

            return flashes;
        }

        public int FirstFullFlash()
        {
            var cycles = 1;

            while (this.Cycle(1) != 100)
            {
                cycles++;
            }

            return cycles;
        }

        public override string ToString()
        {
            var s = new StringBuilder();

            for (int i = 0; i < this.size; i++)
            {
                for (int j = 0; j < this.size; j++)
                {
                    s.Append(this.octopi[i, j]);
                }

                s.Append('\n');
            }

            return s.ToString();
        }

        private void Flash((int Row, int Column) point)
        {
            this.octopi[point.Row, point.Column]++;
            var val = this.octopi[point.Row, point.Column];

            if (val == 10)
            {
                foreach (var p in this.Neighbors(point))
                {
                    this.Flash(p);
                }
            }
        }

        private IEnumerable<(int Row, int Column)> Neighbors((int Row, int Column) subject)
        {
            var neighbors = new List<(int, int)>();

            // left
            if (subject.Column > 0)
            {
                neighbors.Add((subject.Row, subject.Column - 1));
            }

            // top
            if (subject.Row > 0)
            {
                neighbors.Add((subject.Row - 1, subject.Column));
            }

            // right
            if (subject.Column < this.size - 1)
            {
                neighbors.Add((subject.Row, subject.Column + 1));
            }

            // bottom
            if (subject.Row < this.size - 1)
            {
                neighbors.Add((subject.Row + 1, subject.Column));
            }

            // left top
            if (subject.Column > 0 && subject.Row > 0)
            {
                neighbors.Add((subject.Row - 1, subject.Column - 1));
            }

            // right top
            if (subject.Column < this.size - 1 && subject.Row > 0)
            {
                neighbors.Add((subject.Row - 1, subject.Column + 1));
            }

            // left bottom
            if (subject.Column > 0 && subject.Row < this.size - 1)
            {
                neighbors.Add((subject.Row + 1, subject.Column - 1));
            }

            // right bottom
            if (subject.Column < this.size - 1 && subject.Row < this.size - 1)
            {
                neighbors.Add((subject.Row + 1, subject.Column + 1));
            }

            return neighbors;
        }
    }
}
