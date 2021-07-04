import googletrans
dict = googletrans.LANGUAGES
dict2 = {}
count = 0
for i in dict.items():
    if(i[0]=='hi'):
        print(count)
    dict2[i[1]] = i[0]
    count += 1
print(dict2)