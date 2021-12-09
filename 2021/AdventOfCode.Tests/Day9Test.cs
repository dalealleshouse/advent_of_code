namespace AdventOfCode.Tests
{
    using AdventOfCode.Day9;
    using Xunit;

    public class Day9Test
    {
        [Fact]
        public void TestInput()
        {
            var data = Day9InputParser.ParseHeightMap("input_data/day9-test.txt");
            var sut = new CaveHeightMap(data);

            Assert.Equal(15, sut.RiskLevel());
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = Day9InputParser.ParseHeightMap("input_data/day9-1.txt");
            var sut = new CaveHeightMap(data);

            Assert.Equal(452, sut.RiskLevel());
        }

        [Fact]
        public void TestInputTwo()
        {
            var data = Day9InputParser.ParseHeightMap("input_data/day9-test.txt");
            var sut = new CaveHeightMap(data);

            Assert.Equal(1134, sut.Basins());
        }

        [Fact]
        public void PuzzelTwo()
        {
            var data = Day9InputParser.ParseHeightMap("input_data/day9-1.txt");
            var sut = new CaveHeightMap(data);

            Assert.Equal(1263735, sut.Basins());
        }
    }
}
