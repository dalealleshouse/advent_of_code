namespace AdventOfCode.Tests
{
    using System;
    using System.Linq;
    using AdventOfCode.Day6;
    using Xunit;

    public class Day6Test
    {
        [Fact]
        public void TestInput()
        {
            var fish = InputParser.ParseDelimited("input_data/day6-test.txt");
            var school = new LaternFishSchool(fish);

            for (int i = 0; i < 80; i++)
            {
                school = school.SimulateDay();
            }

            Assert.Equal(5934, school.SchoolSize);
        }

        [Fact]
        public void PuzzelOne()
        {
            var fish = InputParser.ParseDelimited("input_data/day6-1.txt");
            var school = new LaternFishSchool(fish);

            for (int i = 0; i < 80; i++)
            {
                school = school.SimulateDay();
            }

            Assert.Equal(394994, school.SchoolSize);
        }

        [Fact]
        public void TestInputTwo()
        {
            var fish = InputParser.ParseDelimited("input_data/day6-1.txt");
            var school = new LaternFishSchool(fish);

            for (int i = 0; i < 256; i++)
            {
                school = school.SimulateDay();
            }

            Assert.Equal(26984457539, school.SchoolSize);
        }

        /* [Fact] */
        /* public void PuzzelTwo() */
        /* { */
        /*     var segments = InputParser.ParseSegments("input_data/day5-1.txt"); */
        /*     var g = new Grid(1000); */
        /*     g.LoadLineSegments(segments); */

        /*     Assert.Equal(21698, g.CountOverlaps()); */
        /* } */
    }
}
