lst_to_string = ['The','Python','Tutorials']
str_join = ",".join(lst_to_string)
print ("After join:",str_join)

lst_mixed = [10, 'The','Python','Tutorials',15.5]
str_join = " ".join(str(x) for x in lst_mixed)
print("After str and join:",str_join)

lst_mixed = ['List','to','String by map',9.9, 50]
str_join_map = " ".join(map(str, lst_mixed))
print("After map and join:",str_join_map)


print(" cruel ".join(["hello", "world", "AHHHH!"]))



