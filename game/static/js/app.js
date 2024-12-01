let board = ['', '', '', '', '', '', '', '', '']; // Array to track board state
let currentPlayer = 'X';  // 'X' is the user
let gameOver = false;  // Flag to check if the game is over

function makeMove(cellIndex) {
    if (gameOver || board[cellIndex] !== '') return;

    // Mark the cell with the user's move ('X')
    board[cellIndex] = 'X';
    document.getElementById(`cell-${cellIndex}`).innerText = 'X';

    // Check if the user wins
    if (checkWinner('X')) {
        gameOver = true;
        window.location.href = "/result/win/";  // Redirect to result page
        return;
    }

    // If the game is not over, let the CPU play
    if (!gameOver) {
        cpuMove();
    }
}

function cpuMove() {
    let emptyCells = board.map((value, index) => value === '' ? index : null).filter(val => val !== null);
    let randomIndex = emptyCells[Math.floor(Math.random() * emptyCells.length)];

    // Mark the cell with CPU's move ('O')
    board[randomIndex] = 'O';
    document.getElementById(`cell-${randomIndex}`).innerText = 'O';

    // Check if CPU wins
    if (checkWinner('O')) {
        gameOver = true;
        window.location.href = "/result/lose/";  // Redirect to result page
    }
}

function checkWinner(player) {
    const winningCombination = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]  // Diagonals
    ];

    for (let combo of winningCombination) {
        if (board[combo[0]] === player && board[combo[1]] === player && board[combo[2]] === player) {
            return true;
        }
    }
    return false;
}

function resetBoard() {
    board = ['', '', '', '', '', '', '', '', ''];
    for (let i = 0; i < 9; i++) {
        document.getElementById(`cell-${i}`).innerText = '';
    }
    gameOver = false;
}
