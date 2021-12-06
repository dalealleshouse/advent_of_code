namespace AdventOfCode.Day2
{
    using System;
    using System.Collections.Generic;

    public class Sub : BaseSub
    {
        private Dictionary<string, Action<Sub, int>> commandDefinitions = new()
        {
            { "up", (Sub sub, int value) => sub.Aim -= value },
            { "down", (Sub sub, int value) => sub.Aim += value },
            {
                "forward",
                (Sub sub, int value) =>
                {
                    sub.HorizontalPostion += value;
                    sub.VerticalPostion += sub.Aim * value;
                }
            },
        };

        public int Aim { get; set; }

        public override void ProcessCommand(SubCommand command)
        {
            this.commandDefinitions[command.Command](this, command.Value);
        }
    }
}
