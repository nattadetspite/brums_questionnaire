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
        self.packed_data = []
        # create log csv
        this_time = datetime.datetime.now()
        day = this_time.day
        month = this_time.month
        year = this_time.year
        self.file_name = str(year) + str(month) + str(day) + '.csv'
        print(self.file_name)
        # self.this_time = this_time.strftime('%c')
        head = pandas.DataFrame(columns=['Time Stamp', 'Name', 'Age', 'Sex', 'Active', 'Alert', 'Angry', 'Annoyed'
                                , 'Anxious', 'Bad tempered', 'Bitter', 'Calm', 'Cheerful', 'Composed'
                                , 'Confused', 'Contented', 'Depressed', 'Downhearted', 'Energetic', 'Exhausted'
                                , 'Happy_', 'Lively', 'Miserable', 'Nervous', 'Panicky', 'Relaxed', 'Restful'
                                , 'Satisfied', 'Sleepy', 'Tired', 'Uncertain', 'Unhappy', 'Worn-out', 'Worried'
                                , 'Mixed-up', 'Muddled'
                                , 'Anger', 'Tension', 'Depression', 'Vigour', 'Fatigue'
                                , 'Confusion', 'Happy', 'Calmness'])

        self.HOME = os.path.realpath('')
        self.LOGS = os.path.join(self.HOME, 'logs')
        os.chdir(self.LOGS)
        csv_files = glob.glob('*.csv')
        count = 1
        for csv_file in csv_files:
            print(len(csv_files))
            if csv_file == self.file_name:
                break
            if count == len(csv_files):
                print('hello2')
                head.to_csv(self.file_name, index=False)
            count += 1

        if len(csv_files) == 0:
            head.to_csv(self.file_name, index=False)
            print('hello')

        os.chdir(self.HOME)

    @Slot('QVariantList')
    def receive_packed_data(self, packed_data):
        this_time = datetime.datetime.now()
        this_time = this_time.strftime('%c')

        anger = packed_data[5] + packed_data[6] + packed_data[8] + packed_data[9]
        tension = packed_data[7] + packed_data[22] + packed_data[23] + packed_data[32]
        depression = packed_data[15] + packed_data[16] + packed_data[21] + packed_data[30]
        vigour = packed_data[3] + packed_data[4] + packed_data[17] + packed_data[20]
        fatigue = packed_data[18] + packed_data[27] + packed_data[28] + packed_data[31]
        confusion = packed_data[13] + packed_data[29] + packed_data[33] + packed_data[34]
        happy = packed_data[11] + packed_data[14] + packed_data[19] + packed_data[26]
        calmness = packed_data[10] + packed_data[12] + packed_data[24] + packed_data[25]

        data_csv = pandas.read_csv('./logs/' + self.file_name)
        print(data_csv)
        data_csv = data_csv.append({'Time Stamp': this_time, 'Name': packed_data[0], 'Age': packed_data[1]
                                    , 'Sex': packed_data[2], 'Active': packed_data[3], 'Alert': packed_data[4]
                                    , 'Angry': packed_data[5], 'Annoyed': packed_data[6], 'Anxious': packed_data[7]
                                    , 'Bad tempered': packed_data[8], 'Bitter': packed_data[9], 'Calm': packed_data[10]
                                    , 'Cheerful': packed_data[11], 'Composed': packed_data[12], 'Confused': packed_data[13]
                                    , 'Contented': packed_data[14], 'Depressed': packed_data[15]
                                    , 'Downhearted': packed_data[16] , 'Energetic': packed_data[17]
                                    , 'Exhausted': packed_data[18], 'Happy_': packed_data[19]
                                    , 'Lively': packed_data[20], 'Miserable': packed_data[21], 'Nervous': packed_data[22]
                                    , 'Panicky': packed_data[23], 'Relaxed': packed_data[24], 'Restful': packed_data[25]
                                    , 'Satisfied': packed_data[26], 'Sleepy': packed_data[27], 'Tired': packed_data[28]
                                    , 'Uncertain': packed_data[29], 'Unhappy': packed_data[30], 'Worn-out': packed_data[31]
                                    , 'Worried': packed_data[32], 'Mixed-up': packed_data[33], 'Muddled': packed_data[34]
                                    , 'Anger': anger, 'Tension': tension, 'Depression': depression, 'Vigour': vigour
                                    , 'Fatigue': fatigue, 'Confusion': confusion, 'Happy': happy, 'Calmness': calmness}
                                    , ignore_index=True)
        data_csv.to_csv('./logs/' + self.file_name, index=False)
        print(packed_data)
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
