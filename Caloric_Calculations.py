g = input("M or F?  ")
bw = float(input("Body Weight (lbs.):  "))
h = float(input("Height (in.):  "))
a = int(input("Age:  "))
al = int(input("Activity Level (1-5):  "))
def mancalc(bw, h, a):
	calc1 = (66+(6.3*bw)+(12.9*h)-(6.8*a))
	if al == 1:
		return calc1*1.2
	if al == 2:
		return calc1*1.375
	if al == 3:
		return calc1*1.55
	if al == 4:
		return calc1*1.725
	if al == 5:
		return calc1*1.9
print(mancalc(bw,h,a))
