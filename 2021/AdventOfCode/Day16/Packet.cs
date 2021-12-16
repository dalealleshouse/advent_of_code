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
        }

        public int Version { get; private set; }

        public int TypeId { get; private set; }

        public long GetValue()
        {
            switch (this.TypeId)
            {
                case 4:
                    return this.GetLiteralValue();
                case 0:
                    return this.SubPackets().Sum(p => p.GetValue());
                case 1:
                    return this.SubPackets().Aggregate(1L, (acc, val) => acc * val.GetValue());
                case 2:
                    return this.SubPackets().Min(p => p.GetValue());
                case 3:
                    return this.SubPackets().Max(p => p.GetValue());
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

        public int NumOfBits()
        {
            if (this.TypeId == 4)
            {
                var pos = 6;
                while (this.raw.Substring(pos, 1) != "0")
                {
                    pos += 5;
                }

                return pos + 5;
            }

            if (this.GetLengthTypeId() == 0)
            {
                return this.Get15BitSubPacketLength() + 7 + 15;
            }

            return this.SubPackets().Sum(x => x.NumOfBits()) + 7 + 11;
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

                var subs = this.raw.Substring(22, len);
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
            var start = 18;

            for (int i = 0; i < subpackets; i++)
            {
                var packet = new Packet(this.raw.Substring(start));
                start += packet.NumOfBits();

                yield return packet;
            }

            yield break;
        }

        public long VersionSum() => this.Version + this.SubPackets().Sum(p => p.VersionSum());

        private int GetVersion() => Convert.ToInt32(this.raw.Substring(0, 3), 2);

        private int GetTypeId() => Convert.ToInt32(this.raw.Substring(3, 3), 2);

        private int GetLengthTypeId() => Convert.ToInt32(this.raw.Substring(6, 1), 2);

        private long GetLiteralValue()
        {
            if (this.TypeId != 4)
            {
                return -1;
            }

            var bits = this.raw.Substring(6, this.NumOfBits() - 6);
            var val = string.Empty;
            var pos = 1;
            while (pos < bits.Length)
            {
                val += bits.Substring(pos, 4);
                pos += 5;
            }

            return Convert.ToInt64(val, 2);
        }

        private int Get15BitSubPacketLength() =>
            Convert.ToInt32(this.raw.Substring(7, 15), 2);

        private int Get11BitNumberofSubPackets() =>
            Convert.ToInt32(this.raw.Substring(7, 11), 2);
    }
}