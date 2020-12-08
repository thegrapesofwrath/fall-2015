x <- c(-1,0,1,2)
X <- matrix(c(-1,1,-1,1,
							 0,0,0,1,
							 1,1,1,1,
							 8,4,2,1),ncol=4,byrow=T)
X.in <- solve(X)
coef <- runif(4,min=-1,max=1)
y <- X%*%coef
plot(x,y)

beta <- X.inv%*%y

sup <- seq(-1,2,len=1024)
lines(sup,beta[1]*sup^3+beta[2]*sup^2+beta[3]*sup+beta[4])

x <- c(x,3)
X <- rbind(X,c(27,9,3,1))
y <- X%*%coef
plot(x,y)

beta <-solve(t(x)%*%X)%*%t(X)%*%y
sup <- seq(-1,3,len=1024)
lines(sup,beta[1]*sup^3+beta[2]*sup^2+beta[3]*sup+beta[4])

beta1 <- X.inv%*%y[1:4]
beta2 <- X.inv%*%y[2:5]


################
#consider a 6th order spline


x <- c(-1,0,1,2)
X <- matrix(c(-1,1,-1,1,
							 0,0,0,1,
							 1,1,1,1,
							 8,4,2,1),ncol=4,byrow=T)
X.in <- solve(X)
coef <- runif(6,min=-1,max=1)
Xtrue <- matrix(c(-1^(6:0),
									 0^(6:0),
									 1^(6:0),
									 2^(6:0)),ncol=7,byrow=T)
y <- Xtrue%*%coef
plot(x,y)

beta <- X.inv%*%y

sup <- seq(-1,2,len=1024)
lines(sup,beta[1]*sup^3+beta[2]*sup^2+beta[3]*sup+beta[4])
lines(sup,coef[1]*sup^6+coef[2]*sup^5+coef[3]*sup^4+coef[4]*sup^3+coef[5]*sup^2+coef[6]*sup^1+coef[7],col='red')


# here is the 6th  order. To match the graphs we will need 6 betas

x <- -1:5
Xtrue <- matrix(c(-1^(6:0),
									0^(6:0),
									1^(6:0),
									2^(6:0),
									3^(6:0),
									4^(6:0),
									5^(6:0)),ncol=7,byrow=T)
									
y <- Xtrue%*%coef
plot(x,y)

beta1 <- Xinv%*%y[1:4]
beta2 <- Xinv%*%y[2:5]
beta3 <- Xinv%*%y[3:6]
beta4 <- Xinv%*%y[4:7]

sup <- seq(-1,2,len=1024)
lines(sup,beta1[1]*sup^3+beta1[2]*sup^2+beta1[3]*sup+beta1[4])
lines(sup+1,beta2[1]*sup^3+beta2[2]*sup^2+beta2[3]*sup+beta2[4])
lines(sup+2,beta3[1]*sup^3+beta3[2]*sup^2+beta3[3]*sup+beta3[4])
lines(sup+3,beta4[1]*sup^3+beta4[2]*sup^2+beta4[3]*sup+beta4[4])




##Another example with some new random coefficients

