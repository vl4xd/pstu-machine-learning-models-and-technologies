import sys
from PyQt5 import QtWidgets

from app.main_window import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.ui.radioButton.clicked.connect()
        # self.ui.radioButton_2.clicked.connect()
        self.ui.pushButton.clicked.connect(self.get_predict)

    def on_model_changed(self):
        """Обработчик изменения выбора модели"""
        # if self.ui.radioButton.
        pass

    def hide_wind_speed_fields(self):
        """Скрыть поля скорости ветра"""
        pass

    def show_wind_speed_fields(self):
        """Показать поля скорости ветра"""
        pass

    def get_predict(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyApp()
    application.show()
    sys.exit(app.exec_())