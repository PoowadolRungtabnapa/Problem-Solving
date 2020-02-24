import networkx as nx
import matplotlib.pylab as plot

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

edge_labels = nx.get_edge_attributes(G, 'weight')
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_color = 'black', node_size=200,font_size=5)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plot.show()

print(nx.shortest_path(G,source='Bangkok',target='Chiang Rai',weight='weight'))