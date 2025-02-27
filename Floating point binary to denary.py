#Floating Point Binary Converter - www.101computing.net/floating-point-binary-converter/  
  
binary = input("Input a number in binary using a normalised floating point notation based on a 5-bit mantissa and 3 bit exponent: ")

if len(binary)!=8:
  print("Invalid binary number - 8 bits required.")
  exit()

mantissa = binary[:5]
exponent = binary[-3:]

print("Mantissa: " + mantissa)
print("Exponent: " + exponent)

mantissa = [int(x) for x in str(mantissa)]
exponent = [int(x) for x in str(exponent)]

#Complete the code here to work out the decimal value...
def mant(mantissa):
  denary = 0
  for i in range(len(mantissa)):
    if mantissa[i] == 1:
      if i == 0:
        denary += -1
      elif i == 1:
        denary += 0.5
      elif i == 2:
        denary += 0.25
      elif i == 3:
        denary += 0.125
      elif i == 4:
        denary += 0.0625
  return denary

def expo(exponent):
  denary = 0
  for i in range(len(exponent)):
    if exponent[i] == 1:
      if i == 0:
        denary += -4
      elif i == 1:
        denary += 2
      elif i == 2:
        denary += 1
  return denary
  
manti = mant(mantissa)
expon = expo(exponent)
final = manti*(2**expon)
print ("Your denary number of", binary, " is:", final)
