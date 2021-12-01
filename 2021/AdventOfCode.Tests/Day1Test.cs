namespace AdventOfCode.Tests
{
    using Xunit;

    public class Day1Test
    {
        [Fact]
        public void TestInput()
        {
            var data = InputParser.Parse("input_data/day1-test.txt");
            var result = Day1.CountIncreasing(data);

            Assert.Equal(7, result);
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = InputParser.Parse("input_data/day1-1.txt");
            var result = Day1.CountIncreasing(data);

            Assert.Equal(1559, result);
        }

        [Fact]
        public void TestInputTwo()
        {
            var data = InputParser.Parse("input_data/day1-test.txt");
            var result = Day1.CountIncreasingWithinSlidingWindow(data, 3);

            Assert.Equal(5, result);
        }

        [Fact]
        public void PuzzelTwo()
        {
            var data = InputParser.Parse("input_data/day1-1.txt");
            var result = Day1.CountIncreasingWithinSlidingWindow(data, 3);

            Assert.Equal(1600, result);
        }
    }
}
