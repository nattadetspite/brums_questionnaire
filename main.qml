import QtQuick 2.11
import QtQuick.Window 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.3
import QtQuick.Controls.Material 2.4
import QtQuick.Dialogs 1.1
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: mainWindow
    width : 1024
    height : 768
    Material.theme: Material.Light
    Material.primary: Material.BlueGrey
    visible : true
    title: qsTr("BRUMS test")
    footer: ToolBar {
        Row {
            anchors.centerIn: parent
            spacing: 40
            Button {
                text: 'BACK'
                onClicked: {
                    if (view.currentIndex > 0) {
                        view.currentIndex -= 1
                    }
                }
            }
            Label {
                anchors.verticalCenter: parent
                text: view.currentIndex + '/5'
            }

            Button {
                text: 'NEXT'
                highlighted: true
                Material.accent: Material.Orange
                onClicked: {
                    if (view.currentIndex < 5) {
                        view.currentIndex += 1
                    }
                }
            }
        }
    }

    SwipeView {
            id: view
            anchors.fill: parent
            Page {
                title: qsTr('Login')
                Column {
                    spacing: 40
                    anchors.centerIn: parent
                    Repeater {
                        model: ['NAME', 'AGE']
                        RowLayout {
                            spacing: 40
                            Label {
                                text: modelData
                            }
                            TextField {
                                placeholderText: 'Enter ' + modelData
                            }
                        }
                    }
                    Row {
                        RadioButton {
                            text: 'Male'
                        }
                        RadioButton {
                            text: 'Female'
                        }
                    }
                }
            }

            Page {
                title: qsTr("A")

                Column {
                    spacing: 40
                    anchors.centerIn: parent
                    Repeater {
                        id: groupA
                        model: ['Active', 'Alert', 'Angry', 'Annoyed', 'Anxious', 'Bad tempered', 'Bitter', 'Calm']
                        RowLayout {
                            width:320
                            height: 40
                            spacing: 10
                            property int sliderValue: sliderA.value
                            Label {
                                text: modelData
                                Layout.preferredWidth: 120
                                font.pointSize: 14
                            }

                            Label {
                                Layout.fillWidth: true
                                text: '1'
                            }
                            ColumnLayout {
                                spacing: 2
                                height: 100
                                Layout.fillWidth: true
                                Slider {
                                    id : sliderA
                                    value: 1
                                    from: 1
                                    to: 5
                                    stepSize: 1
                                    snapMode: Slider.SnapAlways
                                    Layout.alignment: Qt.AlignCenter
                                    onValueChanged: {
                                        console.log(value)
                                    }
                                }
                                Label {
                                    anchors.centerIn: parent
                                    text: sliderA.value
                                }
                            }
                            Label {
                                text: '5'
                                Layout.fillWidth: true
                            }
                        }
                    }
                }
            }
            Page {
                title: qsTr("B")

                Column {
                    spacing: 40
                    anchors.centerIn: parent
                    Repeater {
                        id : groupB
                        model: ['Cheerful', 'Composed', 'Confused', 'Contented', 'Depressed', 'Downhearted', 'Energetic', 'Exhausted']
                        RowLayout {
                            width:320
                            height: 40
                            spacing: 10
                            property int sliderValue: sliderB.value
                            Label {
                                text: modelData
                                Layout.preferredWidth: 120
                                font.pointSize: 14
                            }

                            Label {
                                Layout.fillWidth: true
                                text: '1'
                            }
                            ColumnLayout {
                                spacing: 2
                                height: 100
                                Layout.fillWidth: true
                                Slider {
                                    id : sliderB
                                    value: 1
                                    from: 1
                                    to: 5
                                    stepSize: 1
                                    snapMode: Slider.SnapAlways
                                    Layout.alignment: Qt.AlignCenter
                                }
                                Label {
                                    anchors.centerIn: parent
                                    text: sliderB.value
                                }
                            }
                            Label {
                                text: '5'
                                Layout.fillWidth: true
                            }
                        }
                    }
                }
            }
            Page {
                title: qsTr("C")

                Column {
                    spacing: 40
                    anchors.centerIn: parent
                    Repeater {
                        id : groupC
                        model: ['Happy', 'Lively', 'Miserable', 'Nervous', 'Panicky', 'Relaxed', 'Restful', 'Satisfied']
                        RowLayout {
                            width:320
                            height: 40
                            spacing: 10
                            property int sliderValue: sliderC.value
                            Label {
                                text: modelData
                                Layout.preferredWidth: 120
                                font.pointSize: 14
                            }

                            Label {
                                Layout.fillWidth: true
                                text: '1'
                            }
                            ColumnLayout {
                                spacing: 2
                                height: 100
                                Layout.fillWidth: true
                                Slider {
                                    id : sliderC
                                    value: 1
                                    from: 1
                                    to: 5
                                    stepSize: 1
                                    snapMode: Slider.SnapAlways
                                    Layout.alignment: Qt.AlignCenter
                                }
                                Label {
                                    anchors.centerIn: parent
                                    text: sliderC.value
                                }
                            }
                            Label {
                                text: '5'
                                Layout.fillWidth: true
                            }
                        }
                    }
                }
            }
            Page {
                title: qsTr ("D")

                Column {
                    spacing: 40
                    anchors.centerIn: parent
                    Repeater {
                        id : groupD
                        model: ['Sleepy', 'Tired', 'Uncertain', 'Unhappy', 'Worn-out', 'Worried', 'Mixed-up', 'Muddled']
                        RowLayout {
                            width:320
                            height: 40
                            spacing: 10
                            property int sliderValue: sliderD.value
                            Label {
                                text: modelData
                                Layout.preferredWidth: 120
                                font.pointSize: 14
                            }

                            Label {
                                Layout.fillWidth: true
                                text: '1'
                            }
                            ColumnLayout {
                                spacing: 2
                                height: 100
                                Layout.fillWidth: true
                                Slider {
                                    id : sliderD
                                    value: 1
                                    from: 1
                                    to: 5
                                    stepSize: 1
                                    snapMode: Slider.SnapAlways
                                    Layout.alignment: Qt.AlignCenter
                                }
                                Label {
                                    anchors.centerIn: parent
                                    text: sliderD.value
                                }
                            }
                            Label {
                                text: '5'
                                Layout.fillWidth: true
                            }
                        }
                    }
                }
            }
            Page {
                title: qsTr('finished')
                Column {
                    anchors.centerIn: parent
                    spacing: 20
                    Text {
                        text: qsTr('Thanks for participating in our research')
                        font.pointSize: 16
                    }
                    Button {
                        text: qsTr('SUBMIT')
                        highlighted: true
                        width: 400
                    }
                }
            }
        }
}
