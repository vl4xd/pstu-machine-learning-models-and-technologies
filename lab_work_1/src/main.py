import sys
from datetime import datetime
from PyQt5 import QtWidgets, QtGui

from app.main_window import Ui_MainWindow
from pipeline.models import Model1, Model2

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Создаем группу радиокнопок
        self.model_group = QtWidgets.QButtonGroup(self)
        self.model_group.addButton(self.ui.radioButton, 1)
        self.model_group.addButton(self.ui.radioButton_2, 2)
        # Подключаем сигнал изменения выбора
        self.model_group.buttonClicked.connect(self.on_model_changed)
        # Подключаем сигнал изменения выбора
        self.ui.pushButton.clicked.connect(self.get_predict)
        # Создаем модель для списка предсказаний
        self.history_model = QtGui.QStandardItemModel()
        self.ui.listView.setModel(self.history_model)
        # Начальные настройки
        self.ui.radioButton.setChecked(True) # Первая модель по умолчанию
        self.on_model_changed() # Обрабатываем поля для первой модели

    def on_model_changed(self) -> None:
        """Обработчик изменения выбора модели"""
        model_id = self.model_group.checkedId()
        match model_id:
            case 1:
                self.toggle_humidity_fieles(True)
                self.toggle_temperature_fieles(True)
                self.toggle_wind_speed_fields(False)
            case 2:
                self.toggle_humidity_fieles(True)
                self.toggle_temperature_fieles(True)
                self.toggle_wind_speed_fields(True)
            case _:
                pass

    def toggle_humidity_fieles(self, visible: bool) -> None:
        """Переключить видимость полей влажности"""
        self.ui.label_2.setVisible(visible)
        self.ui.doubleSpinBox.setVisible(visible)

    def toggle_temperature_fieles(self, visible: bool) -> None:
        """Переключить видимость полей температуры"""
        self.ui.label_3.setVisible(visible)
        self.ui.doubleSpinBox_2.setVisible(visible)

    def toggle_wind_speed_fields(self, visible: bool) -> None:
        """Переключить видимость полей скорости ветра"""
        self.ui.label_4.setVisible(visible)
        self.ui.doubleSpinBox_3.setVisible(visible)

    def add_prediction_to_history(self, text: str) -> None:
        item = QtGui.QStandardItem(text)
        self.history_model.insertRow(0, item)
        # Автоматически прокручиваем к новой записи
        self.ui.listView.scrollToTop()

    def get_predict(self) -> None:
        model_id = self.model_group.checkedId()
        
        match model_id:
            case 1:
                model = Model1()
                humidity = self.ui.doubleSpinBox.value()
                temperature = self.ui.doubleSpinBox_2.value()
                pred = model.predict(humidity, temperature)
                text = f'| {datetime.now()} | Влажность {humidity} (%) | Температура {temperature} (°C) | → Ощущаемая температура {pred:.2f} (°C)'
                self.add_prediction_to_history(text)
            case 2:
                model = Model2()
                humidity = self.ui.doubleSpinBox.value()
                temperature = self.ui.doubleSpinBox_2.value()
                wind_speed = self.ui.doubleSpinBox_3.value()
                pred = model.predict(humidity, temperature, wind_speed)
                text = f'| {datetime.now()} | Влажность {humidity} (%) | Температура {temperature} (°C) | Скорость ветра {wind_speed} (км/ч) | → Ощущаемая температура {pred:.2f} (°C)'
                self.add_prediction_to_history(text)
            case _:
                pass


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyApp()
    application.show()
    sys.exit(app.exec_())