namespace AdventOfCode.Tests
{
    using AdventOfCode.Day3;
    using Xunit;

    public class Day3Test
    {
        [Fact]
        public void TestInput()
        {
            var data = Day3InputParser.ParseBinaryString("input_data/day3-test.txt");
            var result = RatingDeviner.PowerConsumption(data);

            Assert.Equal((22, 9), result);
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = Day3InputParser.ParseBinaryString("input_data/day3-1.txt");
            var result = RatingDeviner.PowerConsumption(data);

            Assert.Equal((2277, 1818), result);
        }

        [Fact]
        public void TestInputTwo()
        {
            var o = RatingDeviner.OxygenGeneratorRating(
                    Day3InputParser.ParseBinaryString("input_data/day3-test.txt"));
            var co = RatingDeviner.CO2ScrubberRating(
                    Day3InputParser.ParseBinaryString("input_data/day3-test.txt"));

            Assert.Equal(23, o);
            Assert.Equal(10, co);
        }

        [Fact]
        public void PuzzelTwo()
        {
            var o = RatingDeviner.OxygenGeneratorRating(
                    Day3InputParser.ParseBinaryString("input_data/day3-1.txt"));
            var co = RatingDeviner.CO2ScrubberRating(
                    Day3InputParser.ParseBinaryString("input_data/day3-1.txt"));

            Assert.Equal(2539, o);
            Assert.Equal(709, co);
        }
    }
}
