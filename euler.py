class EulersMethod(self):
   def deriv(self, x, y):
       return y**2 + y*x + x**3
   def approx(self, y, x, h):
       y_j = y + h*self.deriv(x, y)
       x_j = x + h
       return y_j, x_j
