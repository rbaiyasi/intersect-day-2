class EulersMethod(self):
   '''Approximate step in function using Euler's method.'''
   def deriv(self, x, y):
      '''Return derivative (?) of... y?
      Inputs
      ------
      x: float
         Independent variable
      y: float
         Current value of function.
      '''
      return y**2 + y*x + x**3
   def approx(self, y, x, h):
      y_j = y + h*self.deriv(x, y)
      x_j = x + h
      return y_j, x_j
