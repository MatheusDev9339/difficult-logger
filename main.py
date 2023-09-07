from library import libs
match input("log is necessary? (y/n)"):
    case 'y':
        avaliableTypes = 'debug, error, warn, threadError, MatheusDev'
        level = input(f"[can be automated] level of log? ({avaliableTypes})")
        libs.miawlib(level=level)
    case 'n':
        print('reading code now...')
    case 'secret':
        libs.UnusedPropositally()
from db import db
try:
    index = int(input('index (most recent is bugged): '))
    data = eval(f'db.i{index}')
    date = data['logDate']
    info = data['logInfo']
    if info == 'debug':
        result = 'only for developer purpose'
    elif info == 'error':
        result = 'failure from something. And was critical, most due a crash!'
    elif info == 'warn':
        result = 'failure from something. And have been passed.'
    elif info == 'threadError':
        result = "'How the fuck did you get this??'"
    elif info == 'MatheusDev':
        result = 'a message from dev: this is mine authograph! Love you guys!'
    else:
        result = f'{info}... again, HOW THE HOLY FUCK DO YOU GET THIS??????!!!'
    print(f"log from '{date}' is {result}")
except AttributeError:
    print("... what I told ya?")