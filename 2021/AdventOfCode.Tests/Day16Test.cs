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
            Assert.Equal(6, PacketFactory.CreatePacket("D2FE28").VersionSum());
            Assert.Equal(9, PacketFactory.CreatePacket("38006F45291200").VersionSum());
            Assert.Equal(16, PacketFactory.CreatePacket("8A004A801A8002F478").VersionSum());
            Assert.Equal(14, PacketFactory.CreatePacket("EE00D40C823060").VersionSum());
            Assert.Equal(12, PacketFactory.CreatePacket("620080001611562C8802118E34").VersionSum());
            Assert.Equal(23, PacketFactory.CreatePacket("C0015000016115A2E0802F182340").VersionSum());
            Assert.Equal(31, PacketFactory.CreatePacket("A0016C880162017C3686B18A3D4780").VersionSum());
        }

        [Fact]
        public void PuzzelOne()
        {
            Assert.Equal(979, PacketFactory.CreatePacket(InputParser.ParseString("input_data/day16-1.txt").First()).VersionSum());
        }

        [Fact]
        public void TestInputTwo()
        {
            Assert.Equal(3, PacketFactory.CreatePacket("C200B40A82").GetValue());
            Assert.Equal(54, PacketFactory.CreatePacket("04005AC33890").GetValue());
            Assert.Equal(7, PacketFactory.CreatePacket("880086C3E88112").GetValue());
            Assert.Equal(9, PacketFactory.CreatePacket("CE00C43D881120").GetValue());
            Assert.Equal(1, PacketFactory.CreatePacket("D8005AC2A8F0").GetValue());
            Assert.Equal(0, PacketFactory.CreatePacket("F600BC2D8F").GetValue());
            Assert.Equal(0, PacketFactory.CreatePacket("9C005AC2F8F0").GetValue());
            Assert.Equal(1, PacketFactory.CreatePacket("9C0141080250320F1802104A08").GetValue());
        }

        [Fact]
        public void PuzzelTwo()
        {
            Assert.Equal(277110354175, PacketFactory.CreatePacket(InputParser.ParseString("input_data/day16-1.txt").First()).GetValue());
        }
    }
}
