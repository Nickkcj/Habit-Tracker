from src.frontend.main_window import MainWindow
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    main_window = MainWindow()
    