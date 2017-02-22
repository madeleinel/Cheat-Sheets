formatter = "%r %r %r %r"

# put each variable/string into the string defined as 'formatter'
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# line 8 will insert the 'formatter' string (exactly as it looks above) into each space in the 'formatter' string
print formatter % (formatter, formatter, formatter, formatter)
# need to include commas after each string to make the code work (same as for the shorter strings and variables above)
print formatter % (
    "I had this thing",
    "That you could type up right",
    "But it didn't sing",
    "So I said goodnight"
)
# line 13 is printed with double quotes, while lines 11,12,14 are printed with single quotes >> why is that?
# seems to be bc %r was used (which displays the raw data; python prints the strings "in the most efficient way it can, [...] doesn't have to be pretty")
