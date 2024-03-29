itemIdToNameDictionary = {
                  
                    #Weapon
                    "4FBCC83656DEEA075752454445323034" : "PLASMA CUTTER",
                    "49BCC836D03C165F5752454445323034" : "LINE GUN",
                    "4FBCC836E278906F5752454445323034" : "RIPPER",
                    "4FBCC836385FBB675752454445323034" : "PULSE RIFLE",
                    "40BCC8369AB6670C5752454445323034" : "FLAMETHROWER",
                    "3FBCC836C81556F55752454445323034" : "CONTACT BEAM",
                    "48BCC836BA7C47ED5752454445323034" : "FORCE GUN",

                    #Ammo
                    "368CC74B2213659D43454E544B4F5753" : "PLASMA ENERGY",
                    "EC8CC74BCF2CF0DF43454E544B4F5753" : "LINE RACKS",
                    "368CC74B7C75679D43454E544B4F5753" : "PULSE ROUNDS",
                    "2D69C83022F8BB6D4A4F484E534F4E32" : "FLAME FUEL",
                    "2D69C830DC01E1794A4F484E534F4E32" : "RIPPER BLADES",
                    "7773C830EA55BCE3504D454C4445534B" : "CONTACT ENERGY",
                    "907DC8303E0C57E7504D454C4445534B" : "FORCE ENERGY",

                    #Consumables
                    "368CC74BBA895B9D43454E544B4F5753" : "SMALL MED PACK",
                    "368CC74B14EC5D9D43454E544B4F5753" : "MEDIUM MED PACK",
                    "368CC74B6E4E609D43454E544B4F5753" : "LARGE MED PACK",
                    "7FC9C73550A3F3CC4D41544855533737" : "SMALL AIR CAN",
                    "07F0C74BEEFA3F7143454E544B4F5753" : "MEDIUM AIR CAN",
                    "EA06C84BF7D6D94043454E544B4F5753" : "STASIS PACK",
                    "44B4C7379DBF07864D41594E41524436" : "POWER NODE",

                    #Schematic
                    "0AC1C830C9AD8E6C4A4F484E534F4E32" : "FLAMETHROWER SCHEMATIC",
                    "0AC1C830C3E023A14A4F484E534F4E32" : "PULSE ROUNDS SCHEMATIC",
                    "0AC1C830A75A37184A4F484E534F4E32" : "LINE AMMO SCHEMATIC",
                    "0AC1C8300FC1FC894A4F484E534F4E32" : "FLAME FUEL SCHEMATIC",
                    "0BC1C8306D8697F14A4F484E534F4E32" : "RIPPER SCHEMATIC",
                    "0CC1C83024BCDE3F4A4F484E534F4E32" : "MEDIUM MED PACK SCHEMATIC",
                    "0CC1C8309395320A4A4F484E534F4E32" : "RIPPER BLADES SCHEMATIC",
                    "0CC1C8302AE2DFD94A4F484E534F4E32" : "LEVEL 3 RIG SCHEMATIC",
                    "0CC1C830D0140A654A4F484E534F4E32" : "CONTACT BEAM SCHEMATIC",
                    "0CC1C83015A5B8A24A4F484E534F4E32" : "FORCE GUN SCHEMATIC",
                    "0DC1C8309A4D6E764A4F484E534F4E32" : "FORCE ENERGY SCHEMATIC",
                    "0DC1C830B2D440994A4F484E534F4E32" : "CONTACT ENERGY SCHEMATIC",
                    "0DC1C8304ED4D5424A4F484E534F4E32" : "LEVEL 4 RIG SCHEMATIC",
                    "0DC1C830F33709BA4A4F484E534F4E32" : "MEDIUM AIR CAN SCHEMATIC",
                    "0DC1C8305CAADCE34A4F484E534F4E32" : "LARGE MED PACK SCHEMATIC",
                    "0DC1C830E9C18D504A4F484E534F4E32" : "LEVEL 5 RIG SCHEMATIC",
                    "DADAC834268B172A4A4F484E534F4E31" : "LEVEL 6 RIG SCHEMATIC",

                    #Misc
                    "27A7C83031AB8C8E4A4F484E534F4E32" : "GOLD SEMICONDUCTOR",
                    "23A7C830E25BB0CB4A4F484E534F4E32" : "RUBY SEMICONDUCTOR",
                    "25A7C8307AC8993B4A4F484E534F4E32" : "DIAMOND SEMICONDUCTOR",
                    "39EDC84B558D313E43454E544B4F5753" : "PENG",
                    
                    #Suits
                    "8758C8387D7B1B3B54524F53494E3136" : "LEVEL 2 SUIT",
                    "BE53C8362D74C73B5752454445323034" : "LEVEL 3 SUIT",
                    "C254C8389D297B785049545453323032" : "LEVEL 4 SUIT",
                    "7E7DC830CD766B9E4A4F484E534F4E32" : "LEVEL 5 SUIT",
                    "7B7DC83870C377A354524F53494E3136" : "LEVEL 6 SUIT"
                    

                 }
itemNameToIdDictionary = {item[1]: item[0] for item in itemIdToNameDictionary.items()}
keyitemIdToNameDictionary = {
                    "E9ABC84B2E863B6D43454E544B4F5753" : "MAINTENANCE BAY KEY",
                    "E7ABC84B45D129DD43454E544B4F5753" : "DATA BOARD",
                    "DF99C8339CCAC9C3504154454C303633" : "THERMITE",
                    "E199C833A8C20C1A504154454C303633" : "SHOCK PAD",
                    "4FA9C8367BC4883D504154454C313032" : "THERMITE BOMB",
                    "549FC83370B90ACC504154454C303633" : "CAPTAIN'S RIG",
                    "6067C833DC643EAC504154454C373332" : "CHEMICAL CAPSULE",
                    "6567C833825155BF504154454C373332" : "CHEMICAL CAPSULE W/DNA",
                    "7867C833A011A1C5504154454C373332" : "POISON CAPSULE (Chapter 5)",
                    "B2B6C830F81770D94A4F484E534F4E32" : "POISON CAPSULE (Chapter 6)",
                    "AB8AC8382CC6622F5049545453323032" : "MINING ACCESS KEY",
                    "AB8AC83812D43F035049545453323032" : "SOS BEACON",
                    "4991C8367DB1B2F05752454445323034" : "SINGULARTY CORE",
                    "E183C830D75D962C4A4F484E534F4E32" : "CREW KEY",
                    "E183C830851E30544A4F484E534F4E32" : "NAV CARD (1)",
                    "E183C83055736A484A4F484E534F4E32" : "NAV CARD (2)",
                    "E183C83080B43C5E4A4F484E534F4E32" : "NAV CARD (3)"
                  }
keyitemNameToIdDictionary = {item[1]: item[0] for item in keyitemIdToNameDictionary.items()}
dataBaseIdToNameDictionary = {
                    #CHTRA
                    "37A0C835BF6160A34D4154485553373700000000" : "MOVEMENT TRAINING",
                    "37A0C8359868929B4D4154485553373700000000" : "ACTION BUTTON TRAINING",
                    "37A0C8352CA810BF4D4154485553373700000000" : "OBJECTIVES TRAINING",
                    "37A0C8356C2C6BAF4D4154485553373700000000" : "WEAPONS TRAINING",
                    "09B7C84B74107A8743454E544B4F575300000000" : "HEALTH TRAINING",
                    "37A0C8350C4B9AB54D4154485553373700000000" : "MAP TRAINING",
                    "37A0C83504EBB7CC4D4154485553373700000000" : "DISMEMBERMENT TRAINING",
                    "37A0C83566EA50E24D4154485553373700000000" : "STASIS MODULE TRAINING",
                    "37A0C8358062F5DA4D4154485553373700000000" : "UPGRADE BENCH TRAINING",
                    "37A0C83528C0DAC54D4154485553373700000000" : "STORE TRAINING",
                    "36A0C835D6CA533F4D4154485553373700000000" : "KINESIS MODULE TRAINING",
                    "D1CCC839B96A379949474E4143494F3300000000" : "SCHEMATICS TRAINING",
                    "36A0C8359403A06A4D4154485553373700000000" : "KINESIS SYMBOL TRAINING",
                    "36A0C835A81C63564D4154485553373700000000" : "AIR TIMER TRAINING",
                    "36A0C83508197D614D4154485553373700000000" : "ZERO-G TRAINING",
                    "D1CCC839C617AA4949474E4143494F3300000000" : "SECONDARY FIRE TRAINING",
                    "D2CCC839238EA82249474E4143494F3300000000" : "WEAPON SELECT TRAINING",
                    # CH1
                    "88E8C84B3A7AED2C43454E544B4F575300000000" : "MESSAGE FROM NICOLE",
                    "917DC8304BF31A7F4A4F484E534F4E3200000000" : "REPAIR THE TRAM SYSTEM",
                    "147FC83094AE3ADF4A4F484E534F4E3200000000" : "REPLACED THE TRAM CAR",
                    "157FC830C438FB0E4A4F484E534F4E3200000000" : "FOUND THE DATA BOARD",
                    "147FC8309C394E8C4A4F484E534F4E3200000000" : "ACTIVATED THE TRAM",
                    "927DC83072ABC6C74A4F484E534F4E3200000000" : "GO TO MEDICAL",
                    "8180C830F0FEE36D4A4F484E534F4E3200000000" : "RUN!",
                    "AA41C84BBEE65F8E43454E544B4F575300000000" : "VENT WARNING",
                    "5D89C830D3451EC34A4F484E534F4E3200000000" : "DISMEMBERMENT",
                    "DDB6C84B8C1B17C343454E544B4F575300000000" : "STASIS DOOR",
                    "AA41C84B7634706143454E544B4F575300000000" : "TRAM STATUS",
                    "DEB6C84BB6AE002343454E544B4F575300000000" : "REPLACING THE TRAM",
                    "DDB6C84B5C9F378F43454E544B4F575300000000" : "FIND THE DATA BOARD",
                    "DEB6C84B088E504343454E544B4F575300000000" : "MAINTENANCE BAY UNLOCKED",
                    "A941C84BF07438BF43454E544B4F575300000000" : "SHOOT THE LIMBS",
                    "8C80C83020F5CAF54A4F484E534F4E3200000000" : "LOCKED DOOR",
                    "5E89C83094695D2D4A4F484E534F4E3200000000" : "ARRIVED ON BRIDGE",
                    "CE41C84B5A74BA5943454E544B4F575300000000" : "REPAIR INVOICE",
                    #CH2
                    "7B6FC8300EFC8BF04A4F484E534F4E3200000000" : "DESTROY THE BARRICADE",
                    "927DC830DB84925B4A4F484E534F4E3200000000" : "KYNE AND THE CAPTAIN",
                    "927DC830C51211DE4A4F484E534F4E3200000000" : "NICOLE'S REPORT",
                    "7A6FC8307647AC1C4A4F484E534F4E3200000000" : "ENGINE PROBLEMS",
                    "8180C830EE2AFC9D4A4F484E534F4E3200000000" : "MERCER'S JOURNAL",
                    "8180C830402E17E84A4F484E534F4E3200000000" : "FOUND THE THERMITE",
                    "8180C8300E3D46FE4A4F484E534F4E3200000000" : "MERCER AND KYNE",
                    "8280C830E830D8384A4F484E534F4E3200000000" : "FOUND THE SHOCK PAD",
                    "8280C83084E2DFCD4A4F484E534F4E3200000000" : "BARRICADE DESTROYED",
                    "8280C830F0F9C0E54A4F484E534F4E3200000000" : "WE'LL FIND HER",
                    "8280C830063D87FB4A4F484E534F4E3200000000" : "EILEEN",
                    "8380C830F026971C4A4F484E534F4E3200000000" : "COLONIST PROBLEMS",
                    "8380C8300603BD724A4F484E534F4E3200000000" : "CODES RECEIVED",
                    "5D89C83022F848604A4F484E534F4E3200000000" : "SHIP GRAVITY ",
                    "7A8BC830A8ABEAE54A4F484E534F4E3200000000" : "MARKER OVERVIEW",
                    "7B8BC830DEAF04714A4F484E534F4E3200000000" : "INTERESTING RESULTS",
                    "7B8BC83073E2BF854A4F484E534F4E3200000000" : "NEWBORNS",
                    "7C8BC8302334542B4A4F484E534F4E3200000000" : "MORE TIME",
                    "7C8BC830E21200494A4F484E534F4E3200000000" : "AUTOPSY REPORT",
                    #CH3
                    "7C6FC830F42A69554A4F484E534F4E3200000000" : "REPAIR THE SHIP'S ORBIT",
                    "7C6FC83053D4AF6E4A4F484E534F4E3200000000" : "KENDRA IS ALIVE",
                    "7C6FC830D4D606924A4F484E534F4E3200000000" : "ENGINE FIRED",
                    "A20FC835492ED6AA4D4154485553373700000000" : "TEMPLE REPORT 1",
                    "AC0FC835B9A4FEDC4D4154485553373700000000" : "TEMPLE REPORT 2",
                    "AD0FC8359B6D86E44D4154485553373700000000" : "ENGINE REFUELED",
                    "AE0FC83595BB79A64D4154485553373700000000" : "TEMPLE REPORT 3",
                    "AE0FC835D7089AF54D4154485553373700000000" : "TEMPLE REPORT 4",
                    "FD73C849FAEABA9D454E544B4F57534B00000000" : "CENTRIFUGE ACTIVATED",
                    "AF0FC835279B6E3E4D4154485553373700000000" : "TEMPLE REPORT 5",
                    "FF73C84916B7FA8C454E544B4F57534B00000000" : "STRANGE TRANSMISSION",
                    "1C10C835F36F3D0D4D4154485553373700000000" : "CHAOS",
                    "2010C83521114A254D4154485553373700000000" : "CORRUPTION (Chapter 3)",
                    #CH4
                    "7C6FC8303601A8DE4A4F484E534F4E3200000000" : "THE MARKER",
                    "907DC8300DDE383E4A4F484E534F4E3200000000" : "CAPTAIN'S DEMISE",
                    "7C6FC83062D9B4FE4A4F484E534F4E3200000000" : "ATMOSPHERE CONTAMINATED",
                    "8480C83046F36C524A4F484E534F4E3200000000" : "INITIAL ATTACK",
                    "8480C83064F962704A4F484E534F4E3200000000" : "TEMPLE ON THE BRIDGE",
                    "8480C830646A2B914A4F484E534F4E3200000000" : "ASTROGATION MODULE PLACED",
                    "8480C8304A4F28B24A4F484E534F4E3200000000" : "CONTROL MODULE PLACED",
                    "8480C830AA2433C64A4F484E534F4E3200000000" : "REPORT FROM KENDRA",
                    "8480C83034213DE34A4F484E534F4E3200000000" : "SYSTEMS MODULE PLACED",
                    "8480C8309A6B90FE4A4F484E534F4E3200000000" : "ASTEROID IMPACT",
                    "6089C830E0AD1E4C4A4F484E534F4E3200000000" : "BRUTE COMBAT",
                    "8B80C830791729B04A4F484E534F4E3200000000" : "AIM THE ADS CANNON",
                    "8C80C8309CA3AB0C4A4F484E534F4E3200000000" : "REVERSED GRAVITY",
                    "8D80C830A66E63194A4F484E534F4E3200000000" : "AVOID THE ASTEROIDS",
                    "8D80C8305C94AC324A4F484E534F4E3200000000" : "HURRY UP!",
                    "DABAC85ACD866603524F44524947554500000000" : "ALMOST FIXED",
                    "157FC83026BDDE444A4F484E534F4E3200000000" : "ONE MORE MINUTE",
                    "167FC8308F72ED214A4F484E534F4E3200000000" : "ADS ONLINE",
                    "7C8BC8300F95BFB24A4F484E534F4E3200000000" : "REPORT OF INFECTION",
                    "7C8BC830D56AEBDE4A4F484E534F4E3200000000" : "LIST OF DEAD",
                    #CH5
                    "7D6FC830CE6B44484A4F484E534F4E3200000000" : "GO TO CHEMISTRY",
                    "7D6FC83024280C704A4F484E534F4E3200000000" : "INTERRUPTED",
                    "167FC8303BE40A644A4F484E534F4E3200000000" : "GOT THE POISON",
                    "8680C8304438EE0C4A4F484E534F4E3200000000" : "SOMEONE ELSE",
                    "8680C8305C5C91244A4F484E534F4E3200000000" : "DOOR OPENED",
                    "8680C830641A543E4A4F484E534F4E3200000000" : "MERCER'S EXPERIMENT 1",
                    "8680C8309C2BE4554A4F484E534F4E3200000000" : "CREATING THE POISON",
                    "8680C83054C435834A4F484E534F4E3200000000" : "MERCER'S EXPERIMENT 2",
                    "8680C830EFA9B2AA4A4F484E534F4E3200000000" : "HAMMOND ON HYDROPONICS",
                    "8680C8301CEF3FC54A4F484E534F4E3200000000" : "FINISH THE POISON",
                    "8680C830C05BF3F74A4F484E534F4E3200000000" : "POISON COMPLETE",
                    "8780C8308DA1801A4A4F484E534F4E3200000000" : "INDESTRUCTIBLE",
                    "9FB7C830475CD73B4A4F484E534F4E3200000000" : "SECRET LAB REVEALED",
                    "45C1C8366D230F78504154454C31303200000000" : "DNA NEEDED",
                    "99C2C83512FACB204D4154485553373700000000" : "THE LEVIATHAN",
                    #CH6
                    "167FC8308CFAA77E4A4F484E534F4E3200000000" : "HAMMOND'S ALIVE",
                    "167FC8302A5678B44A4F484E534F4E3200000000" : "VICTORY AGAINST THE LEVIATHAN",
                    "A258C845698847635357454152494E4700000000" : "CROSS REPORT 1",
                    "8780C83012CD71584A4F484E534F4E3200000000" : "CROSS REPORT 2",
                    "8780C8300D83BE954A4F484E534F4E3200000000" : "CROSS REPORT 3",
                    "8780C83036ADDCB64A4F484E534F4E3200000000" : "TEMPLE'S SEARCH",
                    "8780C8303443DBDD4A4F484E534F4E3200000000" : "GETTING TO THE LEVIATHAN",
                    "8780C830991EDAF14A4F484E534F4E3200000000" : "A MESSAGE",
                    "8880C8300FF7870D4A4F484E534F4E3200000000" : "CROSS REPORT 4",
                    "B96DC830285A9A6D4A4F484E534F4E3200000000" : "PODS DESTROYED",
                    "10DBC8491E9D7F89454E544B4F57534B00000000" : "KILL THE LEVIATHAN",
                    "5CE0C849A6F025EC454E544B4F57534B00000000" : "TRUST",
                    "A158C845D33B52495357454152494E4700000000" : "CORRUPTION (Chapter 6)",
                    #CH7
                    "7D6FC8309A3F5CC94A4F484E534F4E3200000000" : "DISTRESS CALL",
                    "7D6FC830BA7063E84A4F484E534F4E3200000000" : "ASTEROID LAUNCHED",
                    "83BBC8307F5016BD504954545331303200000000" : "ELEVATOR PROBLEM",
                    "614DC838D5679D70504954545332303200000000" : "TEMPLE AND ELIZABETH",
                    "FCB5C830B72A7F99504954545331303200000000" : "CLEAR THE BOULDERS",
                    "664DC8382D90C1D4504954545332303200000000" : "KEY FOUND",
                    "2144C8382739CCFF504954545332303200000000" : "KYNE'S HOSTAGE",
                    "674DC838EDFE6D02504954545332303200000000" : "BEACON RECOVERED",
                    "84BBC83080737F03504954545331303200000000" : "ELEVATOR FIXED",
                    "644DC838D7B3EF1E504954545332303200000000" : "SUPERVISOR'S CHOICE",
                    "FCB5C830A9E1F1A9504954545331303200000000" : "ATTACH THE BEACON",
                    "664DC838D3259126504954545332303200000000" : "PROCESSING ROOM PROBLEM",
                    "664DC83833F0A68D504954545332303200000000" : "MINING TIMELINE",
                    #CH8
                    "7E6FC83082F326154A4F484E534F4E3200000000" : "GO TO COMMUNICATIONS",
                    "7E6FC830D85F3B384A4F484E534F4E3200000000" : "FIRST CONTACT",
                    "7E6FC8307E4AE56E4A4F484E534F4E3200000000" : "IMPACT",
                    "7E6FC830C7AEB9814A4F484E534F4E3200000000" : "HAMMOND'S RETURN",
                    "8880C83089F04D794A4F484E534F4E3200000000" : "EAVESDROPPER",
                    "8880C8305653AB964A4F484E534F4E3200000000" : "ILLEGAL MINING",
                    "8880C8301C06D3A74A4F484E534F4E3200000000" : "MAIN ARRAY PROBLEM",
                    "8880C830AF2C1FD34A4F484E534F4E3200000000" : "ARRAY FIXED",
                    "8980C830B76CFC0C4A4F484E534F4E3200000000" : "BIG PROBLEMS",
                    #CH9
                    "7E6FC83040C824D34A4F484E534F4E3200000000" : "THE VALOR",
                    "167FC83043B7A8F14A4F484E534F4E3200000000" : "DR. KYNE",
                    "7E6FC8307C921FBC4A4F484E534F4E3200000000" : "SINGULARITY CORE FOUND",
                    "8C80C83010272B774A4F484E534F4E3200000000" : "RADIATION HAZARD",
                    "BA6DC830069B25F74A4F484E534F4E3200000000" : "FIND THE SINGULARITY CORE",
                    "6289C830FCFD29F64A4F484E534F4E3200000000" : "INFECTED SOLDIERS",
                    "6289C8300AF8E5AE4A4F484E534F4E3200000000" : "HAMMOND'S ASSISTANCE",
                    "8980C830916C68D64A4F484E534F4E3200000000" : "EMERGENCY",
                    "6289C830A23CCA724A4F484E534F4E3200000000" : "HAMMOND'S DEATH",
                    "7D8BC830E38A0B294A4F484E534F4E3200000000" : "ORDERS",
                    #CH10
                    "7F6FC830A1CED1544A4F484E534F4E3200000000" : "FIND THE NAV CARDS",
                    "7F6FC8302E8299A44A4F484E534F4E3200000000" : "KYNE'S GAMBIT",
                    "55C1C8301110B2EE4A4F484E534F4E3200000000" : "HIVE MIND GLIMPSE",
                    "8693C83087C887134A4F484E534F4E3200000000" : "MERCER'S LAST SERMON",
                    "8A80C830964D9DAF4A4F484E534F4E3200000000" : "LOCKED EXECUTIVE DOOR",
                    "8C80C8308E219C434A4F484E534F4E3200000000" : "LIFE SUPPORT DOWN",
                    "8A80C830FF294E574A4F484E534F4E3200000000" : "THE HUNTER RETURNS",
                    "6389C83098CD39324A4F484E534F4E3200000000" : "SOB OVERRIDE",
                    "8C80C8306FCA082D4A4F484E534F4E3200000000" : "LOCK BYPASSED",
                    "7F6FC830999D316C4A4F484E534F4E3200000000" : "EXECUTIVE AREA UNLOCKED",
                    "8A80C830347EB3C94A4F484E534F4E3200000000" : "KENDRA'S WARNING",
                    "015EC830BDC5EFD14A4F484E534F4E3200000000" : "CAPTAIN'S REPORT",
                    "8A80C830F4CD0E6E4A4F484E534F4E3200000000" : "ON MY WAY",
                    "7F6FC8309AF8D8834A4F484E534F4E3200000000" : "MEET ON THE FLIGHT DECK",
                    "8B80C830EA94D2144A4F484E534F4E3200000000" : "NEW ALLY?",
                    "FE5DC830A6F6A4EE4A4F484E534F4E3200000000" : "UNITOLOGY ARTICLE",
                    "FF5DC830CBCE65E24A4F484E534F4E3200000000" : "Z-BALL RULES",
                    "005EC8307027CE344A4F484E534F4E3200000000" : "WHITE'S LIST",
                    #CH11
                    "7F6FC830C0FCC7D74A4F484E534F4E3200000000" : "FIND THE MARKER",
                    "7F6FC8305F027EEC4A4F484E534F4E3200000000" : "COME ONBOARD",
                    "4A77C849B6ECE641454E544B4F57534B00000000" : "BETRAYAL",
                    "937DC830894EBA114A4F484E534F4E3200000000" : "NICOLE'S ALIVE",
                    "8B80C83057CE7D334A4F484E534F4E3200000000" : "MARKER TRANSFERRED",
                    "8B80C830453E6B834A4F484E534F4E3200000000" : "TERRIBLE MISTAKE",
                    "6389C8301A4F71B24A4F484E534F4E3200000000" : "RENDEZVOUS",
                    "6389C830D8BC10E94A4F484E534F4E3200000000" : "LANDING THE SHUTTLE",
                    "8C80C8308CD4FAA74A4F484E534F4E3200000000" : "LOAD THE MARKER",
                    "8C80C83093648CC04A4F484E534F4E3200000000" : "RESTORE GRAVITY",
                    #CH12
                    "FD77C838D0D8CB08504954545332303200000000" : "NICOLE'S FAREWELL",
                    "FD77C838675CFD0E504954545332303200000000" : "COLONY CHAOS",
                    "6885C8388040D504504954545332303200000000" : "THE PEDESTAL",
                    "AEA0C838EF699B3B504954545332303200000000" : "RESTORE POWER",
                    "DAECC830E53FBB6D504954545331303200000000" : "UNITOLOGY EXPOSED",
                    "DAECC83085596FA8504954545331303200000000" : "THE USG ISHIMURA",
                    "DAECC830C54C2AB0504954545331303200000000" : "BACKGROUND REQUEST",
                    "DAECC830452D8EB3504954545331303200000000" : "PLANETARY MINING",
                    "DAECC830654C90B6504954545331303200000000" : "RECOMBINATION STUDY",
                    "DAECC830E5D79FBA504954545331303200000000" : "THE RED MARKER"
                    }
dataBaseNameToIdDictionary = {item[1]: item[0] for item in dataBaseIdToNameDictionary.items()}