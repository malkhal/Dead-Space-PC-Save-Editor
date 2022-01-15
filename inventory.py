from typing import Pattern
from common import *
from dictionary import *

class Inventory:
    def __init__(self, hexlist):
        self.magic = ['00', '00', '00', '00', '00', '00',
                      '00', '00', '00', '00', '00', '00',
                      '00', '00', '00', '00', 'DE', '70', 
                      'A2', 'A3', 'FF', 'FF', 'FF', 'FF']
        self.offset = searchForBytePattern(hexlist, self.magic)
        self.sizeAddress = self.offset + 0x18
        self.size = readInt32(hexlist, self.sizeAddress)
        self.trueSize = int((self.size - 4) / 0x1C)
        self.unknownAddress = self.offset + 0x1C
        self.unknown = readBytesList(hexlist, self.unknownAddress, 0x08)
        self.creditAddress = self.offset + 0x24
        self.credit = readInt32(hexlist,self.creditAddress)
        self.items = []
        for x in range(0, self.trueSize):
            itemOffset = self.offset + 0x28 + (x * 0x1C)
            #print(readByteslr(hexlist, itemOffset, 0x10))
            try:
                self.items.append({"name":itemIdToNameDictionary[readByteslr(hexlist, itemOffset, 0x10)],
                                   "id":readByteslr(hexlist, itemOffset, 0x10),
                                   "slot":readInt32(hexlist, itemOffset + 0x10), 
                                   "quantity":readInt32(hexlist, itemOffset + 0x14), 
                                   "unknown0":readInt32(hexlist, itemOffset + 0x18)})
                #print(itemIdToNameDictionary[readByteslr(hexlist, itemOffset, 0x10)])
            except:
                itemIdToNameDictionary[readByteslr(hexlist, itemOffset, 0x10)] = readByteslr(hexlist, itemOffset, 0x10)
                itemNameToIdDictionary[readByteslr(hexlist, itemOffset, 0x10)] = readByteslr(hexlist, itemOffset, 0x10)
                #print(readByteslr(hexlist, itemOffset, 0x10))
                self.items.append({"name":itemIdToNameDictionary[readByteslr(hexlist, itemOffset, 0x10)],
                                   "id":readByteslr(hexlist, itemOffset, 0x10),
                                   "slot":readInt32(hexlist, itemOffset + 0x10), 
                                   "quantity":readInt32(hexlist, itemOffset + 0x14), 
                                   "unknown0":readInt32(hexlist, itemOffset + 0x18)})
    
    def writeData(self, hexlist, offset):
        self.offset = offset
        writeBytes(self.magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.sizeAddress = offset
        self.size = len(self.items) * 0x1C + 0x04
        self.trueSize = len(self.items)
        writeInt32(self.size , hexlist, offset)
        offset += 4
        self.unknownAddress = offset
        writeBytes(self.unknown, hexlist, offset, 0x08, True)
        offset += 0x08
        self.creditAddress = offset
        writeInt32(self.credit, hexlist, offset)
        offset += 0x04
        for i in self.items:
            itemID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(itemID ,hexlist, offset, 0x10, True)
            offset += 0x10
            writeInt32(i["slot"] , hexlist, offset)
            offset += 4
            writeInt32(i["quantity"] , hexlist, offset)
            offset += 4
            writeInt32(i["unknown0"] , hexlist, offset)
            offset += 4
        return offset

def isWeapon(id):
    weaponList = ["4FBCC83656DEEA075752454445323034",
                  "49BCC836D03C165F5752454445323034",
                  "4FBCC836E278906F5752454445323034",
                  "4FBCC836385FBB675752454445323034",
                  "40BCC8369AB6670C5752454445323034",
                  "3FBCC836C81556F55752454445323034",
                  "48BCC836BA7C47ED5752454445323034"]
    return id in weaponList
        
    