#!/usr/bin/python3


numbers = {
1 : ["I","X","C"],
2 : ["II","XX","CC"],
3 : ["III","XXX","CCC"],
4 : ["IV","XL","CD"],
5 : ["V","L","D"],
6 : ["VI","LX","DC"],
7 : ["VII","LXX","DCC"],
8 : ["VIII","LXXX","DCCC"],
9 : ["IX","XC","CM"],
0 : ["","",""]
}


print("Roman Numeral")


num=input("Number to Romanize >>> ")


onez=len(num)-1
tenz=len(num)-2
hunz=len(num)-3
touz=str( num[:len(num)-3] )


rn_onez=numbers[int(num[onez])][0]
rn_tenz=numbers[int(num[tenz])][1]
rn_hunz=numbers[int(num[hunz])][2]
rn_touz=int(touz) * "M"


print("{3}{2}{1}{0}" .format(rn_onez,rn_tenz,rn_hunz,rn_touz))
