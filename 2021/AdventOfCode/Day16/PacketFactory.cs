namespace AdventOfCode.Day16
{
    using System;
    using System.Text;

    public static class PacketFactory
    {
        public static Packet CreatePacket(string data)
        {
            var p = new StringBuilder();

            foreach (var c in data)
            {
                p.Append(Convert.ToString(Convert.ToInt32(c.ToString(), 16), 2).PadLeft(4, '0'));
            }

            return new Packet(p.ToString());
        }
    }
}
