import streamlit as st
import numpy as np
import time

# Helper function to display the Sudoku board
def display_board(board):
    st.write("### Current Sudoku Board")
    board_display = np.array(board)
    st.dataframe(board_display)

# Check if a number can be placed in the specified position
def is_safe(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
                
    return True

# Backtracking function to solve the Sudoku
def solve_sudoku(board, visualize=False):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        
                        if visualize:
                            display_board(board)
                            time.sleep(0.2)  # Pause for visualization

                        if solve_sudoku(board, visualize):
                            return True

                        # Backtrack
                        board[row][col] = 0

                return False

    return True

# Streamlit app
def main():
    st.title("Sudoku Solver with Visualization")

    # Input grid (can be modified to take a user input)
    default_sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # Convert default_sudoku to editable input
    sudoku_input = []
    for row in range(9):
        row_input = []
        for col in range(9):
            row_input.append(st.number_input(f"Cell ({row+1},{col+1})", min_value=0, max_value=9, value=default_sudoku[row][col]))
        sudoku_input.append(row_input)

    # Button to solve the Sudoku
    if st.button("Solve"):
        # Deep copy the input to avoid modifying original array
        sudoku_board = np.array(sudoku_input)

        st.write("### Solving Sudoku...")
        visualize_process = st.checkbox("Visualize solving process", value=True)

        if solve_sudoku(sudoku_board, visualize=visualize_process):
            st.write("### Sudoku Solved Successfully!")
            display_board(sudoku_board)
        else:
            st.write("### No Solution exists for the given Sudoku")

if __name__ == "__main__":
    main()
