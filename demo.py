import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QCalendarWidget
from PyQt5.QtCore import QDate, Qt

class RTOComplianceForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # create the GUI components
        calendar_label = QLabel("Select date range:")
        self.calendar1 = QCalendarWidget()
        self.calendar2 = QCalendarWidget()
        self.calendar2.setEnabled(False) # disable the second calendar initially
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Working from home", "Working from office", "Annual leave", "Sick leave","Bank holiday"])
        self.employee_id_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        

        # add event handlers
        self.calendar1.clicked[QDate].connect(self.toggle_calendar2)
        self.submit_button.clicked.connect(self.submit_form)

        # set up the layout
        vbox1 = QVBoxLayout()
        vbox1.addWidget(calendar_label)
        vbox1.addWidget(self.calendar1)
        vbox1.addWidget(self.calendar2)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel("Type of compliance:"))
        hbox1.addWidget(self.combo_box)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(QLabel("Employee ID:"))
        hbox2.addWidget(self.employee_id_input)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.submit_button)
        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox1)
        vbox2.addLayout(hbox2)
        vbox2.addLayout(hbox3)
        hbox4 = QHBoxLayout()
        hbox4.addLayout(vbox1)
        hbox4.addLayout(vbox2)
        self.setLayout(hbox4)

        # set the window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("RTO Compliance Form")
        self.show()

    def toggle_calendar2(self, date):
        # enable the second calendar if a valid date range is selected
        if self.calendar2.isEnabled() == False:
            self.calendar2.setEnabled(True)
            self.calendar2.setMinimumDate(date)
        else:
            self.calendar2.setEnabled(False)

    def submit_form(self):
        # validate the input and store the compliance data in a database or file
        start_date = self.calendar1.selectedDate()
        end_date = self.calendar2.selectedDate() if self.calendar2.isEnabled() else start_date
        compliance_type = self.combo_box.currentText()
        employee_id = self.employee_id_input.text()

        # perform input validation, e.g. check if weekends are selected, overlapping dates, etc.

        # store the compliance data in a database or file

        # generate a report based on the compliance data

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rto_compliance_form = RTOComplianceForm()
    sys.exit(app.exec_())
