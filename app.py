def app():
    # ...

    class App(QApplication):
        def __init__(self, argv):
            super().__init__(argv)

            self.window = Window()
            self.window.show()

            sys.exit(self.exec())

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Assistente de programação")
        self.setGeometry(50, 50, 600, 400)

        self.menu_bar = QMenuBar(self)
        self.file_menu = QMenu("Arquivo", self.menu_bar)
        self.menu_bar.addMenu(self.file_menu)

        self.exit_action = QAction("Sair", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.file_menu.addAction(self.exit_action)

        self.search_label = QLabel("Pesquisar:")
        self.search_line_edit = QLineEdit()
        self.search_button = QPushButton("Pesquisar")

        self.content_label = QLabel("")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.menu_bar)
        self.layout.addWidget(self.search_label)
        self.layout.addWidget(self.search_line_edit)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.content_label)

        self.search_button.clicked.connect(self.on_search_clicked)

    def on_search_clicked(self):
        topic = self.search_line_edit.text()

        self.content_label.setText("")

        if topic:
            with open(os.path.join(os.path.dirname(__file__), "database.json")) as database:
                database_data = json.load(database)

                for topic_name, topic_data in database_data.items():
                    if topic in topic_name:
                        self.content_label.setText(topic_data)
                        break

if __name__ == "__main__":
    app()
    app.exec()

