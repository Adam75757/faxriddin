tpl = (2,3,22,3,4,5,6,3,4,22,5,7)

top = list(filter(lambda x: tpl.count(x)==1,tpl))

print(top)