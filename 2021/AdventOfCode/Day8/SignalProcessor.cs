namespace AdventOfCode.Day8
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class SignalProcessor
    {
        private readonly IEnumerable<SevenSegmentDigitSignal> signals;

        private Dictionary<int, int> knownLengths = new()
        {
            { 2, 1 },
            { 4, 4 },
            { 3, 7 },
            { 7, 8 },
        };

        public SignalProcessor(IEnumerable<SevenSegmentDigitSignal> signals)
        {
            this.signals = signals;
        }

        public int CountKnownSignalsInOutput()
        {
            return this.signals.Sum(sig =>
                    sig.Output.Count(x => this.knownLengths.Keys.Contains(x.Length)));
        }

        public int SumOfOutputValues()
        {
            var final = 0;

            foreach (var sig in this.signals)
            {
                Dictionary<int, string> vals = new()
                {
                    { 0, string.Empty },
                    { 1, string.Empty },
                    { 2, string.Empty },
                    { 3, string.Empty },
                    { 4, string.Empty },
                    { 5, string.Empty },
                    { 6, string.Empty },
                    { 7, string.Empty },
                    { 8, string.Empty },
                    { 9, string.Empty },
                };

                var possiblities = sig.Input.Select(x => x).ToList();

                vals[1] = possiblities.FirstOrDefault(x => x.Length == 2);
                possiblities.Remove(vals[1]);
                vals[7] = possiblities.FirstOrDefault(x => x.Length == 3);
                possiblities.Remove(vals[7]);
                vals[4] = possiblities.FirstOrDefault(x => x.Length == 4);
                possiblities.Remove(vals[4]);
                vals[8] = possiblities.FirstOrDefault(x => x.Length == 7);
                possiblities.Remove(vals[8]);

                vals[3] = possiblities.FirstOrDefault(x => x.Length == 5 && vals[1].All(x.Contains));
                possiblities.Remove(vals[3]);

                vals[9] = possiblities.FirstOrDefault(x => x.Length == 6 && vals[3].All(x.Contains));
                possiblities.Remove(vals[9]);

                vals[0] = possiblities.FirstOrDefault(x => x.Length == 6 && vals[1].All(x.Contains));
                possiblities.Remove(vals[0]);

                vals[6] = possiblities.Single(x => x.Length == 6);
                possiblities.Remove(vals[6]);

                vals[5] = possiblities.First(x => x.Length == 5 && x.All(vals[6].Contains));
                possiblities.Remove(vals[5]);

                vals[2] = possiblities.Single(x => x.Length == 5);

                var value = (this.GetValue(vals, sig.Output[0]) * 1000)
                    + (this.GetValue(vals, sig.Output[1]) * 100)
                    + (this.GetValue(vals, sig.Output[2]) * 10)
                    + this.GetValue(vals, sig.Output[3]);

                final += value;
            }

            return final;
        }

        private int GetValue(IDictionary<int, string> valMap, string val)
        {
            foreach (var item in valMap)
            {
                if (item.Value.Length == val.Length && item.Value.Intersect(val).Count() == val.Length)
                {
                    return item.Key;
                }
            }

            throw new InvalidOperationException("Value Not Found");
        }
    }
}
