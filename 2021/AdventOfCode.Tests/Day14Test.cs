namespace AdventOfCode.Tests
{
    using AdventOfCode.Day14;
    using Xunit;

    public class Day14Test
    {
        [Fact]
        public void TestInput()
        {
            var sut = new PolymerSolver(InputParser.ParseString("input_data/day14-test.txt"));

            Assert.Equal(1588, sut.MostCommonMinusLeastCommon(10));
        }

        [Fact]
        public void PuzzelOne()
        {
            var sut = new PolymerSolver(InputParser.ParseString("input_data/day14-1.txt"));

            Assert.Equal(3230, sut.MostCommonMinusLeastCommon(10));
        }

        [Fact]
        public void TestInputTwo()
        {
            var sut = new PolymerSolver(InputParser.ParseString("input_data/day14-test.txt"));

            Assert.Equal(2188189693529, sut.MostCommonMinusLeastCommon(40));
        }

        [Fact]
        public void PuzzelTwo()
        {
            var sut = new PolymerSolver(InputParser.ParseString("input_data/day14-1.txt"));

            Assert.Equal(3542388214529, sut.MostCommonMinusLeastCommon(40));
        }
    }
}
