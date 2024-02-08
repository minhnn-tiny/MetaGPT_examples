use std::fmt;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Player {
    X,
    O,
}

impl fmt::Display for Player {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Player::X => write!(f, "X"),
            Player::O => write!(f, "O"),
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct Game {
    pub board: [[Option<Player>; 3]; 3],
    pub current_player: Player,
    pub winner: Option<Player>,
}

impl Game {
    pub fn new() -> Self {
        Self {
            board: [[None; 3]; 3],
            current_player: Player::X,
            winner: None,
        }
    }

    pub fn make_move(&mut self, x: usize, y: usize) -> bool {
        if self.winner.is_some() {
            return false;
        }

        if self.board[x][y].is_some() {
            return false;
        }

        self.board[x][y] = Some(self.current_player);
        self.check_winner();
        self.current_player = match self.current_player {
            Player::X => Player::O,
            Player::O => Player::X,
        };

        true
    }

    pub fn check_winner(&mut self) {
        for i in 0..3 {
            if self.board[i][0] == self.board[i][1] && self.board[i][1] == self.board[i][2] {
                self.winner = self.board[i][0];
                return;
            }

            if self.board[0][i] == self.board[1][i] && self.board[1][i] == self.board[2][i] {
                self.winner = self.board[0][i];
                return;
            }
        }

        if self.board[0][0] == self.board[1][1] && self.board[1][1] == self.board[2][2] {
            self.winner = self.board[0][0];
            return;
        }

        if self.board[0][2] == self.board[1][1] && self.board[1][1] == self.board[2][0] {
            self.winner = self.board[0][2];
            return;
        }
    }
}
