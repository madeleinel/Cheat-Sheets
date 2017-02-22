days = "Mon Tue Wed Thu Fri Sat Sun"
# '\n' creates a line break
# this does not display when using %r, as that command prints the code the way it was written
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "here are the days: ", days
print "here are the months: ", months

# using triple double quotes allows us to type 'unlimited text' within the quotation marks
# within these, we don't need to use '\n' or similar >> the code will be printed as it is written within the file
print """
    There's something going on here.
    With the three double quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
    """

# '\' >> an escape sequence that encodes difficult-to-type characters into a string
# or with other characters creates 'other commands', eg '\n' creates a line break within the string
# or "string /"quote/" continued string" will print the quotation marks around the quote
