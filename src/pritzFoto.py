import os
import glob
import pickle
import shutil
import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

from clint.textui import colored, puts

os.chdir(os.path.join(os.path.dirname(os.getcwd()), "log"))
rootDic =os.path.abspath((os.path.dirname(os.getcwd())))

def copyRenameBurn(old_file_name, new_file_name,textBurn):

    src_dir= os.path.join(rootDic, "newFotos")
    dst_dir= os.path.join(rootDic, "parFotos")
    src_file = os.path.join(src_dir, old_file_name)
    #shutil.copy(src_file,dst_dir)
    
    dst_file = os.path.join(dst_dir, old_file_name)
    new_dst_file_name = os.path.join(dst_dir, new_file_name)
    #os.rename(dst_file, new_dst_file_name)

    
    img = Image.open(src_file)
    draw = ImageDraw.Draw(img)

    fonttype = os.path.join(rootDic,"src","abel-regular.ttf")
    fontSize = 32

    font = ImageFont.truetype(fonttype, fontSize)
    draw.text((0, 0),textBurn,(255,255,255),font=font)
    img.save(new_dst_file_name)

        


def scanFotoFolder(fotoFolderPath,sufix):
    
    listOfFiles = []
    for file in os.listdir(fotoFolderPath):
        if file.endswith("."+str(sufix)):
            listOfFiles.append(file)

    if len(listOfFiles) == 0:
        print "Kein neues Bild gefunden"
    elif len(listOfFiles) == 1:
        choosenIndex = 0

    else:
        print ""
        print "Es wurden mehere neue Bilder gefunden:"
        print ""
        print " Index | Bildname "
        print "------------------"
        for index, pic in enumerate(listOfFiles):
            print str(index+1).ljust(len("Index "))+" | "+str(listOfFiles[index])

        print ""
        choosenIndex = 0
        while not int(choosenIndex) in range(1,len(listOfFiles)+1):
            choosenIndex = input("Waehle >>index<< des Bildes das prozessiert werden soll: ")
            try:
                choosenIndex = int(choosenIndex)
            except:
                print "Es muss eine ganze Zahl eingegeben werden!!!"
        choosenIndex = choosenIndex-1
        print ""

    frage = str(listOfFiles[choosenIndex])+" gefunden, um welche Kennziffer handelt es sich?: "
    kn = raw_input(frage)  

    now = datetime.datetime.now()
    iD = "KN"+str(kn)+"_"+str(now).split(".")[0].replace(" ","_").replace(":","-")
    copyRenameBurn(listOfFiles[choosenIndex] ,(iD+".png"),str(iD))
    shutil.move(os.path.join(rootDic, "newFotos",str(listOfFiles[choosenIndex])), os.path.join(rootDic, "oldFotos",str(listOfFiles[choosenIndex])))


def addEntryKnDic(knDic):
    # Kennziffer Nachschlagewrk
    

    nextKnSug =  sorted(knDic.keys())[-1]+1 # Suggestion for next kennziffer

    for n in range(10):
        print ""
        newKn = raw_input(4*">"+" Welche Kennziffer soll der neue Kleber haben (Vorschlag: "+str(nextKnSug)+"): ")
        try: 
            newKn = int(newKn)
            if newKn in knDic:
                puts(colored.red( 8*">"+" Kennziffer ist schon in Verwendung bitte eine andere Wahl:"))
            else:
                print ""
                newBeschreibung = raw_input(4*">"+" Welcher Kleber verbirgt sich hinter Kennziffer "+str(newKn)+": " )
                knDic[newKn] = newBeschreibung
                showKnDic(knDic,newKn)
                break
        except:
            puts(colored.red(8*">"+" Kenziffern muessen ganze zahlen sein und auch wirklich nur Zahlen!, versuchs nochmal"))
             
    pickle.dump( knDic, open( "knDic.p", "wb" ) )

    return knDic


def showKnDic(knDic,highKn=None):
    print ""
    print " Kennziffer |  Beschreibung "
    print "---------------------------"
    for n in sorted(knDic.keys()):
        columnWidth = len(" Kennziffer ")
        columnCenter = columnWidth/2
        begin = columnCenter- len(str(n))/2
        left = columnWidth-(begin+ len(str(n)))
        if n != highKn:
            print (begin*" "+str(n)).ljust(columnWidth)+"|  "+str(knDic[n])
        else:
            puts(colored.green(begin*" "+str(n)).ljust(columnWidth)+"|  "+str(knDic[n]))
    print ""



####Function Calls
#knDic = addEntryKnDic(pickle.load( open( "knDic.p", "rb" ) ))
showKnDic(pickle.load( open( "knDic.p", "rb" ) ))
#scanFotoFolder(os.path.join(rootDic, "newFotos"),"png")











##Use with caution  <<<Functions<>>>
def emptyKnDic():
    knDic = {}
    pickle.dump( knDic, open( "knDic.p", "wb" ) )