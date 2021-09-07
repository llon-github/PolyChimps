# script to generate metadata for OpenSea NFTs

import os
import sqlite3
import json

# function to filter out attributes
def getAttributes():
    # array to return back to main that has edited attributes for each chimp
    attributeAry = []
    dbAttr = db.execute('SELECT nftid, chimptype, attr1, attr2, attr3, attr4 ,attr5 ,attr6 FROM Chimps')
    data = dbAttr.fetchall()
    
    for d in data:
        tupleList = list(d)
        # remove none element and blank.png elements (formerly gloves)
        while "none" in tupleList:
            tupleList.remove("none")
        while "blank.png" in tupleList:
            tupleList.remove("blank.png")
        attributeAry.append(tupleList)

    return attributeAry

def convertPNGname(attr):
    switch = {
        # Ears
        "earpods.png":"Ear Pods",
        "goldcross.png":"Gold Cross",
        "goldring.png":"Gold Ring",
        "goldringandcross.png":"GRing Cross",
        "goldringandstud.png":"GRing Stud",
        "goldstud.png":"Gold Stud",
        "obsidiancross.png":"Obsidian Cross",
        "obsidianring.png":"Obsidian Ring",
        "obsidianringandcross.png":"ORing Cross",
        "obsidianstud.png":"Obsidian Stud",
        "obsidianringandstud":"ORing Stud",
        "silvercross.png":"Silver Cross",
        "silverring.png":"Silver Ring",
        "silverringandcross.png":"SRing Cross",
        "silverringandstud.png":"SRing Stud",
        "silverstud.png":"Silver Stud",
        # Eyes
        "3dglasses.png":"3D-Glasses",
        "alieneyes.png":"Alien Eyes",
        "alieneyeglass.png":"Eye Glass",
        "alieneyepatch.png":"Eye Patch",
        "cheerfuleyes.png":"Cheerful Eyes",
        "eyeglass.png":"Eye Glass",
        "eyepatch.png":"Eye Patch",
        "lasereyes.png":"Laser Eyes",
        "lineeyes.png":"Line Eyes",
        "nerdglasses.png":"Nerd Glasses",
        "partyglasses.png":"Party Glasses",
        "proudeyes.png":"Proud Eyes",
        "roboteyes.png":"Robot Eyes",
        "sharpspecs.png":"Sharp Specs",
        "sleepyeyes.png":"Sleepy Eyes",
        "squareglasses.png":"Square Glasses",
        "squareshades.png":"Square Shades",
        "staringeyes.png":"Staring Eyes",
        "thuglife.png":"Thug Life Glasses",
        "vrheadset.png":"VR Headset",
        "zombieeyes.png":"Zombie Eyes",
        "zombieeyeglass.png":"Eye Glass",
        "zombieeyepatch.png":"Eye Patch",
        # Head
        "blackbandana.png":"Black Bandana",
        "chefhat.png":"Chef Hat",
        "crown.png":"Crown",
        "devilhorns.png":"Devil Horns",
        "greybandana.png":"Grey Bandana",
        "jesterhat.png":"Jester Hat",
        "pinkmohawk.png":"Pink Mohawk",
        "greenpuff.png":"Green Puff",
        "partyhat.png":"Party Hat",
        "piratehat.png":"Pirate Hat",
        "purplemohawk.png":"Purple Mohawk",
        "redbeanie.png":"Red Beanie",
        "redsweatband.png":"Red Sweatband",
        "bluesweatband.png":"Blue Sweatband",
        "tophat.png":"Top Hat",
        "vikinghelmet.png":"Viking Helmet",
        "wheatbeanie.png":"Wheat Beanie",
        "wizardhat.png":"Wizard Hat",
        "yellowpuff.png":"Yellow Puff",
        # Mouth
        "banana.png":"Banana",
        "bubblegum.png":"Bubble Gum",
        "bubblepipe.png":"Bubble Pipe",
        "buckteeth.png":"Buckteeth",
        "cigarette.png":"Cigarette",
        "pacifier.png":"Pacifier",
        "tongue.png":"Tongue",
        "vampireteeth.png":"Vampire Teeth",
        "vape.png":"Vape",
        # Nose
        "clownnose.png":"Clown Nose",
        "heart.png":"Cheek Heart",
        "nostrils.png":"Nostrils",
        "roseycheeks.png":"Rosey Cheeks"
    }
    newName = switch.get(attr, "Invalid Attribute")
    return newName


# get working directory path to save metadata jsons
dirPath = os.path.dirname(os.path.realpath(__file__))

conn = sqlite3.connect("PolyChimps.db")
db = conn.cursor()
dbAry = db.execute('SELECT * FROM Chimps')
chimpAttributes = getAttributes()

# iterate through every chimp
for x in chimpAttributes:
    counter = 0
    data = {}
    data['description'] = "Poly Chimp {} - Don't be an ape, be a CHIMPION and collect them all!".format(x[0])
    data['image'] = "https://gateway.pinata.cloud/ipfs/Qmf6XaX4dDCUXxwhv5pmTBthXNnmoqAvoP7z5t5RU2ktvT/PolyChimp%20%23{}.png".format(x[0].replace('#',''))
    data['name'] = "Poly Chimp {}".format(x[0])
    data['attributes'] = []
    # for each chimp, get attributes and send to json metadata file
    for y in x:
        if counter == 0:
            # skip; first value is NFTid
            pass
            counter += 1
        elif counter == 1:
            data['attributes'].append({
                'trait_type': 'Type',
                'value': '{}'.format(y),
            })
            counter += 1
        else:
            attribute = convertPNGname(y)
            data['attributes'].append({
                'trait_type': 'Attribute',
                'value': '{}'.format(attribute),
            })
            counter += 1

    # save JSON file at specified location
    with open(dirPath + '\\PCmetadata\\{}metadata.json'.format(x[0].replace('#','')), 'w') as outfile:
        json.dump(data, outfile)
