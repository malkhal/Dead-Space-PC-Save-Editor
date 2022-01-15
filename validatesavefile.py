from common import *

def validateSaveFile(hexlist):

    if(readBytesStr(hexlist, 0, 0x04) != '484D4752'):
        return False, "error @ 0x0 should be '0x484D4752', found '0x{}'".format(readBytesStr(hexlist ,0x0, 0x04))
    if(readWCharASCIIString(hexlist ,0x28) != 'Dead Space'):
        return False, "error @ 0x28 should be 'Dead Space', found '{}'".format(readWCharASCIIString(hexlist ,0x28))
        
    if(readBytesStr(hexlist ,0x2028, 0x04) != '44534D4E'):
        return False, "error @ 0x2028 should be '0x44534D4E', found '0x{}'".format(readBytesStr(hexlist ,0x2028, 0x04))
        
    if(readBytesStr(hexlist ,0x202C, 0x04) != '00000001'):
        return False, "error @ 0x202C should be '0x00000001', found '0x{}'".format(readBytesStr(hexlist ,0x202C, 0x04))
        
    if(readBytesStr(hexlist ,0x2030, 0x04) != '0000080C'):
        return False, "error @ 0x2030 should be '0x0000080C', found '0x{}'".format(readBytesStr(hexlist ,0x2030, 0x04))
    mc02 = MC02Header(hexlist)
    if(mc02.magic != '4D433032'):
        return False, "error @ 0x2834 should be '0x4D433032', found '0x{}'".format(mc02.magic)
        
    if(mc02.totalLength != mc02.chunk0Length + mc02.chunk1Length + 0x1C):
        return False, "Size mismatch"
    return True, "Valid"
    
    
class MC02Header:
        def __init__(self, hexlist):
            self.magic = readBytesStr(hexlist ,0x2834, 0x04)
            self.totalLength = readInt32(hexlist ,0x2838)
            self.chunk0Length = readInt32(hexlist ,0x283C)
            self.chunk1Length = readInt32(hexlist ,0x2840)
            self.checksum0 = readInt32(hexlist ,0x2844)
            self.checksum1 = readInt32(hexlist ,0x2848)
            self.checksum2 = readInt32(hexlist ,0x284C)  
