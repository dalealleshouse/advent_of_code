namespace AdventOfCode.Submarine
{
    public interface ISub
    {
        int HorizontalPostion { get; set; }

        int VerticalPostion { get; set; }

        void ProcessCommand(SubCommand command);
    }
}
