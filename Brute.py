import random 
import pyautogui
import string

#faz uma lista de todas as letras 

#letras = "abcdefghijklmnopqrstuvwxyz0123456789"#

letras = string.printable
letas_lista = list(letras)

#captura a senha usando a interface do pyautogui
senha = pyautogui.password("Digite uma senha : ")

#armazena a senha do usuario como uma string vazia
user_senha = ""

while(user_senha != senha):
    user_senha = random.choices(letas_lista, k=len(senha))
    
    print('\033[1;32m'+"=="+str(user_senha)+ "=="+'\033[1;32m')

    if(user_senha == list(senha)):
        print("sua senha e : "+ "".join(user_senha))
        break
