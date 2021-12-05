namespace AdventOfCode.Day5
{
    public class LineSegment
    {
        public LineSegment((int X, int Y) begin, (int X, int Y) end)
        {
            this.Begin = begin;
            this.End = end;
        }

        public (int X, int Y) Begin { get; }

        public (int X, int Y) End { get; }
    }
}
