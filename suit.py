from common import readBytesList, readInt32, searchForBytePattern, writeBytes, writeInt32


class Suit:
    def __init__(self, hexlist):
        self.magic = ['CB', '53', 'C8', '36', 'EE', 'ED', 
                      '11', '50', '57', '52', '45', '44', 
                      '45', '32', '30', '34', 'D0', '8D',
                      '3A', '47', 'FF', 'FF', 'FF', 'FF']
        self.offset = searchForBytePattern(hexlist, self.magic)
        self.sizeAddress = self.offset + 0x18
        self.size = readInt32(hexlist, self.sizeAddress)
        self.unknownAddress = self.offset + 0x1C
        self.unknown = readBytesList(hexlist, self.unknownAddress, 0x08)
        self.suitLevelAddress = self.offset + 0x24
        self.suitLevel = readInt32(hexlist, self.suitLevelAddress)

    def writeData(self, hexlist, offset):
        writeBytes(self.magic ,hexlist, offset, 0x18, True)
        offset += 0x18
        self.sizeAddress = offset
        self.size = 0x04
        writeInt32(self.size , hexlist, offset)
        offset += 0x04
        self.unknownAddress = offset
        writeBytes(self.unknown, hexlist, self.unknownAddress, 0x08, True)
        offset += 0x08
        self.suitLevelAddress = offset
        writeInt32(self.suitLevel, hexlist, offset)
        offset += 0x04
        return offset