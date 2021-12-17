namespace AdventOfCode.Day17
{
    using System;

    public class TrajectoryCalculator
    {
        private readonly (int Min, int Max) xRange;
        private readonly (int Min, int Max) yRange;

        public TrajectoryCalculator((int Min, int Max) xRange, (int Min, int Max) yRange)
        {
            this.xRange = xRange;
            this.yRange = yRange;
        }

        public int DistinctVelocity()
        {
            var count = 0;

            var yspace = this.GetSearchSpace(this.yRange);
            var xspace = this.GetSearchSpace(this.xRange);

            for (int y = yspace * -1; y < yspace + 1; y++)
            {
                for (int x = xspace * -1; x < xspace + 1; x++)
                {
                    var result = this.Simulate(x, y);
                    if (result.Within)
                    {
                        count++;
                    }
                }
            }

            return count;
        }

        public int HighestY()
        {
            var highest = int.MinValue;

            var yspace = this.GetSearchSpace(this.yRange);
            var xspace = this.GetSearchSpace(this.xRange);

            for (int y = yspace * -1; y < yspace + 1; y++)
            {
                for (int x = xspace * -1; x < xspace + 1; x++)
                {
                    var result = this.Simulate(x, y);
                    if (result.Within)
                    {
                        highest = Math.Max(highest, result.MaxHeight);
                    }
                }
            }

            return highest;
        }

        public (bool Within, int MaxHeight) Simulate(int velX, int velY)
        {
            var pos = new Postion(0, 0);
            var maxH = int.MinValue;

            while (true)
            {
                pos = pos.Add((velX, velY));
                maxH = Math.Max(maxH, pos.Y);

                velY -= 1;

                if (velX > 0)
                {
                    velX -= 1;
                }
                else if (velX < 0)
                {
                    velX += 1;
                }

                if (pos.Within(this.xRange, this.yRange))
                {
                    return (true, maxH);
                }

                if (pos.X > this.xRange.Max || pos.Y < this.yRange.Min)
                {
                    return (false, 0);
                }
            }
        }

        // I'm not sure if this is correct, but it's better than my previous approach and I'm getting correct answers
        private int GetSearchSpace((int Min, int Max) range) => Math.Max(Math.Abs(range.Min), Math.Abs(range.Max));
    }

    public record Postion(int X, int Y)
    {
        public Postion Add((int X, int Y) pos) => new Postion(this.X + pos.X, this.Y + pos.Y);

        public Postion Add(Postion pos) => new Postion(this.X + pos.X, this.Y + pos.Y);

        public bool Within((int Min, int Max) xRange, (int Min, int Max) yRange)
        {
            return this.X >= xRange.Min &&
                this.X <= xRange.Max &&
                this.Y >= yRange.Min &&
                this.Y <= yRange.Max;
        }
    }
}
