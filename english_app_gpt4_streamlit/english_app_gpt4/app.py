## app.py
import streamlit as st
from ui_helpers import StreamlitUI

class App:
    def __init__(self):
        self.ui = StreamlitUI()

    def run(self):
        self.ui.display_home()

if __name__ == "__main__":
    app = App()
    app.run()
