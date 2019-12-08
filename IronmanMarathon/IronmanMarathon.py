def i_tri(s):
  if(s == 0):
    return 'Starting Line... Good Luck!'
  elif(s < 2.4):
    return {"Swim": str('%.2f' % round(140.60 - s, 2)) + ' to go!'}
  elif(s > 2.4 and s < 112):
    return {"Bike":str('%.2f' % round(140.60 - s, 2)) + ' to go!'}
  elif(s > 112 and s < 140.60):
    if(140.6 - s <= 10):
      return {"Run": 'Nearly there!'}
    else:
      return {"Run":str('%.2f' % round(140.60 - s, 2)) + ' to go!'}
  else:
    return "You're done! Stop running!"