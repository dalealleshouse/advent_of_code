namespace AdventOfCode.Tests
{
    using Xunit;

    public class Day4Test
    {
        [Fact]
        public void TestInput()
        {
            var bingo = InputParser.ParseBingo("input_data/day4-test.txt");
            var winner = bingo.FindWinner();

            Assert.Equal(4512, winner.WinningNumber * bingo.SumBoard(winner.WinningBoard));
        }

        [Fact]
        public void PuzzelOne()
        {
            var bingo = InputParser.ParseBingo("input_data/day4-1.txt");
            var winner = bingo.FindWinner();

            Assert.Equal(71708, winner.WinningNumber * bingo.SumBoard(winner.WinningBoard));
        }

        [Fact]
        public void TestInputTwo()
        {
            var bingo = InputParser.ParseBingo("input_data/day4-test.txt");
            var winner = bingo.FindLastWinner();

            Assert.Equal(1924, winner.WinningNumber * bingo.SumBoard(winner.WinningBoard));
        }

        [Fact]
        public void PuzzelTwo()
        {
            var bingo = InputParser.ParseBingo("input_data/day4-1.txt");
            var winner = bingo.FindLastWinner();

            Assert.Equal(34726, winner.WinningNumber * bingo.SumBoard(winner.WinningBoard));
        }
    }
}
