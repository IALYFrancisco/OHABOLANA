print("Fenoy ny banga.".center(100,"_"));
print("\t... atsimo sy avaratra, izay tsy mahalen-kialofana.\n\tIzay mahavangivangy ... .\n\tAza atao fitia varavarana, tiana fa ... .");
a=input("1\t");
b=input("2\t");
c=input("3\t");
note=0;
print("\n\n")
if(a=="Trano"):
    print("1.MARINA");
    note+=1;
else:
    print("1.DISO");
    note+=0;

if(b=="tian-kavagna"):
    print("2.MARINA");
    note+=1;
else:
    print("2.DISO");
    note+=0;


if(c=="atositosika"):
    print("3.MARINA\n\n");
    note+=1;
else:
    print("3.DISO\n\n");
    note+=0;

R=(note*100)/3;

print("Score= ",round(R),"%");