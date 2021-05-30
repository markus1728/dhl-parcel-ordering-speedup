import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QLineEdit, QLabel, QRadioButton,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont
from WarenversandScraping import WarenversandScraping
from PaketScraping import PaketScraping


class DHLParcelOrderingSpeedup(QWidget):

    def __init__(self):
        super().__init__()

        # Insert the sender address details
        self.sender_first_name = "Max"
        self.sender_second_name = "Mustermann"
        self.sender_street = "Musterallee"
        self.sender_street_number = "10"
        self.sender_postal_code = "60318"
        self.sender_city = "Frankfurt"
        self.sender_email = "max.mustermann@gmx.com"

        self.senderAddressList = [self.sender_first_name, self.sender_second_name, self.sender_street,
                                  self.sender_street_number,
                                  self.sender_postal_code, self.sender_city, self.sender_email]

        self.init_ui()

    def init_ui(self):
        self.setGeometry(500, 200, 400, 430)
        self.setWindowTitle('DHL-Parcel-Ordering-Speedup')

        headline_font = QFont()
        headline_font.setBold(True)

        self.headline = QLabel(self)
        self.headline.setText("Receiver's Address")
        self.headline.move(80, 20)
        self.headline.setFont(headline_font)

        self.receiver_name_label = QLabel(self)
        self.receiver_name_label.setText("Name")
        self.receiver_name_label.resize(self.receiver_name_label.sizeHint())
        self.receiver_name_label.move(80, 70)

        self.receiver_street_label = QLabel(self)
        self.receiver_street_label.setText("Street")
        self.receiver_street_label.resize(self.receiver_street_label.sizeHint())
        self.receiver_street_label.move(80, 120)

        self.receiver_street_nr_label = QLabel(self)
        self.receiver_street_nr_label.setText("Number")
        self.receiver_street_nr_label.resize(self.receiver_street_nr_label.sizeHint())
        self.receiver_street_nr_label.move(80, 170)

        self.receiver_zip_code_label = QLabel(self)
        self.receiver_zip_code_label.setText("Postcode")
        self.receiver_zip_code_label.resize(self.receiver_zip_code_label.sizeHint())
        self.receiver_zip_code_label.move(80, 220)

        self.receiver_city_label = QLabel(self)
        self.receiver_city_label.setText("City")
        self.receiver_city_label.resize(self.receiver_city_label.sizeHint())
        self.receiver_city_label.move(80, 270)

        self.receiver_name_input = QLineEdit(self)
        self.receiver_name_input.resize(self.receiver_name_input.sizeHint())
        self.receiver_name_input.move(190, 70)

        self.receiver_street_input = QLineEdit(self)
        self.receiver_street_input.resize(self.receiver_street_input.sizeHint())
        self.receiver_street_input.move(190, 120)

        self.receiver_street_nr_input = QLineEdit(self)
        self.receiver_street_nr_input.resize(self.receiver_street_nr_input.sizeHint())
        self.receiver_street_nr_input.move(190, 170)

        self.receiver_zip_code_input = QLineEdit(self)
        self.receiver_zip_code_input.resize(self.receiver_zip_code_input.sizeHint())
        self.receiver_zip_code_input.move(190, 220)

        self.receiver_city_input = QLineEdit(self)
        self.receiver_city_input.resize(self.receiver_city_input.sizeHint())
        self.receiver_city_input.move(190, 270)

        self.parcel_500g_check = QRadioButton(self)
        self.parcel_500g_check.move(50, 320)
        self.parcel_500g_label = QLabel(self)
        self.parcel_500g_label.setText("'Warensendung 500g'")
        self.parcel_500g_label.move(77, 320)
        self.parcel_500g_label.setToolTip(
            "Length: max. 35,3 cm" + "\n" + "Width: max. 25 cm" + "\n" + "Height: max. 5 cm" + "\n" + "Weight: 500g")

        self.parcel_1000g_check = QRadioButton(self)
        self.parcel_1000g_check.move(50, 350)
        self.parcel_1000g_label = QLabel(self)
        self.parcel_1000g_label.setText("'Warensendung 1000g'")
        self.parcel_1000g_label.move(77, 350)
        self.parcel_1000g_label.setToolTip(
            "Length: max. 35,3 cm" + "\n" + "Width: max. 25 cm" + "\n" + "Height: max. 5 cm" + "\n" + "Weight: 1000g")

        self.parcel_2kg_check = QRadioButton(self)
        self.parcel_2kg_check.move(245, 320)
        self.parcel_2kg_label = QLabel(self)
        self.parcel_2kg_label.setText("'Paket bis 2kg'")
        self.parcel_2kg_label.move(272, 320)
        self.parcel_2kg_label.setToolTip(
            "max. 60 x 30 x 15 cm" + "\n" + "Liability up to 500€" + "\n" + "Shipment tracking")

        self.parcel_5kg_check = QRadioButton(self)
        self.parcel_5kg_check.move(245, 350)
        self.parcel_5kg_label = QLabel(self)
        self.parcel_5kg_label.setText("'Paket bis 5kg'")
        self.parcel_5kg_label.move(272, 350)
        self.parcel_5kg_label.setToolTip(
            "max. 120 x 60 x 60 cm" + "\n" + "Liability up to 500€" + "\n" + "Shipment tracking")

        self.btn = QPushButton('Start', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(170, 385)
        self.btn.clicked.connect(self.start_scraping)

        self.show()

    def start_scraping(self):
        self.receiver_address = [self.receiver_name_input.text(), self.receiver_street_input.text(),
                                 self.receiver_street_nr_input.text(),
                                 self.receiver_zip_code_input.text(), self.receiver_city_input.text()]

        if self.parcel_500g_check.isChecked():
            self.receiver_address.append("500g")
            WarenversandScraping(self.senderAddressList, self.receiver_address)
        elif self.parcel_1000g_check.isChecked():
            self.receiver_address.append("1000g")
            WarenversandScraping(self.senderAddressList, self.receiver_address)
        elif self.parcel_2kg_check.isChecked():
            self.receiver_address.append("2kg")
            PaketScraping(self.senderAddressList, self.receiver_address)
        elif self.parcel_5kg_check.isChecked():
            self.receiver_address.append("5kg")
            PaketScraping(self.senderAddressList, self.receiver_address)
        else:
            print("error")


def main():
    app = QApplication(sys.argv)
    ex = DHLParcelOrderingSpeedup()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
