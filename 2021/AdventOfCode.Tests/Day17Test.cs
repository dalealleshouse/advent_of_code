namespace AdventOfCode.Tests
{
    using System;
    using AdventOfCode.Day17;
    using Xunit;

    public class Day17Test
    {
        [Fact]
        public void TestInput()
        {
            /* target area: x=20..30, y=-10..-5 */
            var sut = new TrajectoryCalculator((20, 30), (-10, -5));
            Assert.Equal(45, sut.HighestY());
        }

        [Fact]
        public void PuzzelOne()
        {
            /* target area: x=111..161, y=-154..-101 */
            var sut = new TrajectoryCalculator((111, 161), (-154, -101));
            Assert.Equal(11781, sut.HighestY());
        }

        [Fact]
        public void TestInputTwo()
        {
            /* target area: x=20..30, y=-10..-5 */
            var sut = new TrajectoryCalculator((20, 30), (-10, -5));
            Assert.Equal(112, sut.DistinctVelocity());
        }

        [Fact]
        public void PuzzelTwo()
        {
            /* target area: x=111..161, y=-154..-101 */
            var sut = new TrajectoryCalculator((111, 161), (-154, -101));
            Assert.Equal(4531, sut.DistinctVelocity());
        }
    }
}
