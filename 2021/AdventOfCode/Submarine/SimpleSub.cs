namespace AdventOfCode.Submarine
{
    using System;
    using System.Collections.Generic;

    public class SimpleSub : ISub
    {
        private Dictionary<string, Action<SimpleSub, int>> commandDefinitions = new ()
        {
            { "up", (SimpleSub sub, int value) => sub.VerticalPostion -= value },
            { "down", (SimpleSub sub, int value) => sub.VerticalPostion += value },
            { "forward", (SimpleSub sub, int value) => sub.HorizontalPostion += value },
        };

        public int HorizontalPostion { get; set; }

        public int VerticalPostion { get; set; }

        public void ProcessCommand(SubCommand command)
        {
            this.commandDefinitions[command.command](this, command.value);
        }
    }
}
