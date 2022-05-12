import os

# по неизвестным автору причинам
# при запуске tic-tac-toe.py через idle, если не закрыть idle shell
# то окно никогда не закроется
# эта функция призвана это решить
def kill():
    os.system('taskkill /f /im pythonw.exe')