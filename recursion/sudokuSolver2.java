package recursion;

/*
A sudoku solution must satisfy all of the following rules:
-> Each of the digits 1-9 must occur exactly once in each row.
-> Each of the digits 1-9 must occur exactly once in each column.
-> Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The ' ' character indicates empty cells.
*/

public class sudokuSolver2 {
    public static void main(String[] args) {
        int[][] board = {
                { 7, 0, 2, 0, 5, 0, 6, 0, 0 },
                { 0, 0, 0, 0, 0, 3, 0, 0, 0 },
                { 1, 0, 0, 0, 0, 9, 5, 0, 0 },
                { 8, 0, 0, 0, 0, 0, 0, 9, 0 },
                { 0, 4, 3, 0, 0, 0, 7, 5, 0 },
                { 0, 9, 0, 0, 0, 0, 0, 0, 8 },
                { 0, 0, 9, 7, 0, 0, 0, 0, 5 },
                { 0, 0, 0, 2, 0, 0, 0, 0, 0 },
                { 0, 0, 7, 0, 4, 0, 2, 0, 3 }
        };
        System.out.println("\nInput\n");
        printBoard(board);
        if (solveBoard(board)) {
            System.out.println("Solved ;)\n");
            printBoard(board);
            System.out.println();
        } else {
            System.out.println("Unsolvable :(\n");
            printBoard(board);
            System.out.println();
        }
    }

    static boolean solveBoard(int[][] board) {
        return solveBoard(board, 0, 0);
    }

    // To print the board
    static void printBoard(int[][] board) {
        for (int row = 0; row < 9; row++) {
            if (row % 3 == 0)
                // for printing before grid rows
                System.out.println("-------------------------------");
            for (int col = 0; col < 9; col++) {
                // for printing before grid columns
                if (col % 3 == 0)
                    System.out.print("|");
                System.out.print(" " + board[row][col] + " ");
                // for printing at last grid column
                if (col == 8)
                    System.out.print("|");
            }
            // for printing at last grid row
            if (row == 8)
                System.out.println("\n-------------------------------");
            System.out.println();
        }
    }

    // a utility function to solve the board
    static boolean solveBoard(int[][] board, int row, int col) {
        // base case -> recursion stops at the 10th row
        if (row == board.length)
            return true;
        int newRow = 0, newCol = 0;
        // when its the last col of the board, goto next row & first col
        if (col == board.length - 1) {
            newRow = row + 1;
            newCol = 0;
        }
        // else, keep increasing the col by one & the row remains the same
        else {
            newRow = row;
            newCol = col + 1;
        }
        // if the cell isn't empty, i.e. there is a number present in that cell
        if (board[row][col] != 0) {
            // do a recursive call, if the fn returns true, i.e. the board is solved,
            // we'll also return true
            if (solveBoard(board, newRow, newCol))
                return true;
        }
        // if cell is empty
        else {
            for (int i = 1; i <= 9; i++) {
                // if it's safe to place 'i' at that cell
                if (isValidPlacement(board, row, col, i)) {
                    board[row][col] = i;
                    // after placing the number, do a recursive call,
                    // if the fn returns true, we'll also return true
                    if (solveBoard(board, newRow, newCol))
                        return true;
                    // if the recursive call returns false, i.e. it wasn't safe to place 'i',
                    // we'll empty the cell & and will try for the next value of 'i' (backtracking)
                    else
                        board[row][col] = 0;
                }
            }
        }
        // return false if it isn't posssible to place a number in the cell
        return false;
    }

    // To check if it is valid to place the number
    static boolean isValidPlacement(int[][] board, int row, int col, int number) {
        // to check if 'number' is present in the row or the col
        for (int i = 0; i < board.length; i++) {
            // return false if 'number' is present in the col
            if (board[i][col] == number)
                return false;
            // return false if 'number' is present in the row
            if (board[row][i] == number)
                return false;
        }
        // to check if the 'number' is present in the 3X3 grid
        // There are two ways to get the initial row and column of 3X3 grid
        // 1
        int startingRow = (row / 3) * 3;
        int startingCol = (col / 3) * 3;
        // 2
        // int startingRow = (row % 3) - row;
        // int startingCol = (col % 3) - col;
        for (int i = startingRow; i < startingRow + 3; i++)
            for (int j = startingCol; j < startingCol + 3; j++)
                // return false if 'number' is present in the 3X3 grid or matrix
                if (board[i][j] == number)
                    return false;
        // return true if 'number' isn't present in row, col & grid
        return true;
    }
}