Class Interpolate:
 
    def solve(self,L,M,method):
        if(method=="newton"):
            return (self.Newton(L,M))
        else:
            return (self.Lagrange(L,M))
    def plot(self,coeffs,L,M):
        coeffs.reverse()
        def f(x):
            order,sum=len(coeffs)-1,0
            for i in range(order+1):
                sum+=(coeffs[i]*(x**(order-i)))
            return sum
        n=int((max(L)-min(L)+2)/0.001)
        x_values=[min(L)-1]
        for i in range(1,n):
            x_values.append(float(str(x_values[0]+(0.001*i))[:5]))
        x_values.append(max(A)+1)
        y_values=[f(x) for x in x_values]
        plt.plot(x_values,y_values,A,B,'r o')
        plt.show()
    

    def Lagrange(self,L,M):                                                
       
        
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(L)                                                           
        x=(-1*L[0],1)                                                      
        for i in range(1,n):
            x=P.polymul(x,(-1*L[i],1))                                    
        result=array([0.0 for i in range(len(x)-1)])                    
        derivative=P.polyder(x)                                             
        for i in range(n):
            result+=(P.polydiv(x,(-1*L[i],1))[0]*M[i])/P.polyval(L[i],derivative)   
        return(list(result))   
    def Newton(self,L,M):                                                   
       
        
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(L)                                                            
        mat=[[0.0 for i in range(n)] for j in range(n)]                    
        for i in range(n):                                                 
            mat[i][0]=M[i]
        for i in range(1,n):                                               
            for j in range(n-i):
                mat[j][i]=(mat[j+1][i-1]-mat[j][i-1])/(L[j+i]-L[j])
        result=array((mat[0][0],))                                          
        for i in range(1,n):
            prod=(-1*L[0],1)                                               
                                                                            
            for j in range(1,i):
                prod=P.polymul(prod,(-1*L[j],1))                              
            result=P.polyadd(result,array(prod)*mat[0][i])
        self.plot(list9result),L,M)
        print("NOTE: coefficients of the terms in the result start from constant term and go up to the highest order term")
        return (list(result))                                               

apx=Interpolate()                                                          
for method in ["newton","lagrange"]:
    solution=apx.solve([1,2,3],[0,-1,0],method)
    print(solution)
