namespace AdventOfCode.Tests
{
    using AdventOfCode.Day2;
    using Xunit;

    public class Day2Test
    {
        [Fact]
        public void TestInput()
        {
            var data = Day2InputParser.ParseCommands("input_data/day2-test.txt");
            var result = new SimpleSub().CalculatePosition(data);

            Assert.Equal((15, 10), result);
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = Day2InputParser.ParseCommands("input_data/day2-1.txt");
            var result = new SimpleSub().CalculatePosition(data);

            Assert.Equal((1996, 1022), result);
        }

        [Fact]
        public void TestInputTwo()
        {
            var data = Day2InputParser.ParseCommands("input_data/day2-test.txt");
            var result = new Sub().CalculatePosition(data);

            Assert.Equal((15, 60), result);
        }

        [Fact]
        public void PuzzelTwo()
        {
            var data = Day2InputParser.ParseCommands("input_data/day2-1.txt");
            var result = new Sub().CalculatePosition(data);

            Assert.Equal((1996, 972980), result);
        }
    }
}
