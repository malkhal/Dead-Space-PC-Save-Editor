from common import readBytesList, readByteslr, readInt32, searchForBytePattern, writeBytes, writeInt32
from dictionary import keyitemIdToNameDictionary, keyitemNameToIdDictionary

class Keyitem:
    def __init__(self, hexlist):
        self.magic = ['00', '00', '00', '00', '00', '00',
                      '00', '00', '00', '00', '00', '00',
                      '00', '00', '00', '00', '57', '69',
                      'A5', 'D6', 'FF', 'FF', 'FF', 'FF']
        self.offset = searchForBytePattern(hexlist, self.magic)
        self.sizeAddress = self.offset + 0x18
        self.size = readInt32(hexlist, self.sizeAddress)
        self.trueSize = int((self.size - 4) / 0x1C)
        self.unknown0Address = self.offset + 0x1C
        self.unknown0 = readBytesList(hexlist, self.unknown0Address, 0x08)
        self.items = []
        for x in range(0, self.trueSize):
            itemOffset = self.offset + 0x24 + (x * 0x1C)
            #print(readByteslr(hexlist, itemOffset + 0x04, 0x10))
            try:
                self.items.append({
                                   "unknown0":readInt32(hexlist, itemOffset),
                                   "name":keyitemIdToNameDictionary[readByteslr(hexlist, itemOffset + 0x04, 0x10)],
                                   "id":readByteslr(hexlist, itemOffset + 0x04, 0x10),
                                   "unknown1":readInt32(hexlist, itemOffset + 0x14), 
                                   "quantity":readInt32(hexlist, itemOffset + 0x18)})
                #print(keyitemIdToNameDictionary[readByteslr(hexlist, itemOffset + 0x04, 0x10)])
            except:
                keyitemIdToNameDictionary[readByteslr(hexlist, itemOffset, 0x10)] = readByteslr(hexlist, itemOffset, 0x10)
                keyitemNameToIdDictionary[readByteslr(hexlist, itemOffset, 0x10)] = readByteslr(hexlist, itemOffset, 0x10)
                #print(readByteslr(hexlist, itemOffset + 0x04, 0x10))
                self.items.append({
                                   "unknown0":readInt32(hexlist, itemOffset),
                                   "name":keyitemIdToNameDictionary[readByteslr(hexlist, itemOffset + 0x04, 0x10)],
                                   "id":readByteslr(hexlist, itemOffset + 0x04, 0x10),
                                   "unknown1":readInt32(hexlist, itemOffset + 0x14), 
                                   "quantity":readInt32(hexlist, itemOffset + 0x18)})
        self.unknown1Address = self.offset + self.size + 0x20
        self.unknown1 = readInt32(hexlist, self.unknown1Address)

    def writeData(self, hexlist, offset):
        writeBytes(self.magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.sizeAddress = offset
        self.size = (len(self.items) * 0x1C) + 0x04
        self.trueSize = len(self.items)
        writeInt32(self.size , hexlist, offset)
        offset += 0x04
        self.unknown0Address = offset
        writeBytes(self.unknown0, hexlist, self.unknown0Address, 0x08, True)
        offset += 0x08
        for i in self.items:
            writeInt32(i["unknown0"] , hexlist, offset)
            offset += 4
            itemID = list(map(''.join, zip(*[iter(i["id"].upper())]*2)))
            writeBytes(itemID ,hexlist, offset, 0x10 , True)
            offset += 0x10
            writeInt32(i["unknown1"] , hexlist, offset)
            offset += 4
            writeInt32(i["quantity"] , hexlist, offset)
            offset += 4
        self.unknown1Address = offset
        writeInt32(self.unknown1, hexlist, self.unknown1Address)
        offset += 0x04
        return offset
