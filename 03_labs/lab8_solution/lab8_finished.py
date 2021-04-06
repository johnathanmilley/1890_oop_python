""" Purpose: An update to the ScoreKeeper App

    Features added
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


class Player:
    """ Player class creates everthing needed to add another scoreboard to the game
    
        attributes: name, score, player_board (the UI elements)
    """
    def __init__(self, name="Player", score=0):
        self.name = name
        self.score = score
        self.create_playerboard()

    def create_playerboard(self):
        """ returns a layout for a player scoreboard """
        self.player_layout = QHBoxLayout()
        
        self.player_down = QPushButton("–")
        self.player_down.setFixedSize(75, 75)
        self.player_down.setFont(QFont('Monospace', 40))
        self.player_down.clicked.connect(self.decrease_score)

        self.player_score_label = QLabel(f"<p style='font: 75px; color: orangered;'>{self.score}</p>")
        self.player_score_label.setAlignment(Qt.AlignCenter)

        self.player_up = QPushButton("+")
        self.player_up.setFixedSize(75, 75)
        self.player_up.setFont(QFont('Monospace', 40))
        self.player_up.clicked.connect(self.increase_score)

        self.player_layout.addWidget(self.player_down)
        self.player_layout.addWidget(self.player_score_label)
        self.player_layout.addWidget(self.player_up)

    def increase_score(self):
        self.score += 1
        self.set_score()

    def decrease_score(self):
        if self.score > 0:
            self.score -= 1
            self.set_score()

    def set_score(self):
        self.player_score_label.setText(f"<p style='font: 75px; color: orangered;'>{str(self.score)}</p>")


class ScoreKeeper(QMainWindow):
    """Main class of the ScoreKeeper application."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ScoreKeeper')
        # self.setFixedSize(400, 400)

        # This stacked widget will hold our player selection window and the scoreboard window
        self.window_stack = QStackedWidget(self)
        self.setCentralWidget(self.window_stack)

        # We create the player selection UI first. Scoreboard UI is created based on # of players
        self._create_player_selection()

        self._create_tool_bar()
        self._create_menu()

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

        self.num_players_select = QComboBox()
        self.num_players_option_list = {'1-Player': 1, '2-Players': 2, '3-Players': 3, '4-Players': 4}
        self.num_players_select.addItems(self.num_players_option_list.keys())

        self.create_game_btn = QPushButton("Create Scoreboard")
        self.create_game_btn.clicked.connect(self._create_scoreboard)

        self.player_selection_layout.addWidget(self.logo_label)
        self.player_selection_layout.addWidget(self.num_players_select)
        self.player_selection_layout.addWidget(self.create_game_btn)

        self.window_stack.addWidget(self.player_selection_window)
        
    def _create_scoreboard(self):
        """Create the scoreboard based on # of players"""
        self.scoreboard_window = QWidget()
        self.scoreboard_window.setObjectName('scoreboard')
        self.scoreboard_window.setStyleSheet('QWidget#scoreboard { background-color: rgb(204, 204, 235); }')
        self.scoreboard_layout = QVBoxLayout()
        self.scoreboard_window.setLayout(self.scoreboard_layout)

        # Add the requested number of players to the scoreboard
        self.players = []
        for p in range(0, self.num_players_option_list[self.num_players_select.currentText()]):
            p = Player()
            self.scoreboard_layout.addLayout(p.player_layout)
            self.players.append(p)

        self.window_stack.addWidget(self.scoreboard_window)

        self.display_stack_window(1)

    def _create_menu(self):
        self.help = self.menuBar().addMenu('&Help')
        # setNativeMenuBar(False) necessary for macOS
        # self.menuBar().setNativeMenuBar(False) 
        self.help.addAction('About', self.display_about)

    def _create_tool_bar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Add', self.add_player)
        tools.addAction('Remove', self.remove_player)

    def display_about(self):
        about = QDialog(self)
        about.setWindowTitle('About ScoreKeeper')
        about_layout = QVBoxLayout()
        about_text = QLabel('This application is a completed version of Lab 8. \n'
                            'Course: CP1890 - Object Oriented Programming')
        about_layout.addWidget(about_text)
        about.setLayout(about_layout)
        about.exec()

    def display_stack_window(self, i):
        self.window_stack.setCurrentIndex(i)
        if i == 0:
            self.scoreboard_window.setParent(None)

    def add_player(self):
        """Adds player to the scoreboard"""
        p = Player()
        self.scoreboard_layout.addLayout(p.player_layout)
        self.players.append(p)

    def remove_player(self):
        """Removes last player from scoreboard"""
        if len(self.players) == 0: return 

        # get last player in players list
        p = self.players[len(self.players) - 1]

        # --- Removing last player UI ---
        # Widgets that have layouts like our player objects need 
        # to be 'deleted' by going through and removing the parent
        # of each one by setting parent to None.
        # https://www.semicolonworld.com/question/58072/clear-all-widgets-in-a-layout-in-pyqt
        for i in reversed(range(p.player_layout.count())):
            p.player_layout.itemAt(i).widget().setParent(None)

         # remove last player from player array
        self.players.pop()

        # resize screen when player widgets are removed
        self.resize(self.sizeHint().width(), self.sizeHint().height())

# Client code
def main():
    """Main function."""
    scorekeeper = QApplication(sys.argv)
    view = ScoreKeeper()
    view.show()
    sys.exit(scorekeeper.exec())

if __name__ == '__main__':
    main()