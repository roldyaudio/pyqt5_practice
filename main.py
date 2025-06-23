import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5.uic.properties import QtCore

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add tittle
        self.setWindowTitle("Reaper_localization_tools")
        self.resize(500, 300)

        # Set vertical, horizontal, etc layout
        self.setLayout(qtw.QVBoxLayout())

        # LABELS
        # Set script path label
        enter_script_label = qtw.QLabel("Enter script path: ")
        enter_audio_label = qtw.QLabel("Enter audio files path: ")
        result_label = qtw.QLabel("")

        # Change font size of label
        enter_script_label.setFont(qtg.QFont("Helvetica", 13))
        enter_audio_label.setFont(qtg.QFont("Helvetica", 13))
        result_label.setFont(qtg.QFont("Helvetica", 13))

        # Create entry box
        rec_script_entry = qtw.QLineEdit()
        rec_script_entry.setObjectName("script_entry")
        rec_script_entry.setText("")
        audiofile_entry = qtw.QLineEdit()
        audiofile_entry.setObjectName("audios_entry")
        audiofile_entry.setText("")

        # Create button
        def pressed():
            # time.sleep(1)
            rec_script_entry.setText("")
            audiofile_entry.setText("")
            # result_label.setText(f"You picked {my_combo.currentData()}")
                # we also can call my_combo.currentText() - my_combo.currentIndex()
            # result_label.setText(f"You picked {my_spin.value()}")
            result_label.setText(f"You picked {my_text.toPlainText()}")
            my_text.setPlainText("Your pressed it")

        button = qtw.QPushButton("Create project")
        button.clicked.connect(pressed)  # Connect signal to slot

        # Create a combo box
        # my_combo = qtw.QComboBox(self)
        # # Add items to it
        # my_combo.addItem("Add item notes to existing Reaper project", "Something")
        # my_combo.addItem("Create project in script order with item notes", 2)
        # my_combo.addItem("Open audio loudness and data an analyzer")
        # my_combo.addItems(["One", "Two", "Three"])
        # my_combo.insertItems(1, ['Second thing', 'Hey'])

        # Create a Spin box
        # my_spin = qtw.QDoubleSpinBox(self,) # Ment for floats. We can use QSpinBox for int
        # my_spin.setValue(1)
        # my_spin.setMaximum(18)
        # my_spin.setMinimum(0)
        # my_spin.setSingleStep(0.25)
        # my_spin.setPrefix("#")
        # my_spin.setSuffix("_Order")

        # Create a Text Box
        my_text = qtw.QTextEdit(self)
        # my_text.setFixedSize(250, 250)
        my_text.setLineWrapMode(qtw.QTextEdit.FixedColumnWidth)
        my_text.setLineWrapColumnOrWidth(50)
        my_text.setPlaceholderText("Insert your text here")
        my_text.setPlainText("This was here before you")
        my_text.setReadOnly(False)
        my_text.acceptRichText()
        my_text.setHtml("<h1>Big Header Text!</h1>")

        # SHOW IN WIDGET
        # self.layout().addWidget(enter_script_label)
        # self.layout().addWidget(rec_script_entry)
        # self.layout().addWidget(enter_audio_label)
        # self.layout().addWidget(audiofile_entry)
        self.layout().addWidget(result_label)
        # self.layout().addWidget(my_combo)
        # self.layout().addWidget(my_spin)
        self.layout().addWidget(my_text)
        self.layout().addWidget(button)

        self.show()

app = qtw.QApplication([])
mw = MainWindow()
# Run the app
app.exec_()
