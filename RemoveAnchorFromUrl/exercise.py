def remove_url_anchor(url):
  if(url.find("#") > 0):
    return url[:url.find("#")]
  else:
    return url