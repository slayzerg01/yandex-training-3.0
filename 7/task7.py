a, b, c = ''.join(open('input.txt', 'r').readlines()).split()
a_h, a_m, a_c = map(int, a.split(":"))
b_h, b_m, b_c = map(int, b.split(":"))
c_h, c_m, c_c = map(int, c.split(":"))
a_s = a_h*3600 + a_m * 60 + a_c
b_s = b_h*3600 + b_m * 60 + b_c
c_s = c_h*3600 + c_m * 60 + c_c
if a_s >= c_s:
    dif = (24*60*60 + c_s - a_s)/2
else:
    dif = (c_s - a_s)/2
new_s = round(b_s + dif + 0.01)
if new_s > 24*60*60:
    new_s = new_s - 24*60*60 
print(f"{new_s//3600:02}:{(new_s%3600)//60:02}:{(new_s%3600)%60:02}")