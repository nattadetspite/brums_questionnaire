# TODO: create frontend for select the range of mood scale
#  receive data in term of csv or dat
#  collect name, age, sex

# TODO: signal submit button from frontend to emit backend function
#  backend function receive package and collect in term os csv files

import pandas
import sys
import os
import glob
import datetime
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Property, QStringListModel, QObject, Signal, Slot, QThread


class Backend(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        # create log csv
        this_time = datetime.datetime.now()
        day = this_time.day
        month = this_time.month
        year = this_time.year
        file_name = str(year) + str(month) + str(day) + '.csv'
        # this_time = this_time.strftime('%c')

        head = pandas.DataFrame(['Time Stamp', 'Name', 'Age', 'Sex', 'Active', 'Alert', 'Angry', 'Annoyed'
                                , 'Anxious', 'Bad tempered', 'Bitter', 'Calm', 'Cheerful', 'Composed'
                                , 'Confused', 'Contented', 'Depressed', 'Downhearted', 'Energetic', 'Exhausted'
                                , 'Happy', 'Lively', 'Miserable', 'Nervous', 'Panicky', 'Relaxed', 'Restful'
                                , 'Satisfied', 'Sleepy', 'Tired', 'Uncertain', 'Unhappy', 'Worn-out', 'Worried'
                                , 'Mixed-up', 'Muddled'
                                , 'Anger', 'Tension', 'Depression', 'Vigour', 'Fatigue'
                                , 'Confusion', 'Happy', 'Calmness'])

        HOME = os.path.realpath('')
        LOGS = os.path.join(HOME, 'logs')
        os.chdir(LOGS)
        csv_files = glob.glob('*.csv')
        count = 1
        for csv_file in csv_files:
            if csv_file == file_name:
                break
            if count == len(csv_files):
                head.to_csv('./logs/' + file_name, index="false")
            count += 1

    @Slot('QVariantList')
    def receive_packed_data(self, packed_data):
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
