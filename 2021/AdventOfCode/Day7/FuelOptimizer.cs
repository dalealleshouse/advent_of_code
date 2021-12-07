namespace AdventOfCode.Day7
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class FuelOptimizer
    {
        private readonly int[] data;

        public FuelOptimizer(IEnumerable<int> data)
        {
            this.data = data.ToArray();
        }

        public long OptimalFuelConsumption()
        {
            return this.AllCosts().Min();
        }

        public long OptimalCompoundFuelConsumption()
        {
            return this.AllCompoundCosts().Min();
        }

        private IEnumerable<long> AllCosts()
        {
            var min = this.data.Min();
            var iterations = this.data.Max() - min;

            for (int i = min; i < iterations; i++)
            {
                yield return this.data.Sum(x => Math.Abs(i - x));
            }
        }

        private IEnumerable<long> AllCompoundCosts()
        {
            var min = this.data.Min();
            var iterations = this.data.Max() - min;

            for (int i = min; i < iterations; i++)
            {
                yield return this.data.Sum(x => this.SumOfNaturalNumbers(Math.Abs(i - x)));
            }
        }

        private long SumOfNaturalNumbers(long val)
        {
            return val * (val + 1) / 2;
        }
    }
}
