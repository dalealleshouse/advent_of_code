namespace AdventOfCode.Tests
{
    using AdventOfCode.Day8;
    using Xunit;

    public class Day8Test
    {
        [Fact]
        public void TestInput()
        {
            var data = Day8InputParser.ParseSegments("input_data/day8-test.txt");
            var sut = new SignalProcessor(data);

            Assert.Equal(26, sut.CountKnownSignalsInOutput());
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = Day8InputParser.ParseSegments("input_data/day8-1.txt");
            var sut = new SignalProcessor(data);

            Assert.Equal(470, sut.CountKnownSignalsInOutput());
        }

        [Fact]
        public void TestInputTwo()
        {
            var data = Day8InputParser.ParseSegments("input_data/day8-test.txt");
            var sut = new SignalProcessor(data);

            Assert.Equal(61229, sut.SumOfOutputValues());
        }

        [Fact]
        public void PuzzelTwo()
        {
            var data = Day8InputParser.ParseSegments("input_data/day8-1.txt");
            var sut = new SignalProcessor(data);

            Assert.Equal(989396, sut.SumOfOutputValues());
        }
    }
}
