from pyautogui import locateOnScreen, moveTo, leftClick, alert, center
from keyboard import send
from time import sleep
import PySimpleGUI as sg
from threading import Thread
import os
import win32api, win32con
import ctypes
from pygetwindow import getWindowsWithTitle
import sys


# Function to check if the window is closed
def verificar_janela_fechada(window):
    return window == Firefox and event == sg.WIN_CLOSED


# Interface gráfica para a janela de login
# GUI for the login window
def janela_login():
    sg.change_look_and_feel('Black')
    Layout = [
        [sg.Text('____ TBB ____', font=('Helvetica', 16, 'bold'))],
        [sg.Button('Enter Bot')],       
    ]
    return sg.Window('Fire test', layout=Layout,finalize=True)

# Interface gráfica para a janela de opções do bot
# GUI for the bot options window
def janela_bot():
    Layout = [
        [sg.Text('___ Enter Bot ___', font=('Helvetica', 16, 'bold'))],
        [sg.Button('Bot')], [sg.Button('Opacity')], [sg.Button('Exit')]]
    return sg.Window('##_BOT_OPTIONS_##', layout=Layout,finalize=True)

# Interface gráfica para a janela principal do bot
# GUI for the main bot window
def janela_principal():
    Layout = [
        [sg.Text('________ BOT OPTIONS _______', font=('Helvetica', 16, 'bold'))],
        [sg.Text('______  Atack ______', font=('Helvetica', 16, 'bold'), text_color='red')],
        [sg.Text("Hotkey Spell:"), sg.Input(key='-CARACTERE-', size=(1, 1)), sg.Text("Coldown:"), sg.Input(key='-CARACTERE2-', size=(1, 1))],
        [sg.Checkbox('Atack', font=('Helvetica', 16, 'bold'), default=False, key='atack')],
        [sg.Button('Confirm atk')],
        [sg.Text('______ Support ______', font=('Helvetica', 16, 'bold'), text_color='Grey')],
        [sg.Checkbox('Mana', font=('Helvetica', 16, 'bold'), text_color='Blue', default=False, key='manareg')], [sg.Text("Hotkey Mana:"), sg.Input(key='-CARACTEREMana', size=(1, 1))],[sg.Button('Confirm Mana')],
        [sg.Checkbox('Regen', font=('Helvetica', 16, 'bold'), text_color='#32CD32',default=False, key='regen')],[sg.Text("Hotkeys is 1, 2, 3")],
        [sg.Text('______ Auto Loot ______', font=('Helvetica', 16, 'bold'), text_color='Yellow')],
        [sg.Checkbox('Loot', font=('Helvetica', 16, 'bold'), default=False, key='catar')],
        [sg.Text('______ Auto ring e Food _____', font=('Helvetica', 16, 'bold'), text_color='orange')],
        [sg.Checkbox('Ring', font=('Helvetica', 16, 'bold'), default=False, key='ring'), sg.Text("Hotkey:"), sg.Input(key='-CARACTEREring', size=(1, 1)), sg.Button('Confirm ring')],
        [sg.Checkbox('Food', font=('Helvetica', 16, 'bold'), default=False, key='food'), sg.Text("Hotkey:"), sg.Input(key='-CARACTEREfood', size=(1, 1)), sg.Button('Confirm food')],
        [sg.Text('______ Cave Bot ______', font=('Helvetica', 16, 'bold'), text_color='Purple')],
        [sg.Checkbox('Run Cavebot', font=('Helvetica', 16, 'bold'), default=False, key='Cavebot')],
        [sg.Button('Back'), sg.Button('Play!'), sg.Button('Stop'), sg.Button('Exit')],
    ]

    return sg.Window('Firefox', layout=Layout,finalize=True)

# Função para ajustar a opacidade da janela do Tibia
# Function to adjust the opacity of the Tibia window
def opacidade():
    GWL_EXSTYLE = -20
    WS_EX_LAYERED = 0x00080000
    LWA_ALPHA = 0x00000002
    
    OPACITY = 1  # 0 -- 255
    WINDOW_TITLE = "Tibia"

    windows = getWindowsWithTitle(WINDOW_TITLE)

    if windows:
        target_window = windows[0]
        target_hwnd = target_window._hWnd
        ex_style = ctypes.windll.user32.GetWindowLongA(target_hwnd, GWL_EXSTYLE)
        ctypes.windll.user32.SetWindowLongA(target_hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)
        ctypes.windll.user32.SetLayeredWindowAttributes(target_hwnd, 0, OPACITY, LWA_ALPHA)
        alert("Tibia Window opacity modified.")
    else:
        alert("Tibia Window not found.")
        

# Caminhos para imagens utilizadas no script
# Paths for images used in the script on computacional visional template match
imgvida2 = 'E:/TEST TB/imagens test TB/images/semvida2.png'
imgsemvida = 'E:/TEST TB/imagens test TB/images/semvida.png'
imgvida3 = 'E:/TEST TB/imagens test TB/images/semvida3.png'
imgmana = 'E:/TEST TB/imagens test TB/images/semmana.png'
battle = 'E:/TEST TB/imagens test TB/images/battle.PNG'
Bred = 'E:/TEST TB/imagens test TB/images/Bred.PNG'
ring = 'E:/TEST TB/imagens test TB/images/ring.PNG'
food = 'E:/TEST TB/imagens test TB/images/food.PNG'
rat = 'E:/TEST TB/imagens test TB/images/rat.png'
ways = ['E:/TEST TB/imagens test TB/images/way1.png','E:/TEST TB/imagens test TB/images/way2.png','E:/TEST TB/imagens test TB/images/way3.png',
        'E:/TEST TB/imagens test TB/images/way4.png','E:/TEST TB/imagens test TB/images/way5.png']
point = 'E:/TEST TB/imagens test TB/images/player_point.png'

way1 = ways[0]
way2 = ways[1]
way3 = ways[2]
way4 = ways[3]
way5 = ways[4]

# Função para simular um clique do mouse em coordenadas (x, y)
# Function to simulate a mouse click at coordinates (x, y)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,5)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,5)
    
# Função principal do Cavebot
# Main function for Cavebot
def Cavebot():
    var1 = False
    parar19 = True
    way_list = [way1, way2, way3, way4]  # Lista com as imagens dos caminhos
    index = 0  # Índice para acompanhar o caminho atual
    direcao = 1  # 1 para avançar, -1 para Back
    while (parar19):
        if verificar_janela_fechada(window):
            window.Close()
            break
        elif window == Firefox and event == 'Stop':
            parar19 = False
            break
        elif window == Firefox and event == 'Exit':
            window.Close()
            break
        # Verificar se a imagem Bred não está na região específica
        # Check if the Bred image is not in the specific region
        if not locateOnScreen(Bred, region=(1429, 385, 16, 3)):
            if 0 <= index < len(way_list):
                way = way_list[index]
                # Verifique se a imagem foi encontrada na tela com confiança de 80%
                # Check if the image is found on the screen with 80% confidence
                result = locateOnScreen(way, confidence=0.8, region=(1433, 25, 108, 112))
                # Verifique se a imagem foi encontrada antes de prosseguir
                # Check if the image is found before proceeding
                if result is not None:
                    x, y, width, height = result  # Extrair as coordenadas e dimensões
                                                  # Extract coordinates and dimensions
                    x_centered = x + width // 2
                    y_centered = y + height // 2
                    moveTo(x_centered, y_centered)
                    leftClick(x_centered, y_centered)
                    sleep(7)
                    # Verifique se a imagem Point não foi encontrada
                    # Check if the Point image is not found
                    if locateOnScreen(point, confidence=0.9, region=(1433, 25, 108, 112)):
                        continue  # Continue clicando no mesmo way // Continue clicking on the same way
            index += direcao  # Avance ou retroceda no índice // Move forward or ward in the index
            if index == len(way_list) or index == -1:
                direcao *= -1  # Inverter a direção quando atingir o final ou o início
                               # Invert the direction when reaching the end or the beginning
        else:
            sleep(5)  # Pausa de 5 segundos se a imagem Bred for encontrada
                      # 5-second pause if the Bred image is found
            
    alert("O Cavebot finished")

# Função para simular o uso de um anel
# Function to simulate using a ring
def Ring():
    parar18 = True
    while (parar18):
        if verificar_janela_fechada(window):
            window.Close()
            break
        elif window == Firefox and event == 'Stop':
            parar18 = False
            break
        elif window == Firefox and event == 'Exit':
            window.Close()
            break
        elif locateOnScreen(ring, region=(1443, 264, 12, 13)):
            send(anel)
            sleep(1)
        else:
            sleep(1)
    alert("Ring finished")         
 
# Função para simular o uso de comida
# Function to simulate using food
def Food():
    parar17 = True
    while (parar17):
        if verificar_janela_fechada(window):
            window.Close()
            break 
        elif window == Firefox and event == 'Stop':
            parar17 = False
            break
        elif window == Firefox and event == 'Exit':
            window.Close()
            break
        if locateOnScreen(food, confidence=0.9):
            send(comer)
            sleep(1)
            
    alert("Food finished")
 
# Função para regeneração de vida
# Function for life regeneration
def Regen():
    parar5 = True
    while (parar5):
        if verificar_janela_fechada(window):
            window.Close()
            break 
        elif window == Firefox and event == 'Stop':
            parar5 = False
            break
        elif window == Firefox and event == 'Exit':
            window.Close()
            break    
        #Cura nivel 4
        #elif locateOnScreen(imgvida2, region=(1530, 141, 15, 10)):
            #send("4")
            #sleep(1)
        #Cura nivel 3
        elif locateOnScreen(imgvida3, region=(1485, 141, 12, 10)):
            send("3")
            sleep(1)
        #Cura nivel 2    
        elif locateOnScreen(imgvida2, region=(1512, 143, 12, 10)):
            send("2")
            sleep(1)
        #Cura nivel 1
        elif locateOnScreen(imgsemvida, region=(1530, 141, 12, 10)):
            send("1")
            sleep(1)
        
    alert("Regen finished")
          

# Função para regeneração de mana
# Function for mana regeneration
def Mana():
    parar4 = True
    while (parar4):
        if verificar_janela_fechada(window):
            window.Close()
            break 
        elif window == Firefox and event == 'Stop':
            parar4 = False
            break
        elif window == Firefox and event == 'Exit':
            window.Close()
            break
        elif locateOnScreen(imgmana, region=(1479, 155, 12, 10)):
            send(Manas)
            sleep(1)
    alert("Mana finished")    

# Defina o diretório onde estão armazenadas as imagens
# Set the directory where the images are stored
diretorio_imagens = 'E:/TEST TB/imagens'
diretorio_imagens = os.path.join(os.path.dirname(__file__), 'imagens')

if getattr(sys, 'frozen', False):
    # Executando em um executável compilado (PyInstaller)
    diretorio_atual = os.path.dirname(sys.executable)
else:
    # Executando a partir do código-fonte (Python normal)
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Combine o diretório atual com o diretório "imagens"
# Combine the current directory with the "imagens" directory
diretorio_imagens = os.path.join(diretorio_atual, 'imagens')

# Lista de nomes de arquivo das imagens na pasta
# List of file names of the images in the folder
imagens = os.listdir(diretorio_imagens)

# Região específica da tela onde você deseja procurar as imagens
# Specific region of the screen where you want to search for images
regiao_tela = (608, 306, 175, 175)
        
# Função para realizar o loot de itens
# Function to perform item loot
def Loot():
    parar3 = True
    while (parar3):
        if verificar_janela_fechada(window):
            window.Close()
            break

        elif window == Firefox and event == 'Stop':
            parar3 = False
            break

        elif window == Firefox and event == 'Exit':
            window.Close()
            break

        # Loop para verificar cada imagem
        # Loop to check each image
        for imagem_nome in imagens:
            imagem_path = os.path.join(diretorio_imagens, imagem_nome)
            # Verifica se a imagem atual está na tela com uma confiança de 0.8
            # Check if the current image is on the screen with 80% confidence
            loot = locateOnScreen(imagem_path, confidence=0.9, region=regiao_tela)
            if loot is not None:
                # Se a imagem foi encontrada, obtenha as coordenadas do centro
                # If the image is found, get the cEnter Bot coordinates
                x, y = center(loot)
                sleep(2)
                moveTo(x, y)
                click(x, y)
                # Aguarde um breve período antes de continuar
                # Wait for a brief period before continuing
                sleep(0.5)

    alert("Loot finished")

# Função para atacar inimigos
# Function to attack enemies
def Atack():
    parar2 = True
    while (parar2):
        if verificar_janela_fechada(window):
            window.Close()
            break
        elif window == Firefox and event == 'Stop':
            parar2 = False
            break

        elif window == Firefox and event == 'Exit':
            window.Close()
            break

        var1 = True
        if locateOnScreen(battle, region=(1427, 374, 101, 56)):
            var1 = True
            sleep(1)
        else:
            if locateOnScreen(Bred, region=(1429, 385, 16, 3)):
                var1 = True
                sleep(1)
            else:
                var1 = False
        if var1 == False:
            send("space")
            sleep(1) 
        '''if var2 == True:
            send(atacar)
            sleep(coldown)'''
            
    alert("Atack finished")  
            
# Inicialização das janelas e variáveis
# Initialize windows and variables
janela1, janela2, Firefox = janela_login(), None, None

#loop principal
#Main Loop
while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        window.Close()
        break
    
    elif window == janela2 and event == sg.WIN_CLOSED:
        window.Close()
        break
    
    elif window == Firefox and event == sg.WIN_CLOSED:
        window.Close()
        break
    
    elif window == janela1 and event == 'Enter Bot':
        janela2 = janela_bot()
        janela1.hide()
        
    elif window == janela2 and event == 'Back':
        janela2.hide()
        janela1.un_hide()
        
    elif window == janela2 and event == 'Bot':
        Firefox = janela_principal()
        janela1.hide()
        janela2.hide()
        
    elif window == janela2 and event == 'Opacity':
        opacidade()
        
    elif window == Firefox and event == 'Back':
        janela2.un_hide()
        Firefox.hide()
        
    if window == janela2 and event == 'Exit':
        window.Close()
        break
    
    elif window == Firefox and event == 'Exit':
        window.Close()
        break
    
    elif window == janela1 and event == 'Exit':
        window.Close()
        break
    
    elif event == 'Confirm atk':
        atacar = values['-CARACTERE-']
        coldown = values['-CARACTERE2-']
        
        if len(atacar) > 0:
            sg.popup("You inserted a hotkey:", atacar)
        else:
            sg.popup("Invalid Enter Bot. Be sure to Enter Bot at least one character or number.")
        if len(coldown) > 0:
            sg.popup("You inserted coldown:", coldown)
        else:
            sg.popup("Invalid Enter Bot. Be sure to Enter Bot at least one character or number.")
            
    elif event == 'Confirm ring':
        anel = values['-CARACTEREring']
        
        if len(anel) > 0:
            sg.popup("You inserted a hotkey:", anel)
        else:
            sg.popup("Invalid Enter Bot. Be sure to Enter Bot at least one character or number.")
            
    elif event == 'Confirm food':
        comer = values['-CARACTEREfood']
        
        if len(comer) > 0:
            sg.popup("You inserted a hotkey:", comer)
        else:
            sg.popup("Invalid Enter Bot. Be sure to Enter Bot at least one character or number.")
            
    elif event == 'Confirm Mana':
        Manas = values['-CARACTEREMana']
        
        if len(Manas) > 0:
            sg.popup("You inserted a hotkey da Mana:", Manas)
        else:
            sg.popup("Invalid Enter Bot. Certifique-se de inserir pelo menos um caractere ou número.")        
                 
    elif window == Firefox and event == 'Play!':
        if values['manareg'] == True:
            Thread(target=Mana).start() 
        if values['regen'] == True:
            Thread(target=Regen).start()
        if values['atack'] == True:
            Thread(target=Atack).start()
        if values['catar'] == True:
            Thread(target=Loot).start()
        if values['ring'] == True:
            Thread(target=Ring).start()
        if values['food'] == True:
            Thread(target=Food).start()
        if values['Cavebot'] == True:
            Thread(target=Cavebot).start()