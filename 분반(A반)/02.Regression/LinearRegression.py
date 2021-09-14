# Linear Regression  y= Wx + b
import random

#Gradient
def g_W(x, y, iters):
    total=0.0
    for i in range(len(x)):
        total += W[iters]*pow(x[i],2)+b[iters]*x[i]-x[i]*y[i]
    return total

def g_b(x, y, iters):
    total=0.0
    for i in range(len(x)):
        total += W[iters]*x[i] + b[iters] - y[i]
    return total

# cost function
def  costfunction(x, y, W, b, iters):
    total = 0.0
    for i in range(len(x)):
        total += pow(W[iters]*x[i]+b[iters]-y[i],2)
    return total/2

#테스트 세트
X = [-3, -2, -1, 0, 1, 2, 3]
y = [-3, -2, -1, 0, 1, 2, 3]  #y1
#y = [-2, -1, -0, 1, 2, 3, 4] #y2
# 화학 반응 
#X=[10, 20, 30, 40]
#y=[71, 45, 24, 8]
# 동아리 키-몸무게 관계 
#X=[157, 160, 160, 168, 172, 175, 175, 177, 182, 184, 188, 190]
#y=[42,   48,  54,  58,  63,  69,  71,  73,  70,  80, 79, 81]

M1_W=[0.0]
M1_b=[0.0]

# Method 1: statistical
print('====================================================')
print(' Method 1:  Statistical Method')
print('====================================================')

Xmean = sum(X)/len(X)
Ymean = sum(y)/len(y) 
print('Xmean:', Xmean, 'Ymean:',Ymean)
print('-----------------------------------------------------')
total1 = 0
total2 = 0
for i in range(len(X)):
    total1 +=  (y[i]-Ymean)*(X[i]-Xmean)
    total2 += pow(X[i]-Xmean, 2)
M1_W[0] = total1/total2
M1_b[0] = Ymean-M1_W[0]*Xmean

print('Linear Regression by Method 1 : y =', M1_W[0],'* x +',M1_b[0])
print('-----------------------------------------------------')
print('y        y_hat ')
print('-------------------')
for i in range(len(X)):
    print(y[i], '   ', M1_W[0]*X[i]+M1_b[0])
print('-------------------')
M1_cost = costfunction(X, y, M1_W, M1_b, 0)
print('cost: ', M1_cost)
print('-------------------')
input('strike any key..')   

# Method 2
print('====================================================')
print(' Method 2:  Gradient Descent Method')
print('====================================================')
W=[0.0]
b=[0.0]
W[0] = float( random.randint(-100, 100))   ## M1_W[0] #
b[0] = float(random.randint(-100, 100))    ##  M1_b[0] #

 #This tells us when to stop the algorithm
iters = 0 #iteration counter
cost = costfunction(X, y, W, b, iters) 

print("Iteration",iters,"\tW[0]:",W[0],"\tb[0]:",b[0],"\tcost:",cost)

rate =  10/cost # Learning rate   ## 0.000001* cost #
MaxItrs = cost   ## 10000  #
precision = 0.0001       ## M1_cost *0.8
while cost > precision: # and iters < MaxItrs:
    iters = iters+1
    gradientW = g_W(X, y, iters-1)
    gradientB = g_b(X, y, iters-1)
    newW = W[iters-1] - rate*gradientW
    newb = b[iters-1] - rate*gradientB
    W.append(newW)
    b.append(newb)
    if iters %100==0:  # 동아리 키-몸무게 사례에서는 1000000로 설정
        print('iteration: ', iters, end=',')
        print('gradient W: %.1f, gradient b:%.1f, ' % (gradientW, gradientB), end=' ')
        print('W[ %d ]:%.1f, b[%d]:%.1f, cost: %.1f'
                % (iters, W[iters] , iters, b[iters], cost))
        ans = input()
        if ans =='q':           
            break
print('iteration: ', iters, end=',')
print('gradient W: %.1f, gradient b:%.1f, ' % (gradientW, gradientB), end=' ')
print('W[ %d ]:%.1f, b[%d]:%.1f, cost: %.1f'
                % (iters, W[iters] , iters, b[iters], cost))
print('-----------------------------------------------------------')
print('Linear Regression by Method2: y =', W[iters],'* x +',b[iters])
print('-----------------------------------------------------------')
print('y        y_hat ')
print('---------------------')
for i in range(len(X)):
    print(y[i], '   ', W[iters]*X[i]+b[iters])


print('====================================================')
print('%10s   %10s   %10s'%  ('y','M1:y_hat','M2:y_hat'))
print('-----------------------------------------------------')
for i in range(len(X)):
    print('%10.1f   %10.3f   %10.3f' % (float(y[i]), M1_W[0]*X[i]+M1_b[0],  W[iters]*X[i]+b[iters]) )
print('------------------------------------------------------')
print('%10s:  %10.3f   %10.3f' % ('cost', costfunction(X, y, M1_W, M1_b, 0), costfunction(X, y, W, b, iters)) )
