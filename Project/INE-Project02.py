import networkx as nx
import matplotlib.pylab as plot
from tkinter import *
from tkinter.ttk import *
from time import strftime

index = 0

G = nx.Graph()

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

G.add_weighted_edges_from([('Loei','Nong Khai',202),('Loei','Nong BuaLamphu',106),('Loei','Khon Kean',206),('Loei','Chaiyaphum',227),
                           ('Nong Khai','Bueng Kan',143),('Nong Khai','Udon Thani',51),('Nong BuaLamphu','Udon Thani',46),
                           ('Nong BuaLamphu','Khon Kean',181),('Chaiyaphum','Khon Kean',150),('Khon Kean','Udon Thani',115),
                           ('Chaiyaphum','NakonRatchasima',119),('Buriram','Khon Kean',200),('Khon Kean','NakonRatchasima',190),
                           ('Bueng Kan','Nakhon Phanom',176),('Udon Thani','Sakon Nakhon',159),('Bueng Kan','Sakon Nakhon',194),
                           ('Udon Thani','Kalasin',192),('Kalasin','Sakon Nakhon',128),('Sakon Nakhon','Nakhon Phanom',93),
                           ('Kalasin','Khon Kean',77),('Khon Kean','Maha Sarakam',73),('Maha Sarakam','NakonRatchasima',214),
                           ('Maha Sarakam','Kalasin',44),('Sakon Nakhon','Mukdahan',119),('Kalasin','Mukdahan',172),('Mukdahan','Nakhon Phanom',104),
                           ('Kalasin','Roi Et',47),('Roi Et','Maha Sarakam',40),('Maha Sarakam','Buriram',145),('Buriram','NakonRatchasima',124),
                           ('Buriram','Roi Et',146),('Roi Et','Mukdahan',162),('Mukdahan','AmnatCharoen',88),('AmnatCharoen','Yasothon',54),
                           ('Yasothon','Mukdahan',166),('Yasothon','Roi Et',71),('Yasothon','AmnatCharoen',57),('Buriram','Surin',50),
                           ('Surin','Roi Et',137),('Roi Et','Sisaket',230),
                           ('Sisaket','Surin',105),('Sisaket','Yasothon',159),('Sisaket','Ubon Ratchathani',61),('Ubon Ratchathani','Yasothon',103),
                           ('Ubon Ratchathani','AmnatCharoen',75),

                           ('Lopburi','NakonRatchasima',198),('Saraburi','NakonRatchasima',152),('NakhonNayok','NakonRatchasima',231),('PrachinBuri','NakonRatchasima',194),
                           ('NakonRatchasima','Sa Kaew',174),('Sa Kaew','Buriram',221),('Nakhon Sawan','Chainat',64),('Nakhon Sawan','Lopburi',130),('Nakhon Sawan','Saraburi',175),
                           ('Uthaithani','Kanchanaburi',197),('Uthaithani','Suphanburi',126),('Chaiyaphum','Phetchabun',215),('Chaiyaphum','Lopburi',243),('Loei','Phetchabun',190),
                           ('Loei','Phitsanulok',269),



                           
                           ('Kanchanaburi','Suphanburi',91),('Kanchanaburi','NakhonPathom',67),('Singburi','Suphanburi',70),
                           ('Kanchanaburi','Ratchaburi',87),('Ratchaburi','NakhonPathom',41),('NakhonPathom','Suphanburi',105),('Phetchaburi','Ratchaburi',54),
                           ('Phetchaburi','Samut Songkhram',53),('Samut Songkhram','Ratchaburi',43),('NakhonPathom','Samut Sakhon',85),
                           ('Samut Sakhon','Ratchaburi',67),('Samut Sakhon','Samut Prakan',65),('Samut Sakhon','Samut Songkhram',37),('Suphanburi','Chainat',101),('Chainat','Uthaithani',26),
                           ('Uthaithani','Nakon Sawan',43),('Nakon Sawan','Chainat',62),('Singburi','Chainat',53),('Chainat','Nakon Sawan',100),
                           ('AngThong','Singburi',40),('AngThong','Saraburi',58),('AngThong','Suphanburi',44),('Suphanburi','Ayutthaya',176),('AngThong','Ayutthaya',31),
                           ('Ayutthaya','NakhonPathom',132),('Nonthaburi','NakhonPathom',64),('Bangkok','Nonthaburi',20),('NakhonPathom','Bangkok',56),
                           ('Samut Sakhon','Bangkok',36),('Nonthaburi','Ayutthaya',96),('Lopburi','Nakon Sawan',151),('Lopburi','Singburi',53),
                           ('Lopburi','AngThong',67),('Saraburi','Ayutthaya',63),('Lopburi','Saraburi',46),('Saraburi','PathhumThani',101),('Saraburi','Singburi',79),
                           ('PathhumThani','Ayutthaya',122),('PathhumThani','Nonthaburi',26),('PathhumThani','Bangkok',46),('NakhonNayok','Saraburi',58),
                           ('PathhumThani','NakhonNayok',101),('PrachinBuri','NakhonNayok',20),('PrachinBuri','Bangkok',136),('Chachoengsao','Bangkok',82),
                           ('Chachoengsao','NakhonNayok',75),('Chachoengsao','PrachinBuri',74),('Samut Prakan','Bangkok',29),('Samut Prakan','Chonburi',70),
                           ('Chonburi','Chachoengsao',50),('Prachuap Khiri Khan','Phetchaburi',158),('Prachuap Khiri Khan','Chumphon',183),('Ranong','Chumphon',117),('Chumphon','Surat Thani',193),
                           ('Surat Thani','Ranong',219),('Phang Nga','Ranong',226),('Phang Nga','Surat Thani',196),('Phang Nga','Phuket',87),
                           ('Phang Nga','Krabi',86),('Krabi','Surat Thani',211),('Surat Thani','Nakhon Si Thammarat',134),('Nakhon Si Thammarat','Krabi',223),
                           ('Krabi','Trang',131),('Trang','Phatthalung',56),('Phatthalung','Nakhon Si Thammarat',99),('Phatthalung','Songkhla',121),
                           ('Songkhla','Satun',125),('Satun','Trang',140),('Trang','Nakhon Si Thammarat',123),('Songkhla','Yala',128),('Songkhla','Pattani',99),('Pattani','Yala',94),
                           ('Narathiwat','Yala',128),('Narathiwat','Pattani',35),('Mae Hong Son','Chiang Mai',349),('Mae Hong Son','Tak',499),('Chiang Mai','Chiang Rai',182),
                          ('Chiang Mai','Lampang',92),('Chiang Mai', 'Tak',265),('Chiang Mai','Lamphun',21),('Tak','Lamphun',244),('Tak','Sukhothai',79),('Tak','Kamphaeng Phet',68),
                          ('Chiang Rai','Phayao',94),('Lampang','Chiang Rai',97),('Lampang','Phayao',131),('Lampang','Phrae',109),('Tak', 'Nakhon Sawan',185),('Lampang','Lamphun',71),
                          ('Lampang','Tak',174),('Lampang','Sukhothai',207),('Phayao','Nan',176),('Nan', 'Uttaradit',191),('Phayao','Phrae',141),('Nan','Phrae',118),
                          ('Phrae','Sukhothai',165),('Phrae','Uttaradit',74),('Sukhothai','Kamphaeng Phet',77),('Sukhothai','Phitsanulok',59),('Uttaradit','Phitsanulok',118),('Uttaradit','Sukhothai',100),
                          ('Phitsanulok','Kamphaeng Phet',103),('Phitsanulok','Phichit',73),('Phitsanulok','Phetchabun',170),('Tak','Uthai Thani',234),
                          ('Kamphaeng Phet','Phichit',90),('Kamphaeng Phet','Nakhon Sawan',117),('Phichit','Phetchabun',129),('Phichit','Nakhon Sawan',113),
                          ('Phetchabun','Nakhon Sawan',184),('Uthai Thani','Nakhon Sawan',50),( 'Saraburi' , 'PathhumThani',85),('Saraburi','NakhonNayok',58), 
                          ('PathhumThani','Nonthaburi',27 ),('PathhumThani','Bangkok', 42),
                          ( 'NakhonNayok','PrachinBuri',29),('NakhonNayok','Chachoengsao',75),('Bangkok','Chachoengsao',85),('PrachinBuri','Chachoengsao',74),
                          ('PrachinBuri','Sa Kaew',98),('Bangkok','PrachinBuri',145),('Bangkok','Samut Prakan',26),('Samut Prakan','Chachoengsao',71),
                          ('Samut Prakan','Chonburi',64 ),('Chonburi','Chachoengsao',43 ),('Chachoengsao','Rayong',135),('Chonburi','Rayong',98), 
                          ('Chanthaburi','Chonburi',164),('Rayong','Chanthaburi',110),('Chachoengsao','Chanthaburi',228 ), 
                          ('Chachoengsao','Sa Kaew',245),('Sa Kaew','Chanthaburi',258), 
                          ('Chanthaburi','Trat',70 )])

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
        'Chonburi','Chainat','Chaiyaphum','Chumphon','Chiang Rai','Chiang Mai','Trang','Trat',
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
                # A > B > C > D (A,B) (B,C) (C,D)
                A_B = nx.shortest_path_length(G,source=S_1,target=F_1,weight='weight')
                B_C = nx.shortest_path_length(G,source=F_1,target=S_2,weight='weight')
                C_D = nx.shortest_path_length(G,source=S_2,target=P_1,weight='weight')
                # A > B > D > C (A,B) (B,D) (D,C) 
                B_D = nx.shortest_path_length(G,source=F_1,target=P_1,weight='weight')
                D_C = nx.shortest_path_length(G,source=P_1,target=S_2,weight='weight')
                # A > C > B > D (A,C) (C,B) (B,D)
                A_C = nx.shortest_path_length(G,source=S_1,target=S_2,weight='weight')
                C_B = nx.shortest_path_length(G,source=S_2,target=F_1,weight='weight')
                # A > C > D > B (A,C) (C,D) (D,B)
                D_B = nx.shortest_path_length(G,source=P_1,target=F_1,weight='weight')
                # A > D > B > C (A,D) (D,B) (B,C)
                A_D = nx.shortest_path_length(G,source=S_1,target=P_1,weight='weight')
                # A > D > C > B (A,D) (D,C) (C,B)
                if A_B < B_C < C_D :
                        print(f"Shortest from {S_1} to {F_1} : {nx.shortest_path(G,source=S_1,target=F_1,weight='weight')}")
                        print(f'Shortest from {F_1} to {S_2} : {nx.shortest_path(G,source=F_1,target=S_2,weight="weight")}')
                        print(f'Shortest from {S_2} to {P_1} : {nx.shortest_path(G,source=S_2,target=P_1,weight="weight")} ')
                        print(f'Shortest length all is {A_B + B_C + C_D}')
                elif A_B < B_D < D_C :
                        print(f'Shortest from {S_1} to {F_1} : {nx.shortest_path(G,source=S_1,target=F_1,weight="weight")}  ')
                        print(f'Shortest from {F_1} to {P_1} : {nx.shortest_path(G,source=F_1,target=P_1,weight="weight")}  ')
                        print(f'Shortest from {P_1} to {S_2} : {nx.shortest_path(G,source=P_1,target=S_2,weight="weight")} ')
                        print(f'Shortest length all is {A_B + B_D + D_C}')
                elif A_C < C_B < B_D :
                        print(f'Shortest from {S_1} to {S_2} : {nx.shortest_path(G,source=S_1,target=S_2,weight="weight")}  ')
                        print(f'Shortest from {S_2} to {F_1} : {nx.shortest_path(G,source=S_2,target=F_1,weight="weight")}  ')
                        print(f'Shortest from {F_1} to {P_1} : {nx.shortest_path(G,source=F_1,target=P_1,weight="weight")} ')
                        print(f'Shortest length all is {A_C + C_B + B_D}')
                elif A_C < C_D < D_B :
                        print(f'Shortest from {S_1} to {S_2} : {nx.shortest_path(G,source=S_1,target=S_2,weight="weight")}  ')
                        print(f'Shortest from {S_2} to {P_1} : {nx.shortest_path(G,source=S_2,target=P_1,weight="weight")}  ')
                        print(f'Shortest from {P_1} to {F_1} : {nx.shortest_path(G,source=P_1,target=F_1,weight="weight")} ')
                        print(f'Shortest length all is {A_C + C_D + D_B}')
                elif A_D < D_B < B_C :
                        print(f'Shortest from {S_1} to {P_1} : {nx.shortest_path(G,source=S_1,target=P_1,weight="weight")}  ')
                        print(f'Shortest from {P_1} to {F_1} : {nx.shortest_path(G,source=P_1,target=F_1,weight="weight")}  ')
                        print(f'Shortest from {F_1} to {S_2} : {nx.shortest_path(G,source=F_1,target=S_2,weight="weight")} ')
                        print(f'Shortest length all is {A_D + D_B + B_C}')
                elif A_D < D_C < C_B :
                        print(f'Shortest from {S_1} to {P_1} : {nx.shortest_path(G,source=S_1,target=P_1,weight="weight")}  ')
                        print(f'Shortest from {P_1} to {S_2} : {nx.shortest_path(G,source=P_1,target=S_2,weight="weight")}  ')
                        print(f'Shortest from {S_2} to {F_1} : {nx.shortest_path(G,source=S_2,target=F_1,weight="weight")} ')
                        print(f'Shortest length all is {A_D + D_C + C_B}')
                
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