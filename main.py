# TODO: create frontend for select the range of mood scale
#  receive data in term of csv or dat
#  collect name, age, sex

# TODO: frontend design, first page for enter name, sex and age
#  mood collection 4 page and 8 question per page

import pandas
import sys

from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Property, QStringListModel, QObject, Signal, Slot, QThread


class Backend(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        # create log csv
        head = pandas.DataFrame(['Time Stamp', 'Name', 'Age', 'Sex', 'Active', 'Alert', 'Angry', 'Annoyed'
                                    , 'Anxious', 'Bad tempered', 'Bitter', 'Calm', 'Cheerful', 'Composed'
                                    , 'Confused', 'Contented', 'Depressed', 'Downhearted', 'Energetic', 'Exhausted'
                                    , 'Happy', 'Lively', 'Miserable', 'Nervous', 'Panicky', 'Relaxed', 'Restful'
                                    , 'Satisfied', 'Sleepy', 'Tired', 'Uncertain', 'Unhappy', 'Worn-out', 'Worried'
                                    , 'Mixed-up', 'Muddled'
                                    , 'Anger', 'Tension', 'Depression', 'Vigour', 'Fatigue', 'Confusion', 'Happy', 'Calmness'])

    @Slot('QVariantList')
    def receive_packed_data(self):
        print('submit')


if __name__ == "__main__":
    sys_argv = sys.argv
    sys_argv += ['--style', 'material']  # using material component style

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()  # Engine for async front and backend program

    backend = Backend()  # define object

    engine.rootContext().setContextProperty("backend", backend)  # root core for connect object to UI

    engine.load('main.qml')  # render UI
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
