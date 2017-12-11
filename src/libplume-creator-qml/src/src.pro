
#lessThan(QT_VERSION, 5.9) {
#        error("Plume Creator requires Qt 5.9 or greater")
#}

TARGET = plume-creator-qml
TEMPLATE = lib
DEFINES += PLUME_CREATOR_QML_LIBRARY
DESTDIR = $$top_builddir/bin/
CONFIG += c++14

QT += qml quick

SOURCES += \



HEADERS  += \ 



FORMS    += \




RESOURCES += \
    $$top_dir/readme.qrc \
    qml.qrc

OTHER_FILES += \
    main.qml

unix {
    target.path = /usr/lib/
    INSTALLS += target
}


win32:CONFIG(release, debug|release): LIBS += -L$$OUT_PWD/../../libplume-creator-data/src/release/ -lplume-creator-data
else:win32:CONFIG(debug, debug|release): LIBS += -L$$OUT_PWD/../../libplume-creator-data/src/debug/ -lplume-creator-data
else:unix: LIBS += -L$$top_builddir/bin/ -lplume-creator-data

INCLUDEPATH += $$PWD/../../libplume-creator-data/src/
DEPENDPATH += $$PWD/../../libplume-creator-data/src/

