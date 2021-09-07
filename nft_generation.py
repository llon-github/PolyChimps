#!/usr/bin/env python3

# Poly Chimps NFTs
# custom code used for OpenSea NFT generation (Polygon)

import os
import random
import sqlite3
import time
from PIL import Image
from random import randint
from random import seed
from random import shuffle

### GLOBAL VARIABLES ###

# create dirs and arrays for each layer
dirPath = os.path.dirname(os.path.realpath(__file__))
bgDir = dirPath + "\BGs\\"
monkeyDir = dirPath + "\Monkeys\\"
attributeDir = dirPath + "\Attributes\\"
saveDir = dirPath + "\PC\\"

# NFT ids for naming
nftID = 1   # 1-2500

# create DB; making 2 tables for later comparison to see if any 2 rows match
if os.path.exists("PolyChimps.db"):
  os.remove("PolyChimps.db")
else:
  print("The file does not exist")

conn = sqlite3.connect("PolyChimps.db")
db = conn.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS Chimps
             ([NFTid] string,[ChimpType] string, [Attr1] string,[Attr2] string,
             [Attr3] string,[Attr4] string,[Attr5] string,[Attr6] string)''')

def init():
    # initialize variables
    global currentAttributes

    currentAttributes = []

def offsetAttribute(attr):
    # some attributes looked better after creation at certain coordinates
    # use (-70,-10) for offset on mouth attribute "partypipe.png"
    # use (0,-10) for offset on mouth attribute "clownnose.png"
    # use (0,-10) for offset on eye attribute "roboteyes.png"
    if attr == "partypipe.png":
        x = -70
        y = -10
    elif attr == "clownnose.png" or attr == "roboteyes.png":
        x = 0
        y = -10
    else:
        x = 0
        y = 0
    
    return x, y

def attributeWeights(attr, type):
    roll = randint(1,1000)
    if attr == "Eyes":
        # alien + zombie have a different eye table than the golden/normal one
        if type == "Alien" or type == "Zombie":
            if roll <= 370:
                if type == "Alien":
                    return "alieneyes.png"
                else:
                    return "zombieeyes.png"
            elif roll > 370 and roll <= 440:
                return "3dglasses.png"
            elif roll > 440 and roll <= 480:
                if type == "Alien":
                    return "alieneyeglass.png"
                else:
                    return "zombieeyeglass.png"
            elif roll > 480 and roll <= 530:
                if type == "Alien":
                    return "alieneyepatch.png"
                else:
                    return "zombieeyepatch.png"
            elif roll > 530 and roll <= 550:
                return "lasereyes.png"
            elif roll > 550 and roll <= 620:
                return "nerdglasses.png"
            elif roll > 620 and roll <= 690:
                return "partyglasses.png"
            elif roll > 690 and roll <= 760:
                return "squareglasses.png"
            elif roll > 760 and roll <= 830:
                return "sharpspecs.png"
            elif roll > 830 and roll <= 900:
                return "squareshades.png"
            elif roll > 900 and roll <= 960:
                return "thuglife.png"
            else:
                return "vrheadset.png"
        else:
            if roll <= 50:
                return "3dglasses.png"
            elif roll > 50 and roll <= 175:
                return "cheerfuleyes.png"
            elif roll > 175 and roll <= 205:
                return "eyeglass.png"
            elif roll > 205 and roll <= 255:
                return "eyepatch.png"
            elif roll > 255 and roll <= 275:
                return "lasereyes.png"
            elif roll > 275 and roll <= 325:
                return "nerdglasses.png"
            elif roll > 325 and roll <= 450:
                return "lineeyes.png"
            elif roll > 450 and roll <= 500:
                return "partyglasses.png"
            elif roll > 500 and roll <= 580:
                return "proudeyes.png"
            elif roll > 580 and roll <= 630:
                return "squareglasses.png"
            elif roll > 630 and roll <= 660:
                return "roboteyes.png"
            elif roll > 660 and roll <= 710:
                return "sharpspecs.png"
            elif roll > 710 and roll <= 790:
                return "sleepyeyes.png"
            elif roll > 790 and roll <= 840:
                return "squareshades.png"
            elif roll > 840 and roll <= 920:
                return "staringeyes.png"
            elif roll > 920 and roll <= 970:
                return "thuglife.png"
            else:
                return "vrheadset.png"
    elif attr == "Head":
        if roll <= 75:
            return "chefhat.png"
        elif roll > 75 and roll <= 95:
            return "crown.png"
        elif roll > 95 and roll <= 145:
            return "devilhorns.png"
        elif roll > 145 and roll <= 170:
            return "greybandana.png"
        elif roll > 170 and roll <= 205:
            return "blackbandana.png"    
        elif roll > 205 and roll <= 235:
            return "jesterhat.png"
        elif roll > 235 and roll <= 275:
            return "purplemohawk.png"
        elif roll > 275 and roll <= 315:
            return "pinkmohawk.png"
        elif roll > 315 and roll <= 345:
            return "partyhat.png"
        elif roll > 345 and roll <= 375:
            return "piratehat.png"
        elif roll > 375 and roll <= 500:
            return "redbeanie.png"
        elif roll > 500 and roll <= 545:
            return "bluesweatband.png"
        elif roll > 545 and roll <= 595:
            return "redsweatband.png"
        elif roll > 595 and roll <= 695:
            return "tophat.png"
        elif roll > 695 and roll <= 745:
            return "vikinghelmet.png"
        elif roll > 745 and roll <= 870:
            return "wheatbeanie.png"
        elif roll > 870 and roll <= 920:
            return "wizardhat.png"
        elif roll > 920 and roll <= 960:
            return "greenpuff.png"
        else:
            return "yellowpuff.png"
    elif attr == "Mouth":
        if roll <= 50:
            return "banana.png"
        elif roll > 50 and roll <= 150:
            return "bubblepipe.png"
        elif roll > 150 and roll <= 350:
            return "buckteeth.png"
        elif roll > 350 and roll <= 450:
            return "cigarette.png"
        elif roll > 450 and roll <= 600:
            return "tongue.png"
        elif roll > 600 and roll <= 800:
            return "vampireteeth.png"
        elif roll > 800 and roll <= 900:
            return "vape.png"
        elif roll > 900 and roll <= 950:
            return "bubblegum.png"
        else:
            return "pacifier.png"
    
    elif attr == "Nose":
        if roll <= 200:
            return "clownnose.png"
        elif roll > 200 and roll <= 700:
            return "nostrils.png"
        elif roll > 700 and roll <= 800:
            return "heart.png"
        else:
            return "roseycheeks.png"
    elif attr == "Hands":
        return "blank.png"
        # if roll <= 300:
        #     return "bikergloves.png"
        # elif roll > 300 and roll <= 400:
        #     return "infinitygauntlets.png"
        # elif roll > 400 and roll <= 600:
        #     return "boxinggloves.png"
        # elif roll > 600 and roll <= 800:
        #     return "mmagloves.png"
        # else:
        #     return "mittens.png"
    elif attr == "Ears":
        if roll <= 80:
            return "goldring.png"
        elif roll > 80 and roll <= 150:
            return "goldcross.png"
        elif roll > 150 and roll <= 220:
            return "goldstud.png"
        elif roll > 220 and roll <= 270:
            return "goldringandcross.png"
        elif roll > 270 and roll <= 330:
            return "goldringandstud.png"
        elif roll > 330 and roll <= 400:
            return "silverring.png"
        elif roll > 400 and roll <= 470:
            return "silvercross.png"
        elif roll > 470 and roll <= 540:
            return "silverstud.png"
        elif roll > 540 and roll <= 590:
            return "silverringandcross.png"
        elif roll > 590 and roll <= 640:
            return "silverringandstud.png"
        elif roll > 640 and roll <= 710:
            return "obsidianring.png"
        elif roll > 710 and roll <= 780:
            return "obsidiancross.png"
        elif roll > 780 and roll <= 850:
            return "obsidianstud.png"
        elif roll > 850 and roll <= 900:
            return "obsidianringandcross.png"
        elif roll > 900 and roll <= 950:
            return "obsidianringandstud.png"
        else:
            return "earpods.png"
    else:
        print("Error calculating weights")

def createNFT(numberCreated):
    global nftID
    monkeyAry = []
    attrAry = []

    while numberCreated > 0:
        # get monkey type; corresponding BG layer auto-applied depending on the monkey type chosen
        # 94% normal, 3% golden, 2% zombie, 1% alien
        monkeyType = randint(1, 100)
        if monkeyType <= 94:
            monkeyLayer = Image.open(monkeyDir + "normal_mk.png")
            bgLayer = Image.open(bgDir + "normal_bg.png")
            monkeyAry.append("Normal")
            currentColor = "Normal"
        elif monkeyType > 94 and monkeyType <= 97:
            monkeyLayer = Image.open(monkeyDir + "golden_mk.png")
            bgLayer = Image.open(bgDir + "golden_bg.png")
            monkeyAry.append("Golden")
            currentColor = "Golden"
        elif monkeyType > 97 and monkeyType <= 99:
            monkeyLayer = Image.open(monkeyDir + "zombie_mk.png")
            bgLayer = Image.open(bgDir + "zombie_bg.png")
            monkeyAry.append("Zombie")
            currentColor = "Zombie"
        else:
            monkeyLayer = Image.open(monkeyDir + "alien_mk.png")
            bgLayer = Image.open(bgDir + "alien_bg.png")
            monkeyAry.append("Alien")
            currentColor = "Alien"

        # combine the monkey and bg layers
        bgLayer.paste(monkeyLayer, (0,0), monkeyLayer)

        # get individual attributes and then shuffle the array
        attrAry = os.listdir(attributeDir)
        random.shuffle(attrAry)

        # iterate through the attributes and roll to see if it is added
        attrCounter = 0;
        for attr in attrAry:
            if attr == "Eyes":
                getAttrName = attributeWeights(attr, currentColor)
                eyeLayer = Image.open(attributeDir + attr + "\\" + getAttrName)
                x,y = offsetAttribute(getAttrName)
                bgLayer.paste(eyeLayer, (x,y), eyeLayer)
                currentAttributes.append(getAttrName)
                attrCounter += 1
            else:
                # roll to determine if you get a particular attribute
                # 0 => 90%, 1 => 80%, 2 => 60%, 3 => 40%, 4 => 20%, 5 => 10%
                roll = randint(1, 100)
                if attrCounter == 0:
                    if roll >= 1 and roll <= 90:
                        getAttrName = attributeWeights(attr, currentColor)
                        newLayer = Image.open(attributeDir + attr + "\\" + getAttrName)
                        x,y = offsetAttribute(getAttrName)
                        bgLayer.paste(newLayer, (x,y), newLayer)
                        currentAttributes.append(getAttrName)
                        attrCounter += 1
                    else:
                        # add attribute as "none" and skip to next attribute
                        currentAttributes.append("none")
                elif attrCounter == 1:
                    if roll >= 1 and roll <= 80:
                        getAttrName = attributeWeights(attr, currentColor)
                        newLayer = Image.open(attributeDir + attr + "\\" + getAttrName)
                        x,y = offsetAttribute(getAttrName)
                        bgLayer.paste(newLayer, (x,y), newLayer)
                        currentAttributes.append(getAttrName)
                        attrCounter += 1
                    else:
                        # do nothing, skip to next attribute
                        currentAttributes.append("none")
                elif attrCounter == 2: 
                    if roll >= 1 and roll <= 60:
                        getAttrName = attributeWeights(attr, currentColor)
                        newLayer = Image.open(attributeDir + attr + "\\" + getAttrName)
                        x,y = offsetAttribute(getAttrName)
                        bgLayer.paste(newLayer, (x,y), newLayer)
                        currentAttributes.append(getAttrName)
                        attrCounter += 1
                    else:
                        # do nothing, skip to next attribute
                        currentAttributes.append("none")
                elif attrCounter == 3: 
                    if roll >= 1 and roll <= 40:
                        getAttrName = attributeWeights(attr, currentColor)
                        newLayer = Image.open(attributeDir + attr + "\\" + getAttrName)
                        x,y = offsetAttribute(getAttrName)
                        bgLayer.paste(newLayer, (x,y), newLayer)
                        currentAttributes.append(getAttrName)
                        attrCounter += 1
                    else:
                        # do nothing, skip to next attribute
                        currentAttributes.append("none")
                elif attrCounter == 4:
                    if roll >= 1 and roll <= 20:
                        getAttrName = attributeWeights(attr, currentColor)
                        newLayer = Image.open(attributeDir + attr + "\\" + getAttrName)
                        x,y = offsetAttribute(getAttrName)
                        bgLayer.paste(newLayer, (x,y), newLayer)
                        currentAttributes.append(getAttrName)
                        attrCounter += 1
                    else:
                        # do nothing, skip to next attribute
                        currentAttributes.append("none")
                else:  
                    if roll >= 1 and roll <= 10:
                        getAttrName = attributeWeights(attr, currentColor)
                        newLayer = Image.open(attributeDir + attr + "\\" + getAttrName)
                        x,y = offsetAttribute(getAttrName)
                        bgLayer.paste(newLayer, (x,y), newLayer)
                        currentAttributes.append(getAttrName)
                        attrCounter += 1
                    else:
                        # do nothing, skip to next attribute
                        currentAttributes.append("none") 
        
        # save img, add chimp to DB, increment NFT id, and subtract from total # to be created
        if nftID >= 1 and nftID < 10:
            nftIDformatted = "000" + str(nftID)
        elif nftID >= 10 and nftID < 100:
            nftIDformatted = "00" + str(nftID)
        elif nftID >= 100 and nftID < 1000:
            nftIDformatted = "0" + str(nftID)
        else:
            nftIDformatted = str(nftID)

        bgLayer.save(saveDir + "PolyChimp #" + nftIDformatted + ".png")
        db.execute('INSERT INTO Chimps VALUES (?,?,?,?,?,?,?,?)', ("#" + nftIDformatted, monkeyAry[nftID - 1],
                   currentAttributes[0], currentAttributes[1], currentAttributes[2], currentAttributes[3],
                   currentAttributes[4], currentAttributes[5]))
        conn.commit()

        nftID += 1
        numberCreated -= 1

        # re-initialize variables
        init()
    
    # metadata
    # total number of each monkey type
    print("Normal: " + str(monkeyAry.count("Normal")))
    print("Golden: " + str(monkeyAry.count("Golden")))
    print("Zombie: " + str(monkeyAry.count("Zombie")))
    print("Alien: " + str(monkeyAry.count("Alien")))

    # checking for any duplicate chimps; if count > 1 then there are duplicates
    test2 = db.execute("SELECT count(*), NFTid, attr1, attr2, attr3, attr4, attr5, attr6 FROM Chimps\
                        GROUP BY NFTid, attr1, attr2, attr3, attr4, attr5, attr6 HAVING COUNT(*) > 1;")
    data2 = db.fetchall()
    if not data2:
        print("There are no duplicate NFTs.")
    else:
        print("There are duplicate NFTs!")

# pass in any number to create that number of NFTs
init()
createNFT(2500)


