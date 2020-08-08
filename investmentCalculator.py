from matplotlib import pyplot as plt



def invest(initial,rate=1.07,time=10,yearly=0):
	f = 10
	frequency = f * time -1
	time = time/frequency
	total = initial
	array = [initial]
	array2 = [frequency/f]
	while frequency != 0:
		if frequency % f == 0 :
			total += yearly
		frequency -= 1
		total = total*rate**(time)
		array.append(total)
		array2.append(frequency/f)
	array2.reverse()
	plt.style.use('seaborn')
	plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
	plt.plot(array2,array)
	plt.xlabel('Time (years)')
	plt.ylabel('Capital (USD)')
	plt.title('Growth of Capital')
	plt.show()

def ask():
	while True:
		initial = int(input('Amount you invest initially: '))
		rate = 1+ float(input('Expected annual growth percentage\nExample: Enter 10 for 10% growth   :  '))/100
		time = int(input('Number of years you will invest for: '))
		yearly = int(input('Amount of money you will add on every year\n(Added to account in the beginning of every year)  : '))
		invest(initial,rate,time,yearly)
		if input('Would you like to model another investment? (yes/no) : ').lower() == 'yes':
			continue
		else: 
			break
print("\n\nThis is EasyInvest, a simple tool to graph your investments!\n\n")
ask()
print("\n\n\nThank you for using EasyInvest by MustafaLabs.")









