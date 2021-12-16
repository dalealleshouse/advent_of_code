namespace AdventOfCode.Day16
{
    using System;
    using System.Text;

    public class PacketParser
    {
        private readonly string packet;

        public PacketParser(string data)
        {
            var p = new StringBuilder();

            foreach (var c in data)
            {
                p.Append(Convert.ToString(Convert.ToInt32(c.ToString(), 16), 2).PadLeft(4, '0'));
            }

            this.packet = p.ToString();
        }

        public long SumOfVersion(string packet = null)
        {
            if (packet == null)
            {
                packet = this.packet;
            }

            var p = new Packet(this.packet);
            return p.VersionSum();
        }

        public long Calculate(string packet = null)
        {
            if (packet == null)
            {
                packet = this.packet;
            }

            var p = new Packet(this.packet);
            return p.GetValue();
        }
    }
}
