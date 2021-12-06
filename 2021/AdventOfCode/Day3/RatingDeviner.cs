namespace AdventOfCode.Day3
{
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;

    public static class RatingDeviner
    {
        public static (int Gamma, int Epsilon) PowerConsumption(IEnumerable<(int BitCount, BitArray Bits)> data)
        {
            var values = data.ToList();

            // The assumption is all bits are the same length
            var bitCount = values[0].BitCount;
            var bits = values.Select(x => x.Bits).ToList();

            var half = bits.Count / 2;

            int gamma = 0;
            int epsilon = 0;
            for (int i = 0; i < bitCount; i++)
            {
                if (bits.Where(x => x.Get(i)).Count() > half)
                {
                    gamma |= 1 << i;
                }
                else
                {
                    epsilon |= 1 << i;
                }
            }

            return (gamma, epsilon);
        }

        public static int OxygenGeneratorRating(IEnumerable<(int BitCount, BitArray Bits)> data) => GetRating(data, true);

        public static int CO2ScrubberRating(IEnumerable<(int BitCount, BitArray Bits)> data) => GetRating(data, false);

        private static int GetRating(IEnumerable<(int BitCount, BitArray Bits)> data, bool modeMatch)
        {
            var values = data.ToList();

            // The assumption is all bits are the same length
            var bitCount = values[0].BitCount;
            var bits = values.Select(x => x.Bits).ToList();

            var pos = bitCount - 1;
            while (bits.Count != 1)
            {
                var half = Math.Ceiling(bits.Count / 2D);
                var intersting = bits.Where(x => x.Get(pos)).Count();
                var mode = (intersting >= half) ? modeMatch : !modeMatch;

                bits = bits.Where(x => x.Get(pos) == mode).ToList();
                pos--;
            }

            int[] array = new int[1];
            bits[0].CopyTo(array, 0);
            return array[0];
        }
    }
}
