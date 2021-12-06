namespace AdventOfCode.Day6
{
    using System.Collections.Generic;

    public struct LaternFish
    {
        private readonly int cycle;

        public LaternFish(int cycle)
        {
            this.cycle = cycle;
        }

        public IEnumerable<LaternFish> NextDay()
        {
            if (this.cycle == 0)
            {
                return new LaternFish[] { new LaternFish(8), new LaternFish(6) };
            }

            return new LaternFish[] { new LaternFish(this.cycle - 1) };
        }
    }
}
