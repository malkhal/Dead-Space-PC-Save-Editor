import struct
from dictionary import itemIdToNameDictionary

def readInt32(hexlist, offset):
    return int(readBytesStr(hexlist ,offset ,0x04), 16)

def readFloat32(hexlist,offset):
    return struct.unpack('f', struct.pack('I', readInt32(hexlist, offset)))[0]

def readBytesStr(hexlist, offset, length):
    revalue = ""
    for x in range(length-1, -1, -1):
        revalue = revalue + (hexlist[x+offset])
    return revalue
    
def readBytesList(hexlist, offset, length):
    revalue = hexlist[offset:offset + length]
    return revalue

def readByteslr(hexlist, offset, length):
    revalue = ""
    for x in range(length):
        revalue = revalue + (hexlist[x+offset])
    return revalue

def readWCharASCIIString(hexlist, offset):
    x = 0
    revalue = ""
    while (hexlist[x+offset] != "00"):
        revalue = revalue + (hexlist[x+offset])
        x += 2
    try:
        revalue = bytes.fromhex(revalue).decode('utf-8', 'ignore')
    except:
        pass
    return revalue

def writeInt32(value, hexlist, offset):
    b = list(struct.pack('<I',value))
    writeBytes(b,  hexlist , offset ,0x04)

def writeInt64(value, hexlist, offset):
    b = list(struct.pack('<L',value))
    writeBytes(b,  hexlist , offset ,0x08)

def writeFloat(value, hexlist, offset):
    b = list(struct.pack('<f',value))
    writeBytes(b,  hexlist , offset ,0x04)

def writeBytes(b, hexlist, offset, length, formatted = False):
    if formatted:
        for i in range(length):
            hexlist[offset+i] = b[i]
    else:
        for i in range(length):
            hexlist[offset+i] = format(b[i],'02X')
    

def searchForBytePattern(hexlist, pattern):
    for i in range(len(hexlist)):
        if hexlist[i] == pattern[0] and hexlist[i:i+len(pattern)] == pattern:
            return i
    return -1

def processItems(hexlist, offset, size):
    items = []
    for x in range(0, size):
            itemOffset = offset + 0x1C + (x * 0x1C)
            print(readByteslr(hexlist,itemOffset + 0x04, 0x10))
            try:
                items.append({"unkown":readInt32(hexlist, itemOffset), "name":itemIdToNameDictionary[readByteslr(hexlist,itemOffset + 0x04, 0x10)], "known1":readInt32(hexlist, itemOffset + 0x14), "quantity":readInt32(hexlist, itemOffset + 0x18)})
                print(itemIdToNameDictionary[readByteslr(hexlist,itemOffset + 0x04, 0x10)])
            except:
                itemIdToNameDictionary[readByteslr(hexlist,itemOffset + 0x04, 0x10)] = readByteslr(hexlist, itemOffset + 0x04, 0x10)
                print(readByteslr(hexlist,itemOffset + 0x04, 0x10))
                items.append({"unkown":readInt32(hexlist, itemOffset), "name":itemIdToNameDictionary[readByteslr(hexlist,itemOffset + 0x04, 0x10)], "known1":readInt32(hexlist, itemOffset + 0x14), "quantity":readInt32(hexlist, itemOffset + 0x18)})
    return items