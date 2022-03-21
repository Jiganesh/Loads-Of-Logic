// https://leetcode.com/problems/n-queens/

package recursion;

import java.util.*;

public class nQueens {

    public static List<List<String>> solveNQueens(int n) {
        // List of Lists of boards
        List<List<String>> allBoards = new ArrayList<>();
        char[][] board = new char[n][n];
        helper(board, allBoards, 0);
        return allBoards;
    }

    static void helper(char[][] board, List<List<String>> allBoards, int col) {
        // save board to allBoards after placing Queens on all possible cols
        if (col == board.length) {
            saveBoard(board, allBoards);
            return;
        }
        for (int row = 0; row < board.length; row++) {
            // if it's safe, place queen at row
            if (isSafe(row, col, board)) {
                board[row][col] = 'Q';
                helper(board, allBoards, col + 1);
                // backtracking
                board[row][col] = '.';
            }
        }
    }

    // Fn to check if it's safe to place Queen
    static boolean isSafe(int row, int col, char[][] board) {
        int len = board.length;
        // traverse in all cols to check if a queen is already present or not
        for (int i = 0; i < len; i++) {
            if (board[row][i] == 'Q')
                return false;
        }
        // traverse in all rows to check if a queen is already present or not
        for (int i = 0; i < len; i++) {
            if (board[i][col] == 'Q')
                return false;
        }
        // traverse through upper left diagonal to check if queen is present
        int r = row;
        for (int c = col; c >= 0 && r >= 0; r--, c--) {
            if (board[r][c] == 'Q')
                return false;
        }
        // traverse through upper right diagonal to check if queen is present
        r = row;
        for (int c = col; c < len && r >= 0; r--, c++) {
            if (board[r][c] == 'Q')
                return false;
        }
        // traverse through lower left diagonal to check if queen is present
        r = row;
        for (int c = col; c >= 0 && r < len; r++, c--) {
            if (board[r][c] == 'Q')
                return false;
        }
        // traverse through lower right diagonal to check if queen is present
        r = row;
        for (int c = col; c < len && r < len; r++, c++) {
            if (board[r][c] == 'Q')
                return false;
        }
        return true;
    }

    // Fn to save a board to List of Boards
    static void saveBoard(char[][] board, List<List<String>> allBoards) {
        int len = board.length;
        String row = "";
        List<String> newBoard = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            row = "";
            for (int j = 0; j < len; j++) {
                if (board[i][j] == 'Q')
                    row += 'Q';
                else
                    row += '.';
            }
            // this adds the row to the newBoards -> "Q..." or "..Q."
            newBoard.add(row);
        }
        // this add the board to the list of boards -> [[..Q., Q..., ...Q, .Q..],...]
        allBoards.add(newBoard);
    }
}
