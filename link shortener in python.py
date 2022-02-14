import pyshorteners
shorts=pyshorteners.Shortener()
link=input("Enter the link to be shortened:")
print(shorts.tinyurl.short(link))
