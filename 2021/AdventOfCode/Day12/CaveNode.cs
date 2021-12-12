namespace AdventOfCode.Day12
{
    using System.Collections.Generic;

    public class CaveNode
    {
        public CaveNode(string nodeName)
        {
            this.Verticies = new List<CaveNode>();
            this.NodeName = nodeName;
        }

        public string NodeName { get; }

        public IList<CaveNode> Verticies { get; }

        public bool Visisted { get; private set; }

        public bool IsLarge => char.IsUpper(this.NodeName, 0);

        public bool IsStart => this.NodeName == "start";

        public bool IsEnd => this.NodeName == "end";

        public void AddVertex(CaveNode node)
        {
            if (node.NodeName == this.NodeName)
            {
                return;
            }

            this.Verticies.Add(node);
        }

        public void SetVisited() => this.Visisted = true;
    }
}
