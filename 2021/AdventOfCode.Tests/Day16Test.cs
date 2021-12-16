namespace AdventOfCode.Tests
{
    using System.Linq;
    using AdventOfCode.Day16;
    using Xunit;

    public class Day16Test
    {
        [Fact]
        public void TestInput()
        {
            Assert.Equal(6, new PacketParser("D2FE28").SumOfVersion());
            Assert.Equal(9, new PacketParser("38006F45291200").SumOfVersion());
            Assert.Equal(16, new PacketParser("8A004A801A8002F478").SumOfVersion());
            Assert.Equal(14, new PacketParser("EE00D40C823060").SumOfVersion());
            Assert.Equal(12, new PacketParser("620080001611562C8802118E34").SumOfVersion());

            Assert.Equal(23, new PacketParser("C0015000016115A2E0802F182340").SumOfVersion());
            Assert.Equal(31, new PacketParser("A0016C880162017C3686B18A3D4780").SumOfVersion());
        }

        [Fact]
        public void PuzzelOne()
        {
            Assert.Equal(979, new PacketParser(InputParser.ParseString("input_data/day16-1.txt").First()).SumOfVersion());
        }

        [Fact]
        public void TestInputTwo()
        {
            Assert.Equal(3, new PacketParser("C200B40A82").Calculate());
            Assert.Equal(54, new PacketParser("04005AC33890").Calculate());
            Assert.Equal(7, new PacketParser("880086C3E88112").Calculate());
            Assert.Equal(9, new PacketParser("CE00C43D881120").Calculate());
            Assert.Equal(1, new PacketParser("D8005AC2A8F0").Calculate());
            Assert.Equal(0, new PacketParser("F600BC2D8F").Calculate());
            Assert.Equal(0, new PacketParser("9C005AC2F8F0").Calculate());
            Assert.Equal(1, new PacketParser("9C0141080250320F1802104A08").Calculate());
        }

        [Fact]
        public void PuzzelTwo()
        {
            Assert.Equal(277110354175, new PacketParser(InputParser.ParseString("input_data/day16-1.txt").First()).Calculate());
        }
    }
}
