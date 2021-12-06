namespace AdventOfCode.Day6
{
    using System.Collections.Generic;
    using System.Linq;

    public class LaternFishSchool
    {
        private Dictionary<int, long> fishCatalog = new()
        {
            { 0, 0 },
            { 1, 0 },
            { 2, 0 },
            { 3, 0 },
            { 4, 0 },
            { 5, 0 },
            { 6, 0 },
            { 7, 0 },
            { 8, 0 },
        };

        public LaternFishSchool(IEnumerable<int> fish)
        {
            foreach (var f in fish)
            {
                this.fishCatalog[f] += 1;
            }
        }

        public long SchoolSize()
        {
            return this.fishCatalog.Sum(f => f.Value);
        }

        public void SimulateDay()
        {
            var fishAtZero = this.fishCatalog[0];

            for (int i = 1; i < 9; i++)
            {
                this.fishCatalog[i - 1] = this.fishCatalog[i];
                this.fishCatalog[i] = 0;
            }

            this.fishCatalog[6] += fishAtZero;
            this.fishCatalog[8] += fishAtZero;
        }
    }
}
