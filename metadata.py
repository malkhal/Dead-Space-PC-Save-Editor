from common import *
import re

class MetaData:
    def __init__(self, hexlist):
        meta = readWCharASCIIString(hexlist, 0x2034)
        match = re.match("^.* (?P<slot>\d{1,2}) \(.* (?P<hoursPlayed>\d{1,2}):(?P<minutesPlayed>\d{1,2}):(?P<secondsPlayed>\d{1,2}) .* (?P<difficulty>\d{1,2}) .* (?P<chapter>\d{1,2}) .* (?P<checkpoint>\d{1,2}) .* (?P<round>\d{1,2})\)$",meta)
        difficultyDic = {"0" : "Easy",
                         "1" : "Medium",
                         "2" : "Hard",
                         "3" : "Impossible"}
        self.slot          = match.group('slot')
        self.hoursPlayed   = match.group('hoursPlayed')
        self.minutesPlayed = match.group('minutesPlayed')
        self.secondsPlayed = match.group('secondsPlayed')
        self.difficulty    = difficultyDic[match.group('difficulty')]
        self.chapter       = match.group('chapter')
        self.checkpoint    = match.group('checkpoint')
        self.round         = match.group('round')