from common import *




class Character:
    def __init__(self, hexlist):
        self.magic = ['00', '00', '00', '00', '00', '00',
                   '00', '00', '00', '00', '00', '00',
                   '00', '00', '00', '00', '3A', 'C1', 
                   '80', '7B', 'FF', 'FF', 'FF', 'FF']
        self.offset = searchForBytePattern(hexlist,self.magic)
        self.sizeAddress = self.offset + 0x18
        self.size = readInt32(hexlist, self.sizeAddress)
        self.unknown0Address = self.offset + 0x1C
        self.unknown0 = readBytesList(hexlist, self.unknown0Address, 0x08)
        self.healthAddress = self.offset + 0x24
        self.health = readFloat32(hexlist, self.healthAddress)
        self.airAddress = self.offset + 0x28
        self.air = readFloat32(hexlist, self.airAddress)
        self.stasisAddress = self.offset + 0x2C
        self.stasis = readFloat32(hexlist, self.stasisAddress)
        self.nodeAddress = self.offset + 0x30
        self.nodes = readInt32(hexlist, self.nodeAddress)
        self.unknown1Address = self.offset + 0x34
        self.unknown1 = readBytesList(hexlist, self.unknown1Address, 0x04)

    def writeData(self, hexlist, offset):
        writeBytes(self.magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.sizeAddress = offset
        writeInt32(self.size , hexlist, offset)
        offset += 0x04
        self.unknown0Address = offset
        writeBytes(self.unknown0 , hexlist, offset, 0x08, True)
        offset += 0x08
        self.healthAddress = offset
        writeFloat(self.health, hexlist, self.healthAddress)
        offset += 0x04
        self.airAddress = offset
        writeFloat(self.air, hexlist, self.airAddress)
        offset += 0x04
        self.stasisAddress = offset
        writeFloat(self.stasis, hexlist, self.stasisAddress)
        offset += 0x04
        self.nodeAddress = offset
        writeInt32(self.nodes, hexlist, self.nodeAddress)
        offset += 0x04
        self.unknown1Address = offset
        writeBytes(self.unknown1 , hexlist, offset, 0x04, True)
        offset += 0x04
        return offset
