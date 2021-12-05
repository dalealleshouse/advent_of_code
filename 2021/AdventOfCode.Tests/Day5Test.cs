namespace AdventOfCode.Tests
{
    using AdventOfCode.Day5;
    using Xunit;

    public class Day5Test
    {
        [Fact]
        public void TestInput()
        {
            var segments = InputParser.ParseSegments("input_data/day5-test.txt");
            var g = new Grid(10);
            g.LoadHVLineSegments(segments);

            Assert.Equal(5, g.CountOverlaps());
        }

        [Fact]
        public void PuzzelOne()
        {
            var segments = InputParser.ParseSegments("input_data/day5-1.txt");
            var g = new Grid(1000);
            g.LoadHVLineSegments(segments);

            Assert.Equal(5294, g.CountOverlaps());
        }

        [Fact]
        public void TestInputTwo()
        {
            var segments = InputParser.ParseSegments("input_data/day5-test.txt");
            var g = new Grid(10);
            g.LoadLineSegments(segments);

            Assert.Equal(12, g.CountOverlaps());
        }

        [Fact]
        public void PuzzelTwo()
        {
            var segments = InputParser.ParseSegments("input_data/day5-1.txt");
            var g = new Grid(1000);
            g.LoadLineSegments(segments);

            Assert.Equal(21698, g.CountOverlaps());
        }
    }
}
