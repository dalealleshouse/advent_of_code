namespace AdventOfCode.Tests
{
    using AdventOfCode.Day7;
    using Xunit;

    public class Day7Test
    {
        [Fact]
        public void TestInput()
        {
            var data = InputParser.ParseDelimited("input_data/day7-test.txt");
            var optimizer = new FuelOptimizer(data);

            Assert.Equal(37, optimizer.OptimalFuelConsumption());
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = InputParser.ParseDelimited("input_data/day7-1.txt");
            var optimizer = new FuelOptimizer(data);

            Assert.Equal(328187, optimizer.OptimalFuelConsumption());
        }

        [Fact]
        public void TestInputTwo()
        {
            var data = InputParser.ParseDelimited("input_data/day7-test.txt");
            var optimizer = new FuelOptimizer(data);

            Assert.Equal(168, optimizer.OptimalCompoundFuelConsumption());
        }

        [Fact]
        public void PuzzelTwo()
        {
            var data = InputParser.ParseDelimited("input_data/day7-1.txt");
            var optimizer = new FuelOptimizer(data);

            Assert.Equal(91257582, optimizer.OptimalCompoundFuelConsumption());
        }
    }
}
