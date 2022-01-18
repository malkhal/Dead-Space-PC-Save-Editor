import os

from common import readInt32
from hash import hashData


def writeSaveFile(srcFileName, hexlist, safe, inventory, shop, bench, keyitem, character, suit, database):
    
    output = ['00'] * 0x066CC8
    inputPos = 0
    headerSize = readInt32(hexlist, inputPos + 0x08)
    output[inputPos:inputPos + headerSize] = hexlist[inputPos:inputPos + headerSize]

    inputPos += headerSize
    metaSize = readInt32(hexlist, inputPos + 0x08)
    output[inputPos: inputPos + metaSize] = hexlist[inputPos:inputPos + metaSize]
    
    
    inputPos += metaSize
    mc02size = readInt32(hexlist, inputPos + 0x04) - readInt32(hexlist, inputPos + 0x0C)
    output[inputPos:inputPos + mc02size] = hexlist[inputPos:inputPos + mc02size]
    
    
    inputPos += mc02size

    numOfSection = readInt32(hexlist, inputPos)
    output[inputPos:inputPos + 0x04] = hexlist[inputPos:inputPos + 0x04]
    inputPos += 4
    outputPos = inputPos
    for i in range(numOfSection):
        dataSubHeader = readInt32(hexlist, inputPos)
        output[outputPos:outputPos + 0x08] = hexlist[inputPos:inputPos + 0x08]
        inputPos += 8
        outputPos += 8
        if (dataSubHeader == 4033131282):
            settingsSize = readInt32(hexlist, inputPos)
            output[outputPos:outputPos + 0x04] = hexlist[inputPos:inputPos + 0x04]
            inputPos += 4
            outputPos += 4
            output[outputPos:outputPos + settingsSize] = hexlist[inputPos:inputPos + settingsSize]
            inputPos += settingsSize
            outputPos += settingsSize
        
        elif (dataSubHeader == 2606639125):
            output[outputPos:outputPos + 0x08] = hexlist[inputPos:inputPos + 0x08]
            inputPos += 8
            outputPos += 8
            inputPos += 0x18
            inputPos += readInt32(hexlist, inputPos) + 0x0C
            outputPos = safe.writeData(output, outputPos)
            inputPos += 0x18
            inputPos += readInt32(hexlist, inputPos)  + 0x0C
            outputPos = inventory.writeData(output, outputPos)
            inputPos += 0x18
            inputPos += readInt32(hexlist, inputPos) + 0x0C
            outputPos = shop.writeData(output, outputPos)
            inputPos += 0x18
            inputPos += readInt32(hexlist, inputPos) + 0x0C
            outputPos = bench.writeData(output, outputPos)
            inputPos += 0x18
            inputPos += readInt32(hexlist, inputPos) + 0x0C
            outputPos = keyitem.writeData(output, outputPos)
            inputPos += 0x18
            inputPos += readInt32(hexlist, inputPos) + 0x0C
            outputPos = character.writeData(output, outputPos)
            inputPos += 0x18
            inputPos += readInt32(hexlist, inputPos) + 0x0C
            outputPos = suit.writeData(output, outputPos)
            for i in range(13):
                inputPos += 0x18
                unknownDataSize = readInt32(hexlist, inputPos) + 0x0C
                inputPos += unknownDataSize
            outputPos = database.writeData(output, outputPos)

        else:
            unknownDataSize = readInt32(hexlist, inputPos)
            output[outputPos:outputPos + 0x04] = hexlist[inputPos:inputPos + 0x04]
            inputPos += 4
            outputPos += 4
            output[outputPos:outputPos + unknownDataSize] = hexlist[inputPos:inputPos + unknownDataSize]
            inputPos += unknownDataSize
            outputPos += unknownDataSize
    
    hashData(output)
    x = 0
    while(os.path.exists("{}.bak{}".format(srcFileName, x))): x += 1
    os.rename(srcFileName, "{}.bak{}".format(srcFileName, x))
    f = open(srcFileName, "wb")
    for i in range(len(output)):
        f.write(bytes.fromhex(output[i]))
        
    f.close()

    return "{}.bak{}".format(srcFileName, x)