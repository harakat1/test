d1={"fname":"ali","age":23,"Salaray":700}
d2={"fname":"mohamad","age":24,"Salaray":600}
d3={"fname":"khled","age":25,"Salaray":400}
d4={"fname":"ibrahim","age":29,"Salaray":500}
lst=[d1,d2,d3,d4]


dd = {}
da = [[],[],[]]
for F1 in lst:
    for F2 in F1:
        a = {5:0,3:1,7:2}
        da[a[len(F2)]].insert(4,F1[F2])
for i in F1:
    dd.__setitem__(i, da[a[len(i)]])



dd2={"fname":["ali","mohamad","khled","ibrahim"],
    "age":[23,24,25,29],
    "Salaray":[700,600,400,500]
    }


