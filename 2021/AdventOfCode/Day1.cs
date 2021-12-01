namespace AdventOfCode
{
    using System.Collections.Generic;
    using System.Linq;

    public static class Day1
    {
        public static int CountIncreasing(IEnumerable<int> data)
        {
            var count = 0;
            var previous = int.MaxValue;

            foreach (var i in data)
            {
                if (i > previous)
                {
                    count++;
                }

                previous = i;
            }

            return count;
        }

        public static int CountIncreasingWithinSlidingWindow(IEnumerable<int> data, int windowSize)
        {
            var q = new Queue<int>();

            var count = 0;
            var previous = int.MaxValue;

            foreach (var i in data)
            {
                q.Enqueue(i);

                if (q.Count < windowSize)
                {
                    continue;
                }
                else if (q.Count > windowSize)
                {
                    q.Dequeue();
                }

                var current = q.Sum();

                if (current > previous)
                {
                    count++;
                }

                previous = current;
            }

            return count;
        }
    }
}
