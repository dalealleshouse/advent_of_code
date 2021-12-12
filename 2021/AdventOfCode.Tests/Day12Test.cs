namespace AdventOfCode.Tests
{
    using AdventOfCode.Day12;
    using Xunit;

    public class Day12Test
    {
        [Fact]
        public void TestInput()
        {
            var sut = new CaveGraph(InputParser.ParseString("input_data/day12-test.txt"));

            Assert.Equal(10, sut.FindPaths());
        }

        [Fact]
        public void PuzzelOne()
        {
            var sut = new CaveGraph(InputParser.ParseString("input_data/day12-1.txt"));

            Assert.Equal(4495, sut.FindPaths());
        }

        [Fact]
        public void TestInputTwo()
        {
            var sut = new CaveGraph(InputParser.ParseString("input_data/day12-test.txt"));

            Assert.Equal(36, sut.FindPaths2());
        }

        [Fact]
        public void PuzzelTwo()
        {
            var sut = new CaveGraph(InputParser.ParseString("input_data/day12-1.txt"));

            Assert.Equal(131254, sut.FindPaths2());
        }
    }
}
