namespace AdventOfCode.Day2
{
    using System.Collections.Generic;

    public abstract class BaseSub
    {
        public int HorizontalPostion { get; set; }

        public int VerticalPostion { get; set; }

        public abstract void ProcessCommand(SubCommand command);

        public (int HorizontalPostion, int VerticalPostion) CalculatePosition(IEnumerable<SubCommand> commands)
        {
            foreach (var cmd in commands)
            {
                this.ProcessCommand(cmd);
            }

            return (this.HorizontalPostion, this.VerticalPostion);
        }
    }
}
