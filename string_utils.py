def split_before_each_uppercases(formula):
    start = 0
    end = 0
    split_formula[]
    for i in range (1,len(formula)):
      if formula[i].isupper:
        split_formula.append(formula[start:end])
        start = end
      split_formula.append(formula[start:len(formula)])  
    return split_formula    




def split_at_first_digit ():
  digit_location = 1
  for ch in formula [1:]:
    if ch.isdigit():
      break
    digit_location += 1 
  if digit_location == len(formula):
    return formula , 1 
  else:
    prefix = formula [:digit_location]
    numeric part = formula[digit_location:]
    return prefix , formula  
