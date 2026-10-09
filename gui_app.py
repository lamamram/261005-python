"""
1. importer la partie graphique (UI_MainWindow) depuis le module
2. accrocher cette classe à la classe principale de la fénêtre de l'app avec héritage multiple
3. exécuter la méthide setupUi() de la classe UI_MainWindow sur l'objet courant de l'application
4. chercher le code métier (package text_analyser)
5. configurer les slots/event_handlers (soit dans __init__ ou avec le décorateur @Slot())
6. installer le code métier et associer le code métier et les widgets dans les slots
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Slot
from gui_MainWindow import Ui_MainWindow
from text_analyser import Cleaner, Counter

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(600, 400)
        self.setupUi(self)

        # configurer un gestionnaire d'évènement
        # self.okBtn.clicked.connect(self.on_okBtn_clicked)

    @Slot()
    def on_okBtn_clicked(self):
        """
        event_handler ou Slot
        si le nom de la méthode est on_<widget_name>_<evt_name>, pas besoin de connexion dans __init__
        """
        # d'abord rafraichir le listWidget
        self.listWidget.clear()

        cl = Cleaner(self.textEdit.toPlainText())
        counter = Counter(cl, self.signWords.value())
        occurences = counter.count()
        # afficher çà dans la listWidget
        for word, occurence in occurences.items():
            self.listWidget.addItem(f"{word}: {occurence}")
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
