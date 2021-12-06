namespace AdventOfCode.Day2
{
    using System;
    using System.Collections.Generic;

    public class SimpleSub : BaseSub
    {
        private Dictionary<string, Action<SimpleSub, int>> commandDefinitions = new()
        {
            { "up", (SimpleSub sub, int value) => sub.VerticalPostion -= value },
            { "down", (SimpleSub sub, int value) => sub.VerticalPostion += value },
            { "forward", (SimpleSub sub, int value) => sub.HorizontalPostion += value },
        };

        public override void ProcessCommand(SubCommand command)
        {
            this.commandDefinitions[command.Command](this, command.Value);
        }
    }
}
