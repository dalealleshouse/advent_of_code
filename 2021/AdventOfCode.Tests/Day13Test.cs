namespace AdventOfCode.Tests
{
    using AdventOfCode.Day13;
    using Xunit;

    public class Day13Test
    {
        [Fact]
        public void TestInput()
        {
            var sut = new InstructionManual(InputParser.ParseString("input_data/day13-test.txt"));

            Assert.Equal(17, sut.FirstFold());
        }

        [Fact]
        public void PuzzelOne()
        {
            var sut = new InstructionManual(InputParser.ParseString("input_data/day13-1.txt"));

            Assert.Equal(671, sut.FirstFold());
        }

        /* [Fact] */
        /* public void PuzzelTwo() */
        /* { */
        /*     var sut = new InstructionManual(InputParser.ParseString("input_data/day13-1.txt")); */
        /*     sut.AllFolds(); */
        /* } */
    }
}
