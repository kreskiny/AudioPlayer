import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QLineEdit

class InteractiveReceipt(QWidget):
    def __init__(self):
        super(InteractiveReceipt, self).__init__()

        # Инициализация основных компонентов
        self.tableWidget = QTableWidget(self)
        self.total = QLineEdit(self)
        self.total.setReadOnly(True)

        # Установка заголовков таблицы
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Товар", "Цена", "Количество"])

        # Установка макета
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(QLabel("Итоговая сумма:"))
        layout.addWidget(self.total)
        self.setLayout(layout)

        # Загрузка данных из файла
        self.load_data_from_file("price.csv")

        # Связывание событий
        self.tableWidget.cellChanged.connect(self.update_total)

    def load_data_from_file(self, filename):
        # Предполагается, что файл имеет формат "название товара;цена"
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(";")
                if len(data) == 2:
                    self.add_row(data[0], float(data[1]))

    def add_row(self, item_name, price):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        # Заполнение ячеек таблицы
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(item_name))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(price)))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem("0"))

    def update_total(self):
        total_sum = 0.0
        for row in range(self.tableWidget.rowCount()):
            price = float(self.tableWidget.item(row, 1).text())
            quantity = float(self.tableWidget.item(row, 2).text())
            total_sum += price * quantity

        # Обновление значения итоговой суммы
        self.total.setText(str(total_sum))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InteractiveReceipt()
    window.show()
    sys.exit(app.exec_())
