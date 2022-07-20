
frameworks=[
    {"fw_name":"django","language":"python","rating":4},
    {"fw_name": "flask", "language": "python", "rating": 4},
    {"fw_name": "oodo", "language": "python", "rating": 4},
    {"fw_name": "express", "language": "javascript", "rating": 5},
    {"fw_name": "wordpress", "language": "php", "rating": 3},
]

fw_names=[fw["fw_name"] for fw in frameworks]
print(fw_names)

print([fw["rating"] for fw in frameworks])            #rating print

print([fw["language"] for fw in frameworks])          #language print
#or
for fw in frameworks:
    print(fw["language"])

print([fw["fw_name"] for fw in frameworks if fw["language"]=="python"])    #print python frameworks

#print all framework name whose rating > 4
print([fw["fw_name"] for fw in frameworks if fw["rating"]>4])

#sort frameworks based on rating
frameworks.sort(key=lambda fw:fw["rating"],reverse=True)
print(frameworks)
#or
def get_rating(fw):
    return fun["rating"]
frameworks.sort(key=get_rating,reverse=True)
print(frameworks)

#sorted() and frameworks.sort() are used
#ajith[*height]<jithesh[*height] can compare
frameworks.sort(key=lambda fw:fw["rating"])
print(frameworks)

# fw decending order sort
frameworks.sort(key=lambda fw:fw["rating"],reverse=True)
print(frameworks)

#print highest rating fw

#[max()
#lst=[10,23,11,1,15]
#square==>map
#even==>filter
#sum==>map
#highest no==>max
#tot sum==>sum()
#lowest no==>min]

#map,filter(condition),reduce
#print all fw name==>map
#print all fw rating==>map
