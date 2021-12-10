namespace AdventOfCode.Tests
{
    using AdventOfCode.Day10;
    using Xunit;

    public class Day10Test
    {
        [Fact]
        public void TestInput()
        {
            var data = InputParser.ParseString("input_data/day10-test.txt");
            var sut = new SyntaxChecker(data);

            Assert.Equal(26397, sut.CalculateIncompleteScore());
        }

        [Fact]
        public void PuzzelOne()
        {
            var data = InputParser.ParseString("input_data/day10-1.txt");
            var sut = new SyntaxChecker(data);

            Assert.Equal(387363, sut.CalculateIncompleteScore());
        }

        [Fact]
        public void TestInputTwo()
        {
            var data = InputParser.ParseString("input_data/day10-test.txt");
            var sut = new SyntaxChecker(data);

            Assert.Equal(288957, sut.AutoCompleteScore());
        }

        [Fact]
        public void PuzzelTwo()
        {
            var data = InputParser.ParseString("input_data/day10-1.txt");
            var sut = new SyntaxChecker(data);

            Assert.Equal(4330777059, sut.AutoCompleteScore());
        }
    }
}
