from typing import Pattern
from common import *
from dictionary import *

class Shop:
    def __init__(self, hexlist):
        self.magic = ['00', '00', '00', '00', '00', '00',
                      '00', '00', '00', '00', '00', '00',
                      '00', '00', '00', '00', '7C', '9D',
                      '55', 'B3', 'FF', 'FF', 'FF', 'FF']
        self.offset = searchForBytePattern(hexlist, self.magic)
        self.sizeAddress = self.offset + 0x18
        self.size = readInt32(hexlist, self.sizeAddress)
        self.trueSize = int((self.size - 4) / 0x14)
        self.unknown0Address = self.offset+0x1C
        self.unknown0 = readBytesList(hexlist, self.unknown0Address, 0x08)
        self.unknown1Address = self.offset+0x24
        self.unknown1 = readInt32(hexlist, self.unknown1Address)
        self.items = []
        
        for x in range(0, self.trueSize):
            itemOffset = self.offset + 0x28 + (x * 0x14)
            #print(readByteslr(hexlist, itemOffset, 0x10))
            try:
                self.items.append({"name":itemIdToNameDictionary[readByteslr(hexlist, itemOffset, 0x10)],
                                   "id":readByteslr(hexlist, itemOffset, 0x10), 
                                   "unknown":readInt32(hexlist, itemOffset + 0x10)})
                #print(itemIdToNameDictionary[readByteslr(hexlist, itemOffset, 0x10)])
            except:
                itemIdToNameDictionary[readByteslr(hexlist,itemOffset, 0x10)] = readByteslr(hexlist, itemOffset, 0x10)
                itemNameToIdDictionary[readByteslr(hexlist,itemOffset, 0x10)] = readByteslr(hexlist, itemOffset, 0x10)
                #print(readByteslr(hexlist, itemOffset, 0x10))
                self.items.append({"name":itemIdToNameDictionary[readByteslr(hexlist, itemOffset, 0x10)],
                                   "id":readByteslr(hexlist, itemOffset, 0x10), 
                                   "unknown":readInt32(hexlist, itemOffset + 0x10)})
    
    def writeData(self, hexlist, offset):
        writeBytes(self.magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.sizeAddress = offset
        self.size = len(self.items) * 0x14 + 0x04
        self.trueSize = len(self.items)
        writeInt32(self.size , hexlist, offset)
        offset += 0x04
        self.unknown0Address = offset
        writeBytes(self.unknown0 ,hexlist, offset, 0x08, True)
        offset += 0x08
        self.unknown1Address = offset
        writeInt32(self.unknown1 , hexlist, offset)
        offset += 0x04
        for i in self.items:
            itemID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(itemID ,hexlist, offset, 0x10, True)
            offset += 0x10
            writeInt32(i["unknown"] , hexlist, offset)
            offset += 4
        return offset


        
        