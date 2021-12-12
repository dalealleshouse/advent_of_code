namespace AdventOfCode.Day12
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class CaveGraph
    {
        private List<CaveNode> nodes = new();
        private int pathCount = 0;

        public CaveGraph(IEnumerable<string> data)
        {
            foreach (var s in data)
            {
                var nodes = s.Split('-');

                var node1 = this.Upsert(nodes[0]);
                var node2 = this.Upsert(nodes[1]);
                node1.AddVertex(node2);
                node2.AddVertex(node1);
            }
        }

        public int FindPaths2()
        {
            var start = this.nodes.First(n => n.IsStart);
            this.FindPath(start, new List<string>(), this.IsOkToVisit2);
            return this.pathCount;
        }

        public int FindPaths()
        {
            var start = this.nodes.First(n => n.IsStart);
            this.FindPath(start, new List<string>(), this.IsOkToVisit);
            return this.pathCount;
        }

        public void FindPath(CaveNode start, List<string> path, Func<CaveNode, List<string>, bool> okFunc)
        {
            path.Add(start.NodeName);

            if (start.IsEnd)
            {
                this.pathCount++;
                return;
            }

            foreach (var n in start.Verticies)
            {
                if (okFunc(n, path))
                {
                    this.FindPath(n, path.GetRange(0, path.Count), okFunc);
                }
            }
        }

        private bool IsOkToVisit(CaveNode node, List<string> path) => node.IsLarge || !path.Contains(node.NodeName);

        private bool IsOkToVisit2(CaveNode node, List<string> path)
        {
            if (node.IsLarge)
            {
                return true;
            }

            if (node.IsStart)
            {
                return false;
            }

            if (!this.DuplicateSmallNodeExists(path))
            {
                return true;
            }

            return !path.Contains(node.NodeName);
        }

        private bool DuplicateSmallNodeExists(List<string> nodes) => nodes
                .Where(x => !char.IsUpper(x, 0))
                .GroupBy(x => x)
                .Where(x => x.Count() > 1)
                .Count() > 0;

        private CaveNode Upsert(string nodeName)
        {
            var node = this.nodes.FirstOrDefault(n => n.NodeName == nodeName);

            if (node == null)
            {
                node = new CaveNode(nodeName);
                this.nodes.Add(node);
            }

            return node;
        }
    }
}
