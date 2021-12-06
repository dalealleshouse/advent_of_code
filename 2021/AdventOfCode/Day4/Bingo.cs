namespace AdventOfCode.Day4
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public class Bingo
    {
        private const int BoardSize = 5;

        public Bingo(List<int> numbers, List<List<int>> boards)
        {
            this.Numbers = numbers;
            this.Boards = boards;
        }

        public List<int> Numbers { get; }

        public List<List<int>> Boards { get; }

        public (int WinningNumber, List<int> WinningBoard) FindLastWinner()
        {
            List<int> lastWinner = null;
            int winningNumber = -1;
            List<int> winner = null;

            foreach (var num in this.Numbers)
            {
                do
                {
                    winner = this.CallNumber(num);
                    if (winner != null)
                    {
                        this.Boards.Remove(winner);
                        lastWinner = winner;
                        winningNumber = num;
                    }
                }
                while (winner != null);
            }

            return (winningNumber, lastWinner);
        }

        public (int WinningNumber, List<int> WinningBoard) FindWinner()
        {
            foreach (var num in this.Numbers)
            {
                var winner = this.CallNumber(num);
                if (winner != null)
                {
                    return (num, winner);
                }
            }

            return (-1, null);
        }

        public List<int> CallNumber(int value)
        {
            foreach (var board in this.Boards)
            {
                this.ClearNumber(board, value);

                if (this.IsWinner(board))
                {
                    return board;
                }
            }

            return null;
        }

        public int SumBoard(List<int> board)
        {
            return board.Where(x => x != -1).Sum();
        }

        private void ClearNumber(List<int> board, int value)
        {
            for (int i = 0; i < board.Count; i++)
            {
                if (board[i] == value)
                {
                    board[i] = -1;
                }
            }
        }

        private bool IsWinner(List<int> board)
        {
            var winningSum = BoardSize * -1;

            for (int i = 0; i < BoardSize; i++)
            {
                var rowSum = board.Skip(i * BoardSize).Take(BoardSize).Sum();
                if (rowSum == winningSum)
                {
                    return true;
                }

                var columnSum = board.Skip(i).Where((x, i) => i % BoardSize == 0).Sum();
                if (columnSum == winningSum)
                {
                    return true;
                }
            }

            return false;
        }

        private void PrintBoard(List<int> board)
        {
            for (int i = 0; i < board.Count; i++)
            {
                Console.Write($"{board[i]}-");

                if ((i + 1) % 5 == 0)
                {
                    Console.WriteLine();
                }
            }

            Console.WriteLine();
        }
    }
}
