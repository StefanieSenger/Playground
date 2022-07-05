# converting roman numerals to integers

converting_dict = {
  "I": 1,
  "IV": 4,
  "V": 5,
  "IX": 9,
  "X": 10,
  "XL": 40,
  "L": 50,
  "XC": 90,
  "C": 100,
  "CD": 400,
  "D": 500,
  "CM": 900,
  "M": 1000,
}

def roman_to_int(roman_number):
  sum = 0
  for key in converting_dict:
    if key in roman_number:
      #print(key)
      if key == 'IV':
        sum += converting_dict['IV'] - 6
      elif key == 'IX':
        sum += converting_dict['IX'] - 11
      elif key == 'XL':
        sum += converting_dict['XL'] - 60
      elif key == 'XC':
        sum += converting_dict['XC'] - 110
      elif key == 'CD':
        sum += converting_dict['CD'] -600
      elif key == 'CM':
        sum += converting_dict['CM'] -1100
  for key in roman_number:
    if key in converting_dict:
      sum += converting_dict[key]
  return sum

print(roman_to_int('IV')) #=> 4
print(roman_to_int('XVI')) #=> 16
print(roman_to_int('MI')) #=> 1001
print(roman_to_int("XII"))