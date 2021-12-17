namespace AdventOfCode.Day17
{
    using System;

    public class TrajectoryCalculator
    {
        private readonly Range xRange;
        private readonly Range yRange;

        public TrajectoryCalculator((int Min, int Max) xRange, (int Min, int Max) yRange)
        {
            this.xRange = new Range(xRange.Min, xRange.Max);
            this.yRange = new Range(yRange.Min, yRange.Max);
        }

        public int DistinctVelocity() => this.BruteForce().Unique;

        public int HighestY() => this.BruteForce().High;

        public int Simulate(int velX, int velY)
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
                    return maxH;
                }

                if (pos.X > this.xRange.Max || pos.Y < this.yRange.Min)
                {
                    return int.MinValue;
                }
            }
        }

        private (int High, int Unique) BruteForce()
        {
            int count = 0;
            var highest = int.MinValue;

            var yspace = this.GetSearchSpace(this.yRange);
            var xspace = this.GetSearchSpace(this.xRange);

            for (int y = yspace * -1; y < yspace; y++)
            {
                for (int x = xspace * -1; x < xspace; x++)
                {
                    var result = this.Simulate(x, y);
                    highest = Math.Max(highest, result);
                    if (result > int.MinValue)
                    {
                        count++;
                    }
                }
            }

            return (highest, count);
        }

        // I'm not sure if this is correct, but it's better than my previous approach and I'm getting correct answers
        private int GetSearchSpace(Range range) => Math.Max(Math.Abs(range.Min), Math.Abs(range.Max)) + 1;
    }

    public record Range(int Min, int Max);

    public record Postion(int X, int Y)
    {
        public Postion Add((int X, int Y) pos) => new Postion(this.X + pos.X, this.Y + pos.Y);

        public bool Within(Range xRange, Range yRange)
        {
            return this.X >= xRange.Min &&
                this.X <= xRange.Max &&
                this.Y >= yRange.Min &&
                this.Y <= yRange.Max;
        }
    }
}
