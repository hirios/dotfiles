import subprocess
import win32gui
import re


compilado = re.compile(r"""(?:^|,)(?=[^"]|(")?)"?((?(1)[^"]*|[^,"]*))"?(?=,|$)""")

def obterTarefas(exe_name):
     cmd = 'chcp 65001 | tasklist /v /fo csv | findstr /i'.split()
     output =  subprocess.Popen(cmd + [f"{exe_name}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
     output, errors = output.communicate()
     return output.decode('utf-8').strip().splitlines()


output = obterTarefas('photoshop')

if len(output) == 0:
    print('Tarefa não encontrada')
    quit()

primeira_tarefa = None
for x in output:
    if re.split(compilado, x)[-2] != 'N/A':
        primeira_tarefa = re.split(compilado, x)[-2]
        
top_windows = []
def windowEnumerationHandler(hwnd, top_window):
     top_window.append((hwnd, win32gui.GetWindowText(hwnd)))

     
win32gui.EnumWindows(windowEnumerationHandler, top_windows)

hw = None
for x in top_windows:
    if primeira_tarefa.lower() in str(x[1]).lower():
        hw = x[0]

try:
    print('Tentando setar foco...')
    print('hwnd: ', hw)
    win32gui.SetForegroundWindow(hw)
except:
    print('Erro ao setar foco')
