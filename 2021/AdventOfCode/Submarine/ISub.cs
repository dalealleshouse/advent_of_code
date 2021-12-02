namespace AdventOfCode.Submarine
{
    public interface ISub
    {
        int HorizontalPostion { get; set; }

        int Verticalpostion { get; set; }

        void ProcessCommand(SubCommand command);
    }
}
