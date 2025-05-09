from PyQt6.QtWidgets import QMainWindow

from gui import Ui_MainWindow
class Logic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.voted_id = set()
        self.candidate = ""
        self.winner = ""

        self.votes = {"jane": 0, "jone": 0}

        self.ui.pushButton.clicked.connect(self.handle_voted)

    def handle_voted(self):
        user_id = self.ui.lineEdit.text().strip()
          # check if the ID is entre
        if not user_id:
            self.ui.label_4.setText("Enter your id")
            return

        if not user_id.isdigit() or len(user_id) != 4:
            self.ui.label_4.setText("ID must be 4 digits")
            return

        if user_id in self.voted_id:
            self.ui.label_4.setText("Already voted")
            return
# selected which candidate was voted
        if self.ui.radioButton.isChecked():
            self.candidate = "jane"
        elif self.ui.radioButton_2.isChecked():
            self.candidate = "jone"

        else:
            self.ui.label_4.setText("enter candidate")
            return
        # this is just adding their number of the vote
        self.voted_id.add(user_id)
        self.votes[self.candidate] += 1

        with open("data_file.txt", "a") as f:
            f.write(f"{user_id}\n")
        self.ui.label_4.setText(f"Voted for {self.candidate}")
# this code just showed who is the winner
        if self.votes["Jane"] > self.votes["Jone"]:
                self.winner = "Jane"
        elif self.votes["Jone"] > self.votes["Jane"]:
                self.winner = "Jone"

        else:
            self.winner = "Tie"
        if hasattr(self.ui, "label_5"):
            if self.winner == "Tie":
                self.ui.label_5.setText("Tie")
            else:
                self.ui.label_5.setText("Winner is " + self.winner)


            total = self.votes["Jane"] + self.votes["Jone"]
            if total > 0:
                percent_Jane = round((self.votes["Jane"] / total) * 100, 2)
                percent_Jone = round((self.votes["Jone"] / total) * 100, 2)

                result = (
                    f"Jane:{self.votes['Jane']} votes({percent_Jane}%)\n"
                    f"Jone:{self.votes['Jone']} votes ({percent_Jone}%)"
                )

                if hasattr(self.ui, "label_6"):
                    self.ui.label_6.setText(result)
