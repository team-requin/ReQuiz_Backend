'''
조민규 선배님의 Flask_Large_Application_Example 에서 흥미롭게 봐서 사용하였습니다.
'''
from termcolor import colored

def log(message: str, keyword: str="WARN"):
    if keyword == "WARN":
        print(colored('[WARN]', 'yellow'), message)
    elif keyword == "ERROR":
        print(colored('[ERROR] ' + message, 'red'))
    elif keyword == "INFO":
        print(colored('[INFO]', 'blue'), message)
    else:
        print(colored('[{}]'.format(type), 'cyan'), message)