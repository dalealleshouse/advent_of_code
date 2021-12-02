namespace AdventOfCode
{
    using System.Collections.Generic;
    using AdventOfCode.Submarine;

    public partial class Day2
    {
        public static (int, int) CalculatePosition(IEnumerable<SubCommand> commands, ISub sub)
        {
            foreach (var cmd in commands)
            {
                sub.ProcessCommand(cmd);
            }

            return (sub.HorizontalPostion, sub.VerticalPostion);
        }
    }
}
