import networkx as nx
import matplotlib.pylab as plot
from tkinter import *
from tkinter.ttk import *
from time import strftime

index = 0

G = nx.Graph()
#sout
G.add_edge('Narathiwat','Yala', weight=128)
G.add_edge('Narathiwat','Pattani', weight=35)
G.add_edge('Pattani', 'Yala', weight=94)
G.add_edge('Pattani','Songkhla', weight=99)
G.add_edge('Yala', 'Songkhla', weight=128)
G.add_edge('Songkhla','Satun', weight=125)
G.add_edge('Songkhla', 'Phatthalung', weight=121)
G.add_edge('Satun', 'Trang', weight=140)
G.add_edge('Trang', 'Phatthalung', weight=56)
G.add_edge('Trang', 'Krabi', weight=131)
G.add_edge('Trangt','Nakhon Si Thammarat', weight=123)
G.add_edge('Phatthalung', 'Nakhon Si Thammarat', weight=99)
G.add_edge('Nakhon Si Thammarat', 'Krabi', weight=223)
G.add_edge('Nakhon Si Thammarat', 'Surat Thani', weight=134)
G.add_edge('Krabi', 'Surat Thani', weight=211)
G.add_edge('Krabi', 'Phangnga', weight=86)
G.add_edge('Phangnga', 'Surat Thani', weight=196)
G.add_edge('Phangnga', 'Phuket', weight=87)
G.add_edge('Surat Thani', 'Chumphon', weight=193)
G.add_edge('Surat Thani', 'Ranong', weight=219)
G.add_edge('Phangnga', 'Ranong', weight=226)
G.add_edge('Ranong', 'Chumphon', weight=117)
G.add_edge('Chumphon', 'Prachuap Khiri Khan', weight=183)
G.add_edge( 'Prachuap Khiri Khan', 'Phetchaburi', weight=158)
G.add_edge('Phetchaburi', 'Ratchaburi', weight=54)
G.add_edge('Ranong', 'Chumphon', weight=117)
G.add_edge('Chumphon', 'Prachuap Khiri Khan', weight=183)
#noth
G.add_edge('Chiang rai', 'Phayao', weight=94)
G.add_edge('Chiang rai', 'Chiang mai', weight=182)
G.add_edge('Chiang rai', 'Lampang', weight=225)
G.add_edge('Phayao', 'Chiang rai', weight=94)
G.add_edge('Phayao', 'Lampang', weight=131)
G.add_edge('Phayao', 'Nan', weight=176)
G.add_edge('Phayao', 'Phrae', weight=141)
G.add_edge('Mae Hong Son', 'Chiang mai', weight=349)
G.add_edge('Mae Hong Son', 'Tak', weight=499)
G.add_edge('Chiang mai', 'Chiang rai', weight=182)
G.add_edge('Chiang mai', 'Lampang', weight=92)
G.add_edge('Chiang mai', 'Lampoon', weight=21)
G.add_edge('Chiang mai', 'Tak', weight=265)
G.add_edge('Chiang mai', 'Mae Hong son', weight=349)
G.add_edge('Lampoon', 'Lampang', weight=71)
G.add_edge('Lampoon', 'Chiang mai', weight=21)
G.add_edge('Lampoon', 'Tak', weight=244)
G.add_edge('Lampang', 'Chiang rai', weight=97)
G.add_edge('Lampang', 'Chiang mai', weight=92)
G.add_edge('Lampang', 'Phayao', weight=131)
G.add_edge('Lampang', 'Phrae', weight=109)
G.add_edge('Lampang', 'Sukhothai', weight=207)
G.add_edge('Lampang', 'Tak', weight=174)
G.add_edge('Lampang', 'Lampoon', weight=71)
G.add_edge('Phrae', 'Phayao', weight=141)
G.add_edge('Phrae', 'Nan', weight=118)
G.add_edge('Phrae', 'Lampang', weight=109)
G.add_edge('Phrae', 'Uttaradit', weight=74)
G.add_edge('Phrae', 'Sukhothai', weight=165)
G.add_edge('Nan', 'Phrae', weight=118)
G.add_edge('Nan', 'Uttaradit', weight=191)
G.add_edge('Nan', 'Phayao', weight=118)
G.add_edge('Tak', 'Mae Hong son', weight=499)
G.add_edge('Tak', 'Chiang mai', weight=265)
G.add_edge('Tak', 'Lampoon', weight=244)
G.add_edge('Tak', 'Lampang', weight=174)
G.add_edge('Tak', 'Sukhothai', weight=79)
G.add_edge('Tak', 'Kamphaeng Phet', weight=68)
G.add_edge('Tak', 'Nakhonsawan', weight=185)
G.add_edge('Tak', 'Uthai Thani', weight=234)
G.add_edge('Sukhothai', 'Phrae', weight=165)
G.add_edge('Sukhothai', 'Uttaradit', weight=100)
G.add_edge('Sukhothai', 'Phitsanulok', weight=59)
G.add_edge('Sukhothai', 'Kamphaeng phet', weight=77)
G.add_edge('Sukhothai', 'Tak', weight=79)
G.add_edge('Sukhothai', 'Lampang', weight=207)
G.add_edge('Uttaradit', 'Phrae', weight=74)
G.add_edge('Uttaradit', 'Nan', weight=191)
G.add_edge('Uttaradit', 'Sukhothai', weight=100)
G.add_edge('Uttaradit', 'Phitsanulok', weight=118)
G.add_edge('Phitsanulok', 'Phetchabun', weight=170)
G.add_edge('Phitsanulok', 'Sukhothai', weight=59)
G.add_edge('Phitsanulok', 'Kamphaeng Phet', weight=103)
G.add_edge('Phitsanulok', 'Phichit', weight=73)
G.add_edge('Phitsanulok', 'Uttaradit', weight=118)
G.add_edge('Kamphaeng Phet', 'Tak', weight=68)
G.add_edge('Kamphaeng Phet', 'Phichit', weight=90)
G.add_edge('Kamphaeng Phet', 'Nakhonsawan', weight=117)
G.add_edge('Kamphaeng Phet', 'Sukhothai', weight=77)
G.add_edge('Kamphaeng Phet', 'Phitsanulok', weight=103)
G.add_edge('Phichit', 'Phitsanulok', weight=73)
G.add_edge('Phichit', 'Kamphaeng Phet', weight=90)
G.add_edge('Phichit', 'Nakhonsawan', weight=113)
G.add_edge('Phichit', 'Phetchabun', weight=129)
G.add_edge('Nakhonsawan', 'Phichit', weight=113)
G.add_edge('Nakhonsawan', 'Phetchabun', weight=184)
G.add_edge('Nakhonsawan', 'Kamphaeng Phet', weight=117)
G.add_edge('Nakhonsawan', 'Uthai Thani', weight=50)
G.add_edge('Nakhonsawan', 'Tak', weight=185)
G.add_edge('Phetchabun', 'Phichit', weight=129)
G.add_edge('Phetchabun', 'Phitsanulok', weight=170)
G.add_edge('Phetchabun', 'Nakhonsawan', weight=184)
G.add_edge('Uthai Thani', 'Tak', weight=234)
G.add_edge('Uthai Thani', 'Nakhonsawan', weight=50)
#mid
G=nx.Graph()
G.add_edge('Bangkok','Samut Prakan',weight=29)
G.add_edge('Bangkok','Samut Sakhon',weight=36)
G.add_edge('Bangkok','Nakhon Pathom',weight=56)
G.add_edge('Bangkok','Nonthaburi',weight=20)
G.add_edge('Bangkok','Pathum Thani',weight=46)
G.add_edge('Bangkok','Prachinburi',weight=136)
G.add_edge('Bangkok','Chachoengsao',weight=82)

G.add_edge('Trat','Chanthaburi',weight=70)

G.add_edge('Chanthaburi','Rayong',weight=110)
G.add_edge('Chanthaburi','Chonburi',weight=164)
G.add_edge('Chanthaburi','Chachoengsao',weight=228)
G.add_edge('Chanthaburi','Sa Kaeo',weight=258)

G.add_edge('Rayong','Chonburi',weight=98)

G.add_edge('Chonburi','Samut Prakan',weight=64)
G.add_edge('Chonburi','Chachoengsao',weight=43)
G.add_edge('Samut Prakan','Chachoengsao',weight=71)
G.add_edge('Sa Kaeo','Chachoengsao',weight=245)
G.add_edge('Sa Kaeo','Prachinburi',weight=98)

G.add_edge('Prachinburi','Nakhon Nayok',weight=29)

G.add_edge('Nakhon Nayok','Saraburi',weight=58)
G.add_edge('Nakhon Nayok','Pathum Thani',weight=101)

G.add_edge('Saraburi','Lopburi',weight=46)
G.add_edge('Saraburi','Phra Nakhon Si Ayutthaya',weight=63)
G.add_edge('Saraburi','Pathum Thani',weight=101)
G.add_edge('Saraburi','Ang Thong',weight=58)
G.add_edge('Saraburi','Sing Buri',weight=79)

G.add_edge('Samut Sakhon','Samut Prakan',weight=65)
G.add_edge('Samut Songkhram','Samut Sakhon',weight=37)
G.add_edge('Prachuap Khiri Khan','Phetchaburi',weight=158)
G.add_edge('Phetchaburi','Ratchaburi',weight=54)
G.add_edge('Phetchaburi','Samut Songkhram',weight=53)

G.add_edge('Ratchaburi','Samut Songkhram',weight=43)
G.add_edge('Ratchaburi','Samut Prakan',weight=129)
G.add_edge('Ratchaburi','Nakhon Pathom',weight=41)
G.add_edge('Ratchaburi','Suphan Buri',weight=147)
G.add_edge('Ratchaburi','Kanchanaburi',weight=87)
G.add_edge('Kanchanaburi','Suphan Buri',weight=91)

G.add_edge('Suphan Buri','Chai Nat',weight=294)
G.add_edge('Suphan Buri','Sing Buri',weight=1056)
G.add_edge('Suphan Buri','Ang Thong',weight=44)
G.add_edge('Suphan Buri','Phra Nakhon Si Ayutthaya',weight=176)
G.add_edge('Suphan Buri','Nakhon Pathom',weight=105)
G.add_edge('Nakhon Pathom','Samut Sakhon',weight=85)

G.add_edge('Chai Nat','Sing Buri',weight=53)
G.add_edge('Chai Nat','Ang Thong',weight=92)
G.add_edge('Lopburi','Sing Buri',weight=33)
G.add_edge('Ang Thong','Sing Buri',weight=40)
G.add_edge('Ang Thong','Lopburi',weight=67)
G.add_edge('Ang Thong','Phra Nakhon Si Ayutthaya',weight=31)

G.add_edge('Phra Nakhon Si Ayutthaya','Pathum Thani',weight=122)
G.add_edge('Phra Nakhon Si Ayutthaya','Nonthaburi',weight=96)
G.add_edge('Phra Nakhon Si Ayutthaya','Nakhon Pathom',weight=132)
G.add_edge('Pathum Thani','Nonthaburi',weight=26)
#esan
G.add_edge('nakornphanom', 'bungkal',weight =176)
G.add_edge('nakornphanom', 'sakonnakhon',weight =93)
G.add_edge('nakornphanom', 'mookdaharn',weight =104)
G.add_edge('bungkal','nongkay',weight =143)
G.add_edge('bungkal','sakonnakhon',weight =194)
G.add_edge('nongkay','loey',weight =202)
G.add_edge('nongkay','udonthani',weight =51)
G.add_edge('loey','udonthani',weight =152)
G.add_edge('loey','nongbualamphu',weight =106)
G.add_edge('loey','khonkaen',weight =206)
G.add_edge('nongbualamphu','udonthani',weight =46)
G.add_edge('nongbualamphu','khonkaen',weight =181)
G.add_edge('udonthani','sakonnakhon',weight =159)
G.add_edge('udonthani','khonkaen',weight =115)
G.add_edge('udonthani','kallasin',weight =192)
G.add_edge('sakonnakhon','kallasin',weight =128)
G.add_edge('sakonnakhon','mookdaharn',weight =119)
G.add_edge('mookdaharn','kallasin',weight =172)
G.add_edge('mookdaharn','royied',weight =162)
G.add_edge('mookdaharn','yasotorn',weight =166)
G.add_edge('mookdaharn','amnajcharoen',weight =88)
G.add_edge('kallasin','khonkaen',weight =77)
G.add_edge('kallasin','mahasarakham',weight =44)
G.add_edge('kallasin','royied',weight =47)
G.add_edge('khonkaen','chaiyaphum',weight =150)
G.add_edge('khonkaen','mahasarakham',weight =73)
G.add_edge('khonkaen','buriram',weight =200)
G.add_edge('khonkaen','nakhonrachasima',weight =190)
G.add_edge('chaiyaphum','nakhonrachasima',weight =119)
G.add_edge('mahasarakham','royied',weight =40)
G.add_edge('mahasarakham','buriram',weight =145)
G.add_edge('royied','buriram',weight =146)
G.add_edge('royied','surin',weight =137)
G.add_edge('royied','srisaket',weight =230)
G.add_edge('royied','yasotorn',weight =71)
G.add_edge('yasotorn','amnajcharoen',weight =54)
G.add_edge('yasotorn','srisaket',weight =159)
G.add_edge('amnajcharoen','ubonrachathani',weight =75)
G.add_edge('ubonrachathani','srisaket',weight =61)
G.add_edge('srisaket','surin',weight =105)
G.add_edge('surin','buriram',weight =50)
G.add_edge('buriram','nakhonrachasima',weight =124)

City = ['Narathiwat','Yala','Pattani','Songkhla','Satun','Trang','Phatthalung','Nakhon Si Thammarat',
        'Krabi','Phuket','Phang Nga','Surat Thani','Ranong','Chumphon','Prachuap Khiri Khan','Phetchaburi',
        'Samut Songkhram','Samut Sakhon','Nonthaburi','Bangkok','Samut Prakan','Ratchaburi','Trat','Chanthaburi',
        'Rayong','Chonburi','Chachoengsao','Sa Kaew','PrachinBuri','NakhonPathom','PathhumThani','NakhonNayok',
        'Kanchanaburi','Suphanburi','Ayutthaya','AngThong','Saraburi','NakonRatchasima','Buriram','Surin',
        'Sisaket','Ubon Ratchathani','Uthaithani','Chainat','Singburi','Lopburi','Nakon Sawan','Chaiyaphum',
        'Maha Sarakam','Roi Et','Yasothon','AmnatCharoen','Tak','KamphaengPhet','Phichit','Phetchabun',
        'Khon Kean','Kalasin','Mukdahan','Nakhon Phanom','Sakon Nakhon','Udon Thani',
        'Nong BuaLamphu','Loei','Phitsanulok','Sukhothai','Nong Khai','Bueng Kan','Uttaradit','Phrae',
        'Nan','Lampang','Lamphun','Mae Hong Son','Chiang Mai','Phayao','Chiang Rai']

'''
M.add_weighted_edges_from([('Loei','Nong Khai',234),('Loei','Nong BuaLamphu',99),('Loei','Khon Kean',207),('Loei','Chaiyaphum',227),
                           ('Nong Khai','Bueng Kan',135),('Nong Khai','Udon Thani',52),('Nong BuaLamphu','Udon Thani',51),('Udon Thani','Bueng Kan',207),
                           ('Nong BuaLamphu','Khon Kean',118),('Chaiyaphum','Khon Kean',141),('Khon Kean','Udon Thani',121),('Chaiyaphum','NakonRatchasima',121),
                           ('Khon Kean','NakonRatchasima',192),('Bueng Kan','Nakhon Phanom',181),('Udon Thani','Sakon Nakhon',166),('Bueng Kan','Sakon Nakhon',196),
                           ('Udon Thani','Kalasin',149),('Kalasin','Sakon Nakhon',129),('Sakon Nakhon','Nakhon Phanom',94),('Kalasin','Khon Kean',100),
                           ('Khon Kean','Maha Sarakam',72),('Maha Sarakam','NakonRatchasima',214),('Maha Sarakam','Kalasin',48),('Sakon Nakhon','Mukdahan',114),
                           ('Kalasin','Mukdahan',164),('Mukdahan','Nakhon Phanom',110),('Kalasin','Roi Et',49),('Roi Et','Maha Sarakam',44),
                           ('Maha Sarakam','Buriram',149),('Buriram','NakonRatchasima',127),('Buriram','Roi Et',149),('Roi Et','Mukdahan',149),
                           ('Mukdahan','AmnatCharoen',99),('AmnatCharoen','Yasothon',57),('Yasothon','Mukdahan',115),('Yasothon','Roi Et',68),
                           ('Yasothon','AmnatCharoen',57),('Buriram','Surin',55),('Surin','Roi Et',145),('Roi Et','Sisaket',146),
                           ('Sisaket','Surin',106),('Sisaket','Yasothon',103),('Sisaket','Ubon Ratchathani',65),('Ubon Ratchathani','Yasothon',103),
                           ('Ubon Ratchathani','AmnatCharoen',77),('Kanchanaburi','Suphanburi',98),('Kanchanaburi','NakhonPathom',67),
                           ('Kanchanaburi','Ratchaburi',81),('Ratchaburi','NakhonPathom',48),('NakhonPathom','Suphanburi',97),('Phetchaburi','Ratchaburi',58),
                           ('Phetchaburi','Samut Songkhram',57),('Samut Songkhram','Ratchaburi',35),('NakhonPathom','Samut Sakhon',67),
                           ('Samut Sakhon','Ratchaburi',67),('Samut Sakhon','Samut Songkhram',38),('Suphanburi','Chainat',101),('Chainat','Uthaithani',26),
                           ('Uthaithani','Nakon Sawan',43),('Nakon Sawan','Chainat',62),('Singburi','Chainat',57),('Chainat','Nakon Sawan',100),
                           ('AngThong','Singburi',40),('AngThong','Suphanburi',77),('Suphanburi','Ayutthaya',64),('AngThong','Ayutthaya',39),
                           ('Ayutthaya','NakhonPathom',32),('Nonthaburi','NakhonPathom',64),('Bangkok','Nonthaburi',22),('NakhonPathom','Bangkok',57),
                           ('Samut Sakhon','Bangkok',36),('Nonthaburi','Ayutthaya',75),('Lopburi','Nakon Sawan',151),('Lopburi','Singburi',32),
                           ('Lopburi','AngThong',42),('Saraburi','Ayutthaya',69),('Lopburi','Saraburi',47),('Saraburi','PathhumThani',85),
                           ('PathhumThani','Ayutthaya',60),('PathhumThani','Nonthaburi',27),('PathhumThani','Bangkok',42),('NakhonNayok','Saraburi',58),
                           ('PathhumThani','NakhonNayok',117),('PrachinBuri','NakhonNayok',20),('PrachinBuri','Bangkok',145),('Chachoengsao','Bangkok',85),
                           ('Chachoengsao','NakhonNayok',75),('Chachoengsao','PrachinBuri',74),('Samut Prakan','Bangkok',26),('Samut Prakan','Chonburi',70),
                           ('Chonburi','Chachoengsao',50),('Prachuap Khiri Khan','Chumphon',189),('Ranong','Chumphon',126),('Chumphon','Surat Thani',184),
                           ('Surat Thani','Ranong',218),('Phang Nga','Ranong',231),('Phang Nga','Surat Thani',159),('Phang Nga','Phuket',87),
                           ('Phang Nga','Krabi',74),('Krabi','Surat Thani',156),('Surat Thani','Nakhon Si Thammarat',140),('Nakhon Si Thammarat','Krabi',172),
                           ('Krabi','Trang',126),('Trang','Phatthalung',58),('Phatthalung','Nakhon Si Thammarat',109),('Phatthalung','Songkhla',122),
                           ('Songkhla','Satun',125),('Satun','Trang',144),('Songkhla','Yala',131),('Songkhla','Pattani',105),('Pattani','Yala',60),
                           ('Narathiwat','Yala',89),('Narathiwat','Pattani',96),('Mae Hong Son','Chiang Mai',237),
                           
                           ('Mae Hong Son','Tak',508),('Chiang Mai','Chiang Rai',190),
                          ('Chiang Mai','Lampang',114),('Chiang Mai','Lamphun',39),('Tak','Lamphun',241),
                          ('Tak','Sukhothai',85),('Tak','Kamphaeng Phet',62),('Chiang Rai','Phayao',92),
                          ('Lampang','Chiang Rai',229),('Lampang','Phayao',142),('Lampang','Phrae',96),
                          ('Lampang','Lamphun',82),('Lampang','Tak',188),('Lampang','Sukhothai',195),('Phayao','Nan',148),
                          ('Phayao','Phrae',143),('Nan','Phrae',119),('Phrae','Sukhothai',163),('Phrae','Uttaradit',72),
                          ('Sukhothai','Kamphaeng Phet',71),('Sukhothai','Phitsanulok',58),('Uttaradit','Phitsanulok',108),('Uttaradit','Sukhothai',91),
                          ('Phitsanulok','Kamphaeng Phet',110),('Phitsanulok','Phichit',100),('Phitsanulok','Phetchabun',177),
                          ('Kamphaeng Phet','Phichit',100),('Kamphaeng Phet','Nakhon Sawan',132),('Phichit','Phetchabun',133),
                          ('Phichit','Nakhon Sawan',104),('Phetchabun','Nakhon Sawan',174),('Uthai Thani','Nakhon Sawan',43),
                          
                          
                          ( 'Saraburi' , 'PathhumThani',85 ) , ( 'Saraburi' ,'NakhonNayok',58 ) , ('PathhumThani','Nonthaburi',27 ) , ( 'PathhumThani', 'Bangkok', 42) ,
                          ( 'NakhonNayok','PrachinBuri',20) ,( 'NakhonNayok','Chachoengsao',75 ) , ('Bangkok','Chachoengsao', 85 ) , ( 'PrachinBuri','Chachoengsao',74 ) ,
                          ('PrachinBuri','Sa Kaew',104) , ('Bangkok','PrachinBuri', 145 ) ,('Bangkok','Samut Prakan', 26 ) , ('Samut Prakan','Chachoengsao', 81) ,
                          ( 'Samut Prakan' , 'Chonburi',70 ) , ('Chonburi','Chachoengsao',50 ) , ( 'Chachoengsao','Rayong',135 ) , ( 'Chonburi', 'Rayong',98 ) , 
                          ( 'Rayong' , 'Chanthaburi',110 ) , ('Chachoengsao' ,'Chanthaburi',228 ) , ('Chachoengsao' , 'Sa Kaew',245) , ('Sa Kaew', 'Chanthaburi',161 ) , 
                          ('Chanthaburi', 'Trat',69 )])
'''

TH = [('1.กระบี่'),('2.กรุงเทพมหานคร'),('3.กาญจนบุรี'),('4.กาฬสินธุ์'),('5.กำแพงเพชร'),('6.ขอนแก่น'),('7.จันทบุรี'),('8.ฉะเชิงเทรา'),
        ('9.ชลบุรี'),('10.ชัยนาท'),('11.ชัยภูมิ'),('12.ชุมพร'),('13.เชียงราย'),('14.เชียงใหม่'),('15.ตรัง'),('16.ตราด'),
        ('17.ตาก'),('18.นครนายก'),('19.นครปฐม'),('20.นครพนม'),('21.นครราชสีมา'),('22.นครศรีธรรมราช'),('23.นครสวรรค์'),
        ('24.นนทบุรี'),('25.นราธิวาส'),('26.น่าน'),('27.บึงกาฬ'),('28.บุรีรัมย์'),('29.ปทุมธานี'),('30.ประจวบคีรีขันธ์'),
        ('31.ปราจีนบุรี'),('32.ปัตตานี'),('33.พระนครศรีอยุธยา'),('34.พะเยา'),('35.พังงา'),('36.พัทลุง'),('37.พิจิตร'),
        ('38.พิษณุโลก'),('39.เพชรบุรี'),('40.เพชรบูรณ์'),('41.แพร่'),('42.ภูเก็ต'),('43.มหาสารคาม'),('44.มุกดาหาร'),
        ('45.แม่ฮ่องสอน'),('46.ยโสธร'),('47.ยะลา'),('48.ร้อยเอ็ด'),('49.ระนอง'),('50.ระยอง'),('51.ราชบุรี'),
        ('52.ลพบุรี'),('53.ลำปาง'),('54.ลำพูน'),('55.เลย'),('56.ศรีสะเกษ'),('57.สกลนคร'),('58.สงขลา'),('59.สตูล'),
        ('60.สมุทรปราการ'),('61.สมุทรสงคราม'),('62.สมุทรสาคร'),('63.สระแก้ว'),('64.สระบุรี'),('65.สิงห์บุรี'),('66.สุโขทัย'),
        ('67.สุพรรณบุรี'),('68.สุราษฎร์ธานี'),('69.สุรินทร์'),('70.หนองคาย'),('71.หนองบัวลำภู'),('72.อ่างทอง'),
        ('73.อำนาจเจริญ'),('74.อุดรธานี'),('75.อุตรดิตถ์'),('76.อุทัยธานี'),('77.อุบลราชธานี')]

ENG = [('1.Krabi'),('2.Bangkok'),('3.Kanchanaburi'),('4.Kalasin'),('5.Kamphaeng Phet'),('6.Khon Kaen '),('7.Chanthaburi'),('8.Chachoengsao'),
        ('9.Chonburi'),('10.Chainat'),('11.Chaiyaphum'),('12.Chumphon'),('13.Chiang Mai '),('14.Chiang Rai'),('15.Trang'),('16.Trat'),
        ('17.Tak'),('18.Nakhon Nayok'),('19.Nakhon Pathom'),('20.Nakhon Phanom'),('21.Nakhon Ratchasima'),('22.Nakhon Si Thammarat'),('23.Nakhon Sawan'),
        ('24.Nonthaburi'),('25.Narathiwat'),('26.Nan'),('27.Bueng Kan'),('28.Buriram'),('29.Pathum Thani'),('30.Prachuap Khiri Khan'),
        ('31.Prachinburi'),('32.Pattani'),('33.Phra Nakhon Si Ayutthaya'),('34.Phayao'),('35.Phang Nga'),('36.Phatthalung'),('37.Phichit'),
        ('38.Phitsanulok'),('39.Phetchaburi'),('40.Phetchabun'),('41.Phrae'),('42.Phuket'),('43.Maha Sarakham'),('44.Mukdahan'),
        ('45.Mae Hong Son'),('46.Yasothon'),('47.Yala'),('48.Roi Et'),('49.Ranong'),('50.Rayong'),('51.Rayong'),
        ('52.Lopburi'),('53.Lampang'),('54.Lamphun'),('55.Loei'),('56.Sisaket'),('57.Sakon Nakhon'),('58.Songkhla'),('59.Satun'),
        ('60.Samut Prakan'),('61.Samut Songkhram'),('62.Samut Sakhon'),('63.Sa Kaeo'),('64.Saraburi'),('65.Sing Buri'),('66.Sukhothai'),
        ('67.Suphan Buri'),('68.Surat Thani'),('69.Surin'),('70.Nong Khai'),('71.Nong Bua Lamphu'),('72.Ang Thong'),
        ('73.Amnat Charoen'),('74.Udon Thani'),('75.Uttaradit'),('76.Uthai Thani'),('77.Ubon Ratchathani')]

E = ['Krabi','Bangkok','Kanchanaburi','Kalasin','Kamphaeng Phet','Khon Kaen ','Chanthaburi','Chachoengsao',
        'Chonburi','Chainat','Chaiyaphum','Chumphon','Chiang Mai ','Chiang Rai','Trang','Trat',
        'Tak','Nakhon Nayok','Nakhon Pathom','Nakhon Phanom','Nakhon Ratchasima','Nakhon Si Thammarat','Nakhon Sawan',
        'Nonthaburi','Narathiwat','Nan','Bueng Kan','Buriram','Pathum Thani','Prachuap Khiri Khan',
        'Prachinburi','Pattani','Phra Nakhon Si Ayutthaya','Phayao','Phang Nga','Phatthalung','Phichit',
        'Phitsanulok','Phetchaburi','Phetchabun','Phrae','Phuket','Maha Sarakham','Mukdahan',
        'Mae Hong Son','Yasothon','Yala','Roi Et','Ranong','Rayong','Rayong',
        'Lopburi','Lampang','Lamphun','Loei','Sisaket','Sakon Nakhon','Songkhla','Satun',
        'Samut Prakan','Samut Songkhram','Samut Sakhon','Sa Kaeo','Saraburi','Sing Buri','Sukhothai',
        'Suphan Buri','Surat Thani','Surin','Nong Khai','Nong Bua Lamphu','Ang Thong',
        'Amnat Charoen','Udon Thani','Uttaradit','Uthai Thani','Ubon Ratchathani']


def THMeun() :
        global index
        print('===| เลือกจังหวัดที่ต้องการ |===')
        for i in TH :
                print(i)
        c = 'uc'
        while c != 'c' :
                Start = int(input('เลือกต้นทาง : '))
                if 77 >= Start >= 1 :
                        c = 'c'
                else :
                        c= 'uc'

        c= 'uc'
        while c != 'c' :
                First = int(input('เลือกจุดที่ 1 แต่ถ้าไม่ต้องการให้เลือก 0 : '))
                if 77 >= First >= 1 and Start != First  :
                        index = 1
                        c = 'c'
                elif First == 0 :
                        index = 0
                        First = 0
                        c = 'c'
                else :
                        c = 'uc'
        
        c = 'uc'
        while c != 'c' and index == 1  :
                Second = int(input('เลือกจุดที่ 2 แต่ถ้าไม่ต้องการให้เลือก 0 : '))
                if 77 >= Second >= 1 and Start != Second and Second != First :
                        index = 2
                        c = 'c'
                elif Second == 0 :
                        Second = 0
                        c = 'c'
                else :
                        c = 'uc'

        if index == 0 :
                Second = 0
                First = 0

        c = 'uc'
        while c != 'c' : 
                Place = int(input('เลือกปลายทาง : '))
                if 77 >= Place >= 1 and Start != Place and Place != Second and Place != First :
                        c = 'c'
                else :
                        c = 'uc'

        if E[Start - 1 ] in City :
                print('Start In')
        if E[First - 1] in City and First != 0 :
                print('First In')
        if E[Second - 1] in City and Second != 0:
                print('Second In') 
        if E[Place - 1] in City :
                print('Place In')       

        Count(Start,First,Second,Place)

def Count(Start,First,Second,Place) :
        global index
        edge_labels = nx.get_edge_attributes(G, 'weight')

        S_1 = E[Start-1]
        if index == 1 or index == 2:
                F_1 = E[First-1]
        if index == 2 :
                S_2 = E[Second-1]
        P_1 = E[Place-1]

        if index == 0 :
                P = nx.shortest_path(G,source=S_1,target=P_1,weight='weight')
                C = nx.shortest_path_length(G,source=S_1,target=P_1,weight='weight')
                print(f'Shortest from {S_1} to {P_1} : {P} ')
                print(f'Shortest length from {S_1} to {P_1} : {C}')
        if index == 1 :
                F = nx.shortest_path(G,source=S_1,target=F_1,weight='weight')
                P = nx.shortest_path(G,source=F_1,target=P_1,weight='weight')
                C = nx.shortest_path_length(G,source=S_1,target=F_1,weight='weight') + nx.shortest_path_length(M,source=F_1,target=P_1,weight='weight')

                A = nx.shortest_path_length(G,source=S_1,target=F_1,weight='weight')
                B = nx.shortest_path_length(G,source=S_1,target=P_1,weight='weight')
                
                if A < B :
                        W = nx.shortest_path_length(G,source=F_1,target=P_1,weight='weight')
                        print(f'Shortest from {S_1} to {F_1} : {F} {A}')
                        print(f'Shortest from {F_1} to {P_1} : {P} {B}')
                        print(f'Shortest length from {S_1} to {P_1} : {A + W}')
                elif A > B :
                        W = nx.shortest_path_length(G,source=F_1,target=P_1,weight='weight')
                        print(f'Shortest from {S_1} to {P_1} : {F} {B}')
                        print(f'Shortest from {P_1} to {F_1} : {P} {A}')
                        print(f'Shortest length from {S_1} to {P_1} : {W + B}')

        if index == 2 :
                F = nx.shortest_path(G,source=S_1,target=F_1,weight='weight')
                S = nx.shortest_path(G,source=F_1,target=S_2,weight='weight')
                P = nx.shortest_path(G,source=S_2,target=P_1,weight='weight')
                C = nx.shortest_path_length(G,source=S_1,target=F_1,weight='weight') + nx.shortest_path_length(G,source=F_1,target=S_2,weight='weight') + nx.shortest_path_length(G,source=S_2,target=P_1,weight='weight')
                print(f'Shortest from {S_1} to {F_1} : {F}  ')
                print(f'Shortest from {F_1} to {S_2} : {S}  ')
                print(f'Shortest from {S_2} to {P_1} : {P} ')
                print(f'Shortest length from {S_1} to {P_1} : {C}')
                
        pos = nx.spring_layout(G)
        
        nx.draw(G, pos, with_labels=True, font_color = 'black', node_size=200,font_size=5)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plot.show()

def ENMeun() :
        global index
        print('===| Choose |===')
        for i in ENG :
                print(i)
        c = 'uc'
        while c != 'c' :
                Start = int(input('Start From : '))
                if 77 >= Start >= 1 :
                        c = 'c'
                else :
                        c= 'uc'

        c= 'uc'
        while c != 'c' :
                First = int(input('Your First Rest Area ( If Not Have Choose 0 ) : '))
                if 77 >= First >= 1 and Start != First  :
                        index = 1
                        c = 'c'
                elif First == 0 :
                        index = 0
                        First = 0
                        c = 'c'
                else :
                        c = 'uc'

        c = 'uc'
        while c != 'c' and index == 1 :
                Second = int(input('Your Second Rest Area ( If Not Have Choose 0 ) : '))
                if 77 >= Second >= 1 and Start != Second and Second != First :
                        index = 2
                        c = 'c'
                elif Second == 0 :
                        Second = 0
                        c = 'c'
                else :
                        c = 'uc'

        c = 'uc'
        
        if index == 0 :
                Second = 0
                First = 0
        while c != 'c' : 
                Place = int(input('Your Destination : '))
                if 77 >= Place >= 1 and Start != Place and Place != Second and Place != First :
                        c = 'c'
                else :
                        c = 'uc'

        if E[Start - 1 ] in City :
                print('Start In')
        if E[First - 1] in City and First != 0 :
                print('First In')
        if E[Second - 1] in City and Second != 0:
                print('Second In') 
        if E[Place - 1] in City :
                print('Place In')    
                
        Count(Start,First,Second,Place)

def main() :
        correct = 'uncorrect'
        L = input('Enter TH/EN : ')
        while correct != 'correct' :
                if L == 'TH' :
                        correct = 'correct'
                        THMeun()
                elif L == 'EN' :
                        correct = 'correct'
                        ENMeun()
                else :
                        print(']----------[')
                        print('Error Choose')
                        print(']----------[')
                        correct = 'uncorrect'
                        L = input('Enter TH/EN : ')

main()