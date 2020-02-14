import networkx as nx
import matplotlib.pylab as plot

M = nx.Graph()

C = []

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
                           ('Phetchaburi','Samut Songkhram',57),('Samut Songkhram','Ratchaburi',35)])

edge_labels = nx.get_edge_attributes(M, 'weight')

print('Shortest is : ',nx.shortest_path(M,source='Loei',target='Yasothon',weight='weight'))
print('Shortest length is : ',nx.shortest_path_length(M,source='Loei',target='Yasothon',weight='weight'))

pos = nx.spring_layout(M)
nx.draw(M, pos, with_labels=True, font_color = 'black', node_size=200,font_size=5)
nx.draw_networkx_edge_labels(M, pos, edge_labels=edge_labels)
plot.show()

def THMeun() :
        pass

def ENMeun() :
        pass

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