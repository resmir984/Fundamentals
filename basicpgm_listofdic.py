results=[
    {"district":"tvm","win":98,"A+":45000},
    {"district":"ktm","win":95,"A+":44000},
    {"district":"apy","win":97,"A+":47000},
    {"district":"idk","win":90,"A+":38000},
    {"district":"ekm","win":99,"A+":56000},
    {"district":"pta","win":99,"A+":58000},
    {"district":"tsr","win":98,"A+":57000},
    {"district":"kzd","win":99,"A+":58000},
    {"district":"pkd","win":95,"A+":50000},
    {"district":"mpm","win":90,"A+":4500}
]


#1. win % of tvm

for result in results:
    if result["district"]=="tvm":
        print(result["win"])
    #result={"district":"tvm","win":98,"A+":45000}
tvm_win=[result["win"] for result in results if result["district"]=="tvm"]
print(tvm_win)
#or
print([res for res in results if res["district"]=="tvm"])

#2. district with highest win %



# district with lowest win %
# district with highest A+
# district with lowest A+
# total number of A+
# total win %
# sort districts wrt win % order by asc

#sorting
def get_win(res):
    return res["win"]
results.sort(key=get_win,reverse=True)
print(results)
#or
results.sort(key=lambda res:res["win"],reverse=True)
print(results)

print(max(results,key=lambda res:res["win"]))   #for max
print(min(results,key=lambda res:res["win"]))   #for min

for res in results:                        #tvm win %
    if res["district"]=="tvm":
        print(res["win"])
#or
tvm_details=[res for res in results if res["district"]=="tvm"]        #list_comprehension
print(tvm_details)

#for sorting use methods are sorted(),or lst.sort()
results.sort(reverse=True,key=lambda res:res["win"])      #sorting using win
print(results)

#max win %
aplus=max(results,key=lambda res:res["A+"])
print(aplus)

win=max(results,key=lambda res:res["win"])
print(win)

#aplu_total=sum(results,ley=lamda res:res["A+"]
#print(aplu_total)                               #sum() takes no keyword arguments

aplus=[res["A+"] for res in results]                     #A+ list
print(aplus)

aplus=sum([res["A+"] for res in results])                #sum of A+ lst
print(aplus)
#or
print(sum([res["A+"] for res in results]))                #sum of A+ lst
#or
sum=0
for res in results:
    sum+=res["A+"]
print(sum)

