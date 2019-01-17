import re
pattern='[;]+'
str='fasdfas;falsfjlaj;ljflasdjflsajfl;;;;;;faskldjflsdaj;;;;;;fsdaklfjskldafj;dla;;'
newStr=re.sub(pattern,'\n',str)
print(newStr)