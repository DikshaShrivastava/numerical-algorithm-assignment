# ques 5
class PolynomialSolver:
	def F(self,n,L,val):
		return sum(L[i]*(val**i) for i in range(n+1))
	def Fder(self,n,L,val):
		return sum(i*L[i]*(val**(i-1)) for i in range(1,n+1))
	def solve(self,n,L,method):
		if(method=='bisection'):
			print("Input lower bound of interval in which root lies")
			l=int(input())
			print("Input upper bound of interval in which root lies")
			u=int(input())
			print("Input maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,l)-self.F(n,L,u))>0.00001 and it>0):
				m=(l+u)/2
				if(self.F(n,L,l)*self.F(n,L,m)<0):
					u=m
				else:
					l=m
				print (l,u,self.F(n,L,l),self.F(n,L,u))
				it-=1
			return([l,u])
		if(method=='secant'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter upper bound of interval in which root lies")
			u=int(input())
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,l))>0.00001 and it>0):
				f1=self.F(n,L,l)
				f2=self.F(n,L,u)
				l,u=u,u-(((u-l)*f2)/(f2-f1))
				print (l,u,f1,f2)
				it-=1
			return(l)
		if(method=='secantRF'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter upper bound of interval in which root lies")
			u=int(input())
			m=l
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,m))>0.00001 and it>0):
				f1=self.F(n,L,l)
				f2=self.F(n,L,u)
				m=u-(((u-l)*f2)/(f2-f1))
				fm=self.F(n,L,m)
				if(f1*fm<0):
					u=m
				else:
					l=m
				print (m)
				it-=1
			return(l)
		if(method=='newtonraphson'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,l))>0.00001 and it>0):
				l=l-self.F(n,L,l)/self.Fder(n,L,l)
			return(l)
		else:
			return NULL
...
import matplotlib.pyplot as plt
import numpy as np
class PolynomialSolver:
    epsilon, I1, I2, M, poly_coff, Interval = 0.0001, [], [], 0, [], [],
    def BisectionSearch(self, poly_coff, Interval):
        self.poly_coff = poly_coff
        self.Interval = Interval
        self.plot_the_curve()
        while (self.Interval[1]-self.Interval[0]) > self.epsilon:
            self.plot_Interval() 
            self.M = (self.Interval[1]+self.Interval[0])/2.0
            self.I1 = [self.Interval[0],self.M]
            self.I2 = [self.M,self.Interval[1]]
            if self.f(self.I1[0])*self.f(self.I1[1]) < 0:
                self.Interval = self.I1
            else:
                self.Interval = self.I2      
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.annotate('Approximate Root', xy = (self.Interval[0],5.0), xytext = (self.Interval[0],
        self.f(self.Interval[0])+20.0), arrowprops = dict(facecolor = 'black',shrink = 0.01))
        plt.show()
        return self.Interval            
    def f(self,x):
        sum = 0
        for i in range(len(self.poly_coff)):
            sum += self.poly_coff[i]*(x**i)
        return sum
    def plot_the_curve(self):
        x_cor = np.linspace(self.Interval[0], self.Interval[1], 100)
        plt.plot(x_cor,self.f(x_cor), color = '#123456', linewidth = 2.0)
    def plot_Interval(self):
        x_cor = np.array(self.Interval)
        plt.plot(x_cor,self.f(x_cor), 'o')



