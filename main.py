import os


def getfiles(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            f = open(file_name, "r", encoding="utf-8")
            if text in f.read():
                f = 1
                print('текст ' + "\"%s\"" % text + ' найден в файле ' + file_name)
                return True
    if f != 1:
        print('текст ' + "\"%s\"" % text + ' не найден! ')
        return False


text = input("input text : ")
path = input("path : ")
getfiles(path)
