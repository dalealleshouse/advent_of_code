namespace AdventOfCode.Day14
{
    using System.Collections.Generic;
    using System.Linq;
    using System.Text.RegularExpressions;

    public class PolymerSolver
    {
        private readonly string template;
        private Regex rx = new Regex(@"(?<pair>.*) -> (?<insertion>.*)");
        private Dictionary<string, long> pairMap = new();
        private Dictionary<string, (string First, string Second)> ruleMap = new();

        public PolymerSolver(IEnumerable<string> data)
        {
            var first = true;

            foreach (var d in data)
            {
                if (first)
                {
                    this.template = d;
                    for (int i = 1; i < d.Length; i++)
                    {
                        var p = $"{d[i - 1]}{d[i]}";
                        var c = this.pairMap.GetValueOrDefault(p, 0) + 1;
                        this.pairMap[p] = c;
                    }

                    first = false;
                    continue;
                }

                if (string.IsNullOrWhiteSpace(d))
                {
                    continue;
                }

                var m = this.rx.Match(d);
                var pair = m.Groups["pair"].Value;
                var insertion = m.Groups["insertion"].Value;
                this.ruleMap[pair] = ($"{pair[0]}{insertion}", $"{insertion}{pair[1]}");
            }
        }

        public long MostCommonMinusLeastCommon(int numIterations)
        {
            for (int i = 0; i < numIterations; i++)
            {
                this.ProcessRules();
            }

            Dictionary<char, long> charMap = new();
            foreach (var kv in this.pairMap)
            {
                charMap[kv.Key[0]] = kv.Value + charMap.GetValueOrDefault(kv.Key[0], 0);
                charMap[kv.Key[1]] = kv.Value + charMap.GetValueOrDefault(kv.Key[1], 0);
            }

            // Each character is counted twice with the exception of the first and last
            charMap[this.template[0]]++;
            charMap[this.template[this.template.Length - 1]]++;

            return (charMap.Max(x => x.Value) - charMap.Min(x => x.Value)) / 2;
        }

        private void ProcessRules()
        {
            Dictionary<string, long> newMap = new();

            foreach (var kv in this.pairMap)
            {
                if (this.ruleMap.ContainsKey(kv.Key))
                {
                    var rule = this.ruleMap[kv.Key];

                    var c = this.pairMap.GetValueOrDefault(kv.Key, 0);
                    newMap[rule.First] = c + newMap.GetValueOrDefault(rule.First, 0);
                    newMap[rule.Second] = c + newMap.GetValueOrDefault(rule.Second, 0);
                }
                else
                {
                    newMap[kv.Key] = kv.Value;
                }
            }

            this.pairMap = newMap;
        }
    }
}
