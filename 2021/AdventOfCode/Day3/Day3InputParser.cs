namespace AdventOfCode.Day3
{
    using System;
    using System.Collections;
    using System.Collections.Generic;

    public static class Day3InputParser
    {
        public static IEnumerable<(int BitCount, BitArray Bits)> ParseBinaryString(string path) =>
            InputParser.Parse(path, x =>
        {
            return (x.Length, new BitArray(new int[] { Convert.ToInt32(x, 2) }));
        });
    }
}
