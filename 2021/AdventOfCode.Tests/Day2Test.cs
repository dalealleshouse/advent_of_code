namespace AdventOfCode.Tests
{
    using AdventOfCode.Submarine;
    using Xunit;

    public class Day2Test
    {
        [Fact]
        public void TestInput()
        {
            var data = InputParser.ParseCommands("input_data/day2-test.txt");
            var result = Day2.CalculatePosition(data, new SimpleSub());

            Assert.Equal((15, 10), result);
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = InputParser.ParseCommands("input_data/day2-1.txt");
            var result = Day2.CalculatePosition(data, new SimpleSub());

            Assert.Equal((1996, 1022), result);
        }

        [Fact]
        public void TestInputTwo()
        {
            var data = InputParser.ParseCommands("input_data/day2-test.txt");
            var result = Day2.CalculatePosition(data, new Sub());

            Assert.Equal((15, 60), result);
        }

        [Fact]
        public void PuzzelTwo()
        {
            var data = InputParser.ParseCommands("input_data/day2-1.txt");
            var result = Day2.CalculatePosition(data, new Sub());

            Assert.Equal((1996, 972980), result);
        }
    }
}
