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

    st.write("### Input a 2D array representing the Sudoku (9x9)")
    input_text = st.text_area(
        "Enter the Sudoku as a Python-style 2D list (use 0 for empty cells):", 
        value="[[5, 3, 0, 0, 7, 0, 0, 0, 0],\n"
              "[6, 0, 0, 1, 9, 5, 0, 0, 0],\n"
              "[0, 9, 8, 0, 0, 0, 0, 6, 0],\n"
              "[8, 0, 0, 0, 6, 0, 0, 0, 3],\n"
              "[4, 0, 0, 8, 0, 3, 0, 0, 1],\n"
              "[7, 0, 0, 0, 2, 0, 0, 0, 6],\n"
              "[0, 6, 0, 0, 0, 0, 2, 8, 0],\n"
              "[0, 0, 0, 4, 1, 9, 0, 0, 5],\n"
              "[0, 0, 0, 0, 8, 0, 0, 7, 9]]"
    )

    try:
        # Parse the input text as a Python list
        sudoku_board = eval(input_text)

        # Button to solve the Sudoku
        if st.button("Solve"):
            st.write("### Solving Sudoku...")
            visualize_process = st.checkbox("Visualize solving process", value=True)

            if solve_sudoku(sudoku_board, visualize=visualize_process):
                st.write("### Sudoku Solved Successfully!")
                display_board(sudoku_board)
            else:
                st.write("### No Solution exists for the given Sudoku")
    except Exception as e:
        st.error(f"Error parsing the input. Make sure it's a valid 9x9 2D list format.\nError: {e}")

if __name__ == "__main__":
    main()
