namespace AdventOfCode.Day6
{
    using System.Collections.Generic;
    using System.Linq;

    public struct LaternFishSchool
    {
        private IEnumerable<LaternFish> fish;

        public LaternFishSchool(IEnumerable<LaternFish> fish)
        {
            this.fish = fish;
        }

        public int SchoolSize => this.fish.Count();

        public LaternFishSchool SimulateDay()
        {
            return new LaternFishSchool(this.fish.SelectMany(x => x.NextDay()));
        }
    }
}
