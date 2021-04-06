""" Purpose: An update to the ScoreKeeper App

    Features to add
        1. Select number of players from the first screen 
        2. Add tool bar options for adding and removing player-boards on the 2nd screen
        3. Add 'Help' menu option
        4. Add 'About' action to Help menu

    Author: John Milley
"""

from functools import partial
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtGui import (QPixmap, QFont)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStackedWidget, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QToolBar, QVBoxLayout, QWidget)

import sys
import lab8_resources

class ScoreKeeper(QMainWindow):
    """Main class for the ScoreKeeper application."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ScoreKeeper')
        self.setFixedSize(400, 400)

        # This stacked widget will hold our player selection window and the scoreboard window
        self.window_stack = QStackedWidget(self)
        self.setCentralWidget(self.window_stack)

        # We create the player selection UI first. Scoreboard UI is created based on # of players
        self._create_player_selection()

    def _create_player_selection(self):
        """Creates the first widget in the stack: the app entry screen."""
        self.player_selection_window = QWidget()
        self.player_selection_layout = QVBoxLayout()
        self.player_selection_window.setLayout(self.player_selection_layout)

        # You create an image using a QLabel, QPixmap, and QLabels setPixmap() method.
        # https://www.learnpyqt.com/tips/adding-images-to-pyqt5-applications/
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap(':/img/score.png')
        self.logo_label.setPixmap(self.logo_pixmap)

        self.num_players_layout = QHBoxLayout()
        self.num_players_layout.setContentsMargins(10,50,10,10) #left, top, right, bottom

        self.create_game_btn = QPushButton("Create Scoreboard")
        self.create_game_btn.clicked.connect(self.create_scoreboard)

        self.player_selection_layout.addWidget(self.logo_label)
        self.player_selection_layout.addWidget(self.create_game_btn)

        self.window_stack.addWidget(self.player_selection_window)
        
    def create_scoreboard(self):
        """Creates the second widget in the stack: the scoreboard."""
        self.scoreboard_window = QWidget()
        self.scoreboard_window.setObjectName('scoreboard')
        self.scoreboard_window.setStyleSheet('QWidget#scoreboard { background-color: rgb(204, 204, 235); }')
        self.scoreboard_layout = QVBoxLayout()
        self.scoreboard_window.setLayout(self.scoreboard_layout)
        
        self.create_playerboard()

        self.window_stack.addWidget(self.scoreboard_window)

        self.display_stack_window(1)

    def create_playerboard(self):
        """Creates the label and buttons for a single player."""
        self.player = QHBoxLayout()
        self.player.setContentsMargins(25,25,25,25)

        self.player_down = QPushButton("–")
        self.player_down.setFixedSize(75, 75)
        self.player_down.setFont(QFont('Monospace', 40))
        self.player_down.clicked.connect(self.decrease_score)

        self.score = 0
        self.player_score_label = QLabel(f"<p style='font: 75px; color: orangered;'>{self.score}</p>")
        self.player_score_label.setAlignment(Qt.AlignCenter)

        self.player_up = QPushButton("+")
        self.player_up.setFixedSize(75, 75)
        self.player_up.setFont(QFont('Monospace', 40))
        self.player_up.clicked.connect(self.increase_score)

        self.player.addWidget(self.player_down)
        self.player.addWidget(self.player_score_label)
        self.player.addWidget(self.player_up)

        self.scoreboard_layout.addLayout(self.player)
    
    def display_stack_window(self, i):
        """Changes visible widget in stack by index."""
        self.window_stack.setCurrentIndex(i)
        if i == 0:
            self.scoreboard_window.setParent(None)

    def increase_score(self):
        self.score += 1
        self.set_score()
        
    def decrease_score(self):
        if self.score > 0:
            self.score -= 1
            self.set_score()

    def set_score(self):
        self.player_score_label.setText(f"<p style='font: 75px; color: orangered;'>{str(self.score)}</p>")

# Client code
def main():
    """Main function."""
    scorekeeper = QApplication(sys.argv)
    view = ScoreKeeper()
    view.show()
    sys.exit(scorekeeper.exec())

if __name__ == '__main__':
    main()