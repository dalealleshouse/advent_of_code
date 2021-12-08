namespace AdventOfCode.Day8
{
    using System.Linq;

    public class SevenSegmentDigitSignal
    {
        public SevenSegmentDigitSignal(string[] input, string[] output)
        {
            this.Input = input;
            this.Output = output;
            this.All = this.Input.Concat(this.Output).ToArray();
        }

        public string[] Input { get; }

        public string[] Output { get; }

        public string[] All { get; }

        public override string ToString()
        {
            return $"{string.Join(',', this.Input)}|{string.Join(',', this.Output)}";
        }
    }
}
