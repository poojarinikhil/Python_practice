D2={"NIKHIL":"SHAWARMA","KARTHIK":"BIRYANI", "MAHEK":"KABAB", "SNEHALI": "BAIGAN"}
print(D2)
print(D2["SNEHALI"])
del D2["KARTHIK"]
print(D2)
d3=D2.copy()#for copy if you not use copy it will be pointer and reflect the changes you have done to D2
del D2["MAHEK"]
print("this is d3 : ")
print(d3)
print("this is D2 : ")
print(D2)
# this is used only to print keys
print(D2.keys())
# this is to print items
print(D2.items())