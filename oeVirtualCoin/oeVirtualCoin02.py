# -*- coding: cp1250 -*-
#-----------------------
# 2017/11/14 - v021.ok
ver="v0.21-17/11"

import sys, os, time, random
import pygame, pyqrcode 
from pygame.locals import * # MOUSEBUTTONDOWN...
from json import *
from datetime import datetime 
from bitcoin import *

startTime = time.time()
pygame.init()

from oeLib.oePygame import *
from myWallets import *
from oeLib.oeCrypto import * 
testCrypto = True

myMatrix={}     # main
font={}             # font from extern file
myMatSil={}     # 
myMatFilt={}    # filt   

myDir = "data/"
notePrefix="B.test:"
logTime = datetime.now().strftime("%Y%m%d_%H%M%S") 
logFile = myDir+logTime+"log.txt"
fileJpg = myDir+logTime+".jpg"
filePng = myDir+logTime+".png"
filetPng = myDir+"temp.png"

coin="BTC" #LTC,NMC,VTC
wbtc = getWBTC()
wcoin = wbtc
pbtc=wbtc+wbtc
pcoin = pbtc

addLog(logFile,"octopusEngine - VirtualCoin02 - beta")
addLog(logFile,"log: "+str(logTime))

myFont = pygame.font.SysFont("monospace", 15)

# Set up some variables containing the screeen size
sizeWinX=900
sizeWinY=500

colYel = (255,255,0)
colWhi = (255,255,255)
colRed = (255,0,0)
colBlu = (0,0,255)
colSil = (128,128,128)
colBla = (0,0,0)

hA= mxW() #main matrix width
hB= mxH() #main matrix height
hBod = mxP()
hW=hA*hBod #velikost
hH=hB*hBod
hX=0   #pozice
hY=0
mxx = 7 #matrix offset
mxy = 128

winMat = pygame.display.set_mode([hA,hB]) # Create the pygame matrix window
win = pygame.display.set_mode([sizeWinX,sizeWinY]) # Create the pygame window
pygame.display.set_caption("oeVirtualCoin")        

##==================================================================
cisloCrypto = 123456789

if (testCrypto):
  cislo = cisloCrypto
  print cislo
  wifcislo = numtowif(cislo)
  print wifcislo
  print wiftonum(wifcislo)

  hextobin(hex(cislo))
  
  print "---bin---"
  strb = "aaa"
  print strb
  print strtobin(strb)
  print bintostr(strtobin(strb))
  strb = wifcislo
  print strb
  print strtobin(strb)
  print bintostr(strtobin(strb))
##==================================================================

butty = 35
bty = 10
btx1 = 660
btx2 = btx1+100
chy = 390
chyc = chy+35
ch1 = CheckBox(win,200,chy);ch1.initChBox("select 1")
ch2 = CheckBox(win,330,chy);ch2.initChBox("select 2")
ch3 = CheckBox(win,460,chy);ch3.initChBox("select 3")

ch1c = CheckBox(win,200,chyc);ch1c.initChBox("L")
ch2c = CheckBox(win,330,chyc);ch2c.initChBox("N")
ch3c = CheckBox(win,460,chyc);ch3c.initChBox("V")

bt1 = ButtBox(win,btx1,bty);bt1.labelButt("clear")        
bt3 = ButtBox(win,btx1,bty+butty);bt3.labelButt("invert")
bt5 = ButtBox(win,btx1,bty+butty*2);bt5.labelButt("noise")

bt7 = ButtBox(win,btx1,bty+butty*3);bt7.labelButt("octop")
bt9 = ButtBox(win,btx1,bty+butty*4);bt9.labelButt("world")
bt11 = ButtBox(win,btx1,bty+butty*5);bt11.labelButt(">info1")
bt13 = ButtBox(win,btx1,bty+butty*6);bt13.labelButt("info2")
bt15 = ButtBox(win,btx1,bty+butty*7);bt15.labelButt(">qr1")
bt17 = ButtBox(win,btx1,bty+butty*8);bt17.labelButt("qr2")

bt2 = ButtBox(win,btx2,bty);bt2.labelButt("save")
bt4 = ButtBox(win,btx2,bty+butty);bt4.labelButt("load")
bt6 = ButtBox(win,btx2,bty+butty*2);bt6.labelButt("> gen1 <")
bt8 = ButtBox(win,btx2,bty+butty*3);bt8.labelButt("gen2")
bt10 = ButtBox(win,btx2,bty+butty*4);bt10.labelButt("test")
bt12 = ButtBox(win,btx2,bty+butty*5);bt12.labelButt("quit")

def clickOctop():
  doBmp2Mat(myMatrix,"src/o128i.bmp",10,0)
  print "time>" + str(time.time()-startTime)
  print "printMat>"
  plotMat(win,myMatrix)
  print "time plot>" + str(time.time()-startTime)

def clickGen1():
	        global pcoin,wcoin 
                print("---gen1---")
		if (ch1.getChBox()): #sel1 = from PK
                  pkall = createWall(coin,getPBTC())
		else:
		  pkall = createWall(coin,"x") #new PK / entropy...
		        #private_key, pkwif,public_key,pubhex, wall 
                print "time info>" + str(time.time()-startTime) 
                print("0: "+str(pkall[0]))
                pcoin=str(pkall[1])
                addLog(logFile,"1: "+pcoin)
		print("("+str(len(pcoin))+")")
                addLog(logFile,"2: "+str(pkall[2]))
                addLog(logFile,"3: "+str(pkall[3]))
                wcoin=str(pkall[4])
                addLog(logFile,"4: "+wcoin)
		print("("+str(len(wcoin))+")")

def clickQr1():
                setMat(myMatrix,0)                
                mxStr(win, myMatrix,coin+".test: "+logTime,mxx,mxy)
                mxStr(win, myMatrix,wcoin,mxx,mxy+10)
                mxStr(win, myMatrix,ver,mxx,mxy+20)
                #mxStr(win, myMatrix,(wbtc+wbtc),5,161)            
                mxStr(win, myMatrix,oeShort(pcoin,17),mxx,mxy+30)    
                mxStr(win, myMatrix,"octopusEngine",mxx,mxy+40) 
           
                filetPng = myDir+"tempqr.png" 
                qrx=5
                qry=5               
                
		createQR(wcoin,3)
                addLog(logFile,wcoin)
                loadMatQR(win,filetPng,myMatrix,150,qry)
                obr = pygame.image.load(filetPng) 
                obrRect = obr.get_rect()
                obrRect = obrRect.move(200,0) #hX*2+100
                win.blit(obr, obrRect)                               
                
                addLog(logFile,pcoin)
                createQR(pcoin,2)
                loadMatQR(win,filetPng,myMatrix,qrx,qry)                
                obr = pygame.image.load(filetPng) 
                obrRect = obr.get_rect()
                obrRect = obrRect.move(10,0)
                win.blit(obr, obrRect) 
		
		createQR("123456789",1) #reset temp                         
                plotMat(win,myMatrix)
		
def clickInfo():
                print("---save---info---")                
                wifinfo = numtowif(cisloCrypto) 
		strsave = "frag "+pcoin+" ment"
                #print("wif:"+wifinfo)
                #infostr = strtobin(wifcislo)
                #hexinfo = hex(cislo)
                #print("hex:"+hexinfo)
                teststr = "abcdefgxyz123567ABCDXYZ"
		testbPrefix = "000000011111110000000"
		if (ch1.getChBox()): #sel1=test	
                   #infoMat(myMatrix,sel,"0b01010100110011001100000111110101010101")
		   infoMat(myMatrix,sel,strtobin7(teststr))
		   print teststr	
		   print strtobin7(teststr)[:100]	
                else:
		   infoMat(myMatrix,sel,testbPrefix+strtobin7(strsave))
		   #print(cisloCrypto)
		   print strsave
		   print testbPrefix+strtobin7(strsave)[:100]
                plotMat(win,myMatrix)
                print "time info save>" + str(time.time()-startTime)   

def startWin():
  print "clrMat>"
  setMat(myMatrix,0)
  print "time>" + str(time.time()-startTime)
  print "printMat>"
  plotMat(win,myMatrix)
  print "time>" + str(time.time()-startTime)

  label = myFont.render("test Virtual Coin", 1, colYel)
  win.blit(label, (chy, 10))

  ## hriste
  print "hriste>"
  doHriste(win)

  print "test znak a slovo>"
  mxChar(win, myMatrix,51,220,10,inverze=False)
  mxStr(win, myMatrix,"IMAGE text TEST",5,135)
  co = "size:" + str(hA)+"x"+str(hB)
  mxStr(win, myMatrix,co,5,145)
  mxStr(win, myMatrix,wbtc,5,155)  
  clickOctop()

#hBod=2
#creaMatSil()
#plotMatSil(300,70)
#print "time sil>" + str(time.time()-startTime)
#print "time>" + str(time.time()-startTime)
#pygame.quit()
#----------------------------------------------------------------------------

startWin()
while True:
   #time.sleep(1)
   for event in pygame.event.get():
     if event.type == MOUSEBUTTONDOWN:
        x, y = event.pos
        #print x, y
        ch1.setChBox(x,y)
        ch2.setChBox(x,y)
        ch3.setChBox(x,y)
        sel = 1
        if (ch1.getChBox()): sel = 2
        if (ch2.getChBox()): sel = 5
        if (ch3.getChBox()): sel = 10
		
	ch1c.setChBox(x,y)
        ch2c.setChBox(x,y)
        ch3c.setChBox(x,y)	
	coin = "BTC"	
	if (ch1c.getChBox()): coin = "LTC"	
        if (ch2c.getChBox()): coin = "NMC"	
        if (ch3c.getChBox()): coin = "VTC"	
        
        if bt1.testClickButt(x,y): #clear
                setMat(myMatrix,0)
                plotMat(win,myMatrix)
                print "time clear>" + str(time.time()-startTime)  
        
        if bt3.testClickButt(x,y): #invert
                #mxStr(win, myMatrix,"invert",5,155)
                invertMat(myMatrix)
                plotMat(win,myMatrix)
                print "time inv>" + str(time.time()-startTime)
                
        if bt5.testClickButt(x,y): #noise
                addnoiseMat(myMatrix)
                #mxStr(win, myMatrix,"noise",5,155)
                plotMat(win,myMatrix)
                print "time noise>" + str(time.time()-startTime) 
		
	if bt7.testClickButt(x,y): #octop
		clickOctop()
		
	if bt9.testClickButt(x,y): #world		
		doBmp2Mat(myMatrix,"src/world128x64i.bmp",10,0)
                plotMat(win,myMatrix)
                                         
        if bt11.testClickButt(x,y): #info save
		clickInfo() 
             
        if bt4.testClickButt(x,y): #info load
                print("---load---info---")
                myBin = loadMat(win,filetPng,myMatrix,sel)
                print("load bin: ")
		print(myBin[:256])
                #hexinfo=bin8tohex(myBin[:160])
		print "load > "+bin7tostr(myBin[:512])
                #print("hex:"+hexinfo)
                #print("int:"+str(int(hexinfo, base=16)))
                plotMat(win,myMatrix)
                print "time info>" + str(time.time()-startTime)
                
        if bt6.testClickButt(x,y):
                clickGen1()
		clickQr1()
                                     
        if bt15.testClickButt(x,y):  # qr1 test wallet 
                clickQr1()
		
	if bt17.testClickButt(x,y): #qr2
		setMat(myMatrix,0) #clear
		clickQr1()
		doBmp2Mat(myMatrix,"src/world128x64i.bmp",10,0)
		clickInfo() 
                plotMat(win,myMatrix)	
        
	if bt10.testClickButt(x,y):
                print("---test unspent---")
                if (ch1.getChBox()):		
                  h = history(wcoin)
                  print h
                  u = unspent(wcoin)
                  print u
                sumUnsp = str(oeJTxSumVal(unspent(wcoin)))
		print(oeShort(wcoin,8)+" > "+sumUnsp)
		#mxStr(win, myMatrix,"("+sumUnsp+")",5,mxy+20)		
		clickQr1()
		mxStr(win, myMatrix,wcoin+" ("+sumUnsp+")",mxx,mxy+10)
		plotMat(win,myMatrix)
	
        if bt2.testClickButt(x,y):
		filePng = myDir+logTime+coin[0]+".png"
                if (ch1.getChBox()):
                  saveJpg(win,fileJpg,sizeWinX, sizeWinY)
                else: 
                  winMat = pygame.display.set_mode([hA,hB]) # Create the pygame matrix window
                  #plotMat(winMat,myMatrix)             
                  saveMat(winMat,filePng,myMatrix)
		  saveMat(winMat,filetPng,myMatrix)
                  print("---ok-save: "+filePng)
                  win = pygame.display.set_mode([sizeWinX,sizeWinY]) # Create the pygame window
                  win.fill(colBla)
                  pygame.display.flip                                    
                  startWin()
     
     if event.type == pygame.QUIT:
                  sys.exit() 
