namespace AdventOfCode.Submarine
{
    using System;
    using System.Collections.Generic;

    public class Sub : ISub
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

        public int HorizontalPostion { get; set; }

        public int VerticalPostion { get; set; }

        public int Aim { get; set; }

        public void ProcessCommand(SubCommand command)
        {
            this.commandDefinitions[command.Command](this, command.Value);
        }
    }
}
