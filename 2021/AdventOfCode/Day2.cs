namespace AdventOfCode
{
    using System.Collections.Generic;
    using AdventOfCode.Submarine;

    public static class Day2
    {
        public static (int HorizontalPostion, int VerticalPostion) CalculatePosition(IEnumerable<SubCommand> commands, ISub sub)
        {
            foreach (var cmd in commands)
            {
                sub.ProcessCommand(cmd);
            }

            return (sub.HorizontalPostion, sub.VerticalPostion);
        }
    }
}
