namespace AdventOfCode.Tests
{
    using Xunit;

    public class Day3Test
    {
        [Fact]
        public void TestInput()
        {
            var data = InputParser.ParseBinaryString("input_data/day3-test.txt");
            var result = Day3.PowerConsumption(data);

            Assert.Equal((22, 9), result);
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = InputParser.ParseBinaryString("input_data/day3-1.txt");
            var result = Day3.PowerConsumption(data);

            Assert.Equal((2277, 1818), result);
        }

        [Fact]
        public void TestInputTwo()
        {
            var o = Day3.OxygenGeneratorRating(InputParser.ParseBinaryString("input_data/day3-test.txt"));
            var co = Day3.CO2ScrubberRating(InputParser.ParseBinaryString("input_data/day3-test.txt"));

            Assert.Equal(23, o);
            Assert.Equal(10, co);
        }

        [Fact]
        public void PuzzelTwo()
        {
            var o = Day3.OxygenGeneratorRating(InputParser.ParseBinaryString("input_data/day3-1.txt"));
            var co = Day3.CO2ScrubberRating(InputParser.ParseBinaryString("input_data/day3-1.txt"));

            Assert.Equal(2539, o);
            Assert.Equal(709, co);
        }
    }
}
