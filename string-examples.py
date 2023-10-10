

# Metody do stosowania na stringach

s = "ala ma kota!"
print(s.capitalize())
print(s.title())
print(s.count("a"))
print(s.upper())
print(s.lower())
print(len(s))
print(s.find("ala1"))
print(s.index("ma"))
s = s + " A Marek ma psa!"
print(s)
words = s.split(" ")
print(words)
print("|".join(words))

# array slicing
s = "Ala ma kota!"
print(s[0:5]) # od indeksu 0 do indeksu 4 (wlacznie)
print(s[:5]) # od indeksu 0 do indeksu 4 (wlacznie)
print(s[4:12]) #od indeksu 4 do konca
print(s[4:])
print(s[10:12]) # ostatnie dwa znaki
print(s[-2:]) # ostatnie dwa znaki
print(s[:-1]) # wez wszystkie oprocz ostatniego

# 3xS RULE
# [ START : STOP : STEP]
print(s[0:12:2])
print(s[::2])

s = "Kobyła ma mały bok"
s = s.upper().replace(" ","")
print(s)
print(s[::-1])

s = " \t  ABC FEFGH KJL \n\r\f "
print("|", s.strip(), "|", sep="")
