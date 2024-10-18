import hashlib
import os
def aurkitu(fitxategi):
    with open(fitxategi, "rb") as f: #with erabiltzen dugu salbuespen bat gertatzen bada. rb erabiltzen da fitxategia modu binarioan irekitzeko, hau ez delako aldatzen
        info = f.read();
        kode = hashlib.new("md5")
        kode.update(info)#hash balioa kalkulatu, aurretik aukeratutako kodea erabiliz
        return kode.hexdigest() #balioa hexadezimalean bueltatu, bestela binarioan

karpeta="~/Descargas/irudia" #poned la ruta de donde tengais la carpeta que ha subido el
fitx_lista=os.listdir(karpeta)# conseguir todos los nombres de los archivos de la carpeta
aurk=False
ind=0
while aurk==False and ind<len(fitx_lista):
    fitx=fitx_lista[ind]
    fitx=karpeta+os.sep+fitx 
    if os.path.isfile(fitx): #comprueba si es un archivo o no
        hashbalioa=aurkitu(fitx) #llamar a la funcion de antes para calcular el valor hash
        if(hashbalioa=="e5ed313192776744b9b93b1320b5e268"):
            aurk=True
            print("fitxategia honako hau da " + fitx)
    ind=ind+1