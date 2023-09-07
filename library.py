class libs:
    file_location = 'db.py'
    def getCurrentX():
        import db
        newX = db.x.x + 1
        return newX
    def getCurrentDate():
        import datetime
        today = datetime.datetime.today()
        return today
    def updateX(old_x):
        import shutil, tempfile
        with open(libs.file_location, 'r') as file,  tempfile.NamedTemporaryFile('w', delete=False) as out:
            for line in file:
                get_x = str(line[:5])
                if get_x == '    x':
                    newX = int(old_x) + 1
                    line = line[:5] + f' = {newX}\n'
                out.write(line)
        shutil.move(out.name, libs.file_location)
    def miawlib(level):
    # using OBJECT do: 
        import json
        date = libs.getCurrentDate()
        method = 'a+'
        newX = libs.getCurrentX()
        text = {"logDate":f"{date}","logInfo": f"{level}"}
        with open(libs.file_location, method) as f:
            f.write(f'    i{newX} = {text}\n')
            f.close()
        libs.updateX(newX-1)
        print(f"log done!, log: 'i{newX} = {text}'")
    def UnusedPropositally():
# del all and reset things
        with open(libs.file_location, 'w') as file:
            file.write("class x:\n    x = 0\nclass db:\n    i0 = {'logDate': '2023-09-06 23:34:00', 'logInfo': 'MatheusDev'}\n")