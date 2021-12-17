namespace AdventOfCode.Day16
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class Packet
    {
        private readonly string raw;

        public Packet(string raw)
        {
            this.raw = raw;
            this.Version = this.GetVersion();
            this.TypeId = this.GetTypeId();
            this.HeaderSize = this.GetHeaderSize();
        }

        public int Version { get; private set; }

        public int TypeId { get; private set; }

        public int HeaderSize { get; private set; }

        public long VersionSum() => this.Version + this.SubPackets().Sum(p => p.VersionSum());

        public long GetValue()
        {
            switch (this.TypeId)
            {
                case 0:
                    return this.SubPackets().Sum(p => p.GetValue());
                case 1:
                    return this.SubPackets().Aggregate(1L, (acc, val) => acc * val.GetValue());
                case 2:
                    return this.SubPackets().Min(p => p.GetValue());
                case 3:
                    return this.SubPackets().Max(p => p.GetValue());
                case 4:
                    return this.GetLiteralValue();
                case 5:
                    var gt1 = this.SubPackets().First().GetValue();
                    var gt2 = this.SubPackets().Last().GetValue();
                    return (gt1 > gt2) ? 1 : 0;
                case 6:
                    var lt1 = this.SubPackets().First().GetValue();
                    var lt2 = this.SubPackets().Last().GetValue();
                    return (lt1 < lt2) ? 1 : 0;
                case 7:
                    var e1 = this.SubPackets().First().GetValue();
                    var e2 = this.SubPackets().Last().GetValue();
                    return (e1 == e2) ? 1 : 0;
                default:
                    throw new InvalidOperationException();
            }
        }

        public IEnumerable<Packet> SubPackets()
        {
            // literals don't have sub packets
            if (this.TypeId == 4)
            {
                yield break;
            }

            if (this.GetLengthTypeId() == 0)
            {
                var len = this.Get15BitSubPacketLength();

                var subs = this.raw.Substring(this.HeaderSize, len);
                var pos = 0;
                while (pos < len)
                {
                    var sub = new Packet(subs.Substring(pos));
                    pos += sub.NumOfBits();
                    yield return sub;
                }

                yield break;
            }

            var subpackets = this.Get11BitNumberofSubPackets();
            var start = this.HeaderSize;

            for (int i = 0; i < subpackets; i++)
            {
                var packet = new Packet(this.raw.Substring(start));
                start += packet.NumOfBits();

                yield return packet;
            }

            yield break;
        }

        private int NumOfBits()
        {
            if (this.TypeId == 4)
            {
                var pos = this.HeaderSize;
                while (this.raw.Substring(pos, 1) != "0")
                {
                    pos += 5;
                }

                return pos + 5;
            }

            if (this.GetLengthTypeId() == 0)
            {
                return this.Get15BitSubPacketLength() + this.HeaderSize;
            }

            return this.SubPackets().Sum(x => x.NumOfBits()) + this.HeaderSize;
        }

        private long GetLiteralValue()
        {
            if (this.TypeId != 4)
            {
                throw new InvalidOperationException();
            }

            var bits = this.raw.Substring(this.HeaderSize, this.NumOfBits() - this.HeaderSize);
            var val = string.Empty;
            var pos = 1;
            while (pos < bits.Length)
            {
                val += bits.Substring(pos, 4);
                pos += 5;
            }

            return Convert.ToInt64(val, 2);
        }

        private int GetHeaderSize()
        {
            if (this.TypeId == 4)
            {
                return 6;
            }

            if (this.GetLengthTypeId() == 0)
            {
                return 22;
            }

            return 18;
        }

        private int Get15BitSubPacketLength() =>
            Convert.ToInt32(this.raw.Substring(7, 15), 2);

        private int Get11BitNumberofSubPackets() =>
            Convert.ToInt32(this.raw.Substring(7, 11), 2);

        private int GetVersion() => Convert.ToInt32(this.raw.Substring(0, 3), 2);

        private int GetTypeId() => Convert.ToInt32(this.raw.Substring(3, 3), 2);

        private int GetLengthTypeId() => Convert.ToInt32(this.raw.Substring(6, 1), 2);
    }
}
