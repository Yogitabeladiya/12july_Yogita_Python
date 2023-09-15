# acednding and desending by value
d={ "yogita":101, "rinkal":25, "mital":21,
      "nena": 12,  "bhagvati":34    
} 


 #sort by values
y1=sorted(d.items(),key=lambda x:x[1])
print(dict(y1))



