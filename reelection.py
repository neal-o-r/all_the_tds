import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def read_names():
        
        with open('tds.txt', 'r') as f:
                txt = f.readlines()

        tds = []
        for line in txt:
                line = line[:-1]
                names = line.split(', ')

                tds_this_house = []
                for name in names:
                        tds_this_house.append(name[1:-1])
                
                tds.append(tds_this_house)

        return tds

def read_dates():

        with open('dates.csv','r') as f:
                txt = f.readlines()

        dates = []
        for line in txt:
                dates.append(int(line.strip().split(',')[1]))

        return dates[1:]
        

def reelection_frac():

        tds = read_names()

        reel_frac = []
        for i in range(0,31):
                seats_in_both  = len(set(tds[i])) + len(set(tds[i+1]))
                people_in_both = len(set(tds[i]).union(set(tds[i+1])))

                reel_frac.append(people_in_both / seats_in_both)
        
        return reel_frac

years = read_dates()
pct   = [i*100 for i in reelection_frac()]

plt.plot(years, pct, 'o-')
plt.ylim(0,100)
plt.ylabel('Re-election %')
plt.xlabel('Year')

plt.show()

