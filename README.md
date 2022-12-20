# python-project
8000
{\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fnil\fcharset0 Courier New;}}
{\colortbl ;\red0\green0\blue0;}
\viewkind4\uc1\pard\li195\cf1\f0\fs20 LXI H E000h
\par MVI D 11h
\par MOV B M
\par MOV C M
\par 
\par LOOP: MOV A M
\par DCR D
\par JZ VAYO
\par INX H
\par 
\par CMP B
\par JNZ ZERO
\par JMP HEYO
\par ZERO: JNC CARRY
\par JMP HEYO
\par CARRY: MOV B A
\par JMP HEYO
\par 
\par HEYO: CMP C
\par JC CARY
\par JMP LOOP
\par 
\par CARY: MOV C A
\par JMP LOOP
\par 
\par VAYO: MOV A B
\par MOV D H
\par MOV E L
\par STAX D
\par INX D
\par MOV A C
\par STAX D
\par HLT
\par 
\par 
\par 
\par \cf0 
\par }
<End Codes>
26
1| E000| 78
2| E001| 59
3| E002| 80
4| E003| 40
5| E004| 20
6| E005| 07
7| E006| 60
8| E007| 30
9| E008| 09
10| E009| 40
11| E00A| 99
12| E00B| 12
13| E00C| 30
14| E00D| 50
15| E00E| 50
16| E00F| 50
17| E010| 99
18| E011| 07
19| 0000| 00
20| 0000| 00
21| 0000| 00
22| 0000| 00
<End UserData>
564
1| 8000| 21
2| 8001| 00
3| 8002| E0
4| 8003| 16
5| 8004| 11
6| 8005| 46
7| 8006| 4E
8| 8007| 7E
9| 8008| 15
10| 8009| CA
11| 800A| 29
12| 800B| 80
13| 800C| 23
14| 800D| B8
15| 800E| C2
16| 800F| 14
17| 8010| 80
18| 8011| C3
19| 8012| 1E
20| 8013| 80
21| 8014| D2
22| 8015| 1A
23| 8016| 80
24| 8017| C3
25| 8018| 1E
26| 8019| 80
27| 801A| 47
28| 801B| C3
29| 801C| 1E
30| 801D| 80
31| 801E| B9
32| 801F| DA
33| 8020| 25
34| 8021| 80
35| 8022| C3
36| 8023| 07
37| 8024| 80
38| 8025| 4F
39| 8026| C3
40| 8027| 07
41| 8028| 80
42| 8029| 78
43| 802A| 54
44| 802B| 5D
45| 802C| 12
46| 802D| 13
47| 802E| 79
48| 802F| 12
49| 8030| 76
<End HexData>

<End Comment>
