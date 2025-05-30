from subprocess import check_output

mountains = ['Mount Everest', 'K2','Mont Blanc','Kilimanjaro','Denali']
rivers = ['Nile','Amazon','Yangtze','Mississippi','Danube']
countries = ['Japan','Canada','Brazil','South Africa','Germany']
cities = ['New York','Tokyo','Paris','Sydney','Cairo']
languages = ['English','Spanish','Mandarin Chinese','Arabic','French']


#sort function
mountains.sort()
print(mountains)
#sort(reverse=True)
mountains.sort(reverse=True)
print(mountains)

# sorted()
print(sorted(rivers))
print(sorted(rivers,reverse=True))

# reverse()
countries.reverse()
print(countries)


#length of a list
print(len(languages))