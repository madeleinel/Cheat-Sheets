# '%r' is for debugging, '%s' is for displaying
# >> so escape sequences won't work when using '%r', but will work when using '%s'

# '\t' indents the line
tabby_cat = "\tI'm tabbed in"
# '\n creates a line break'
persian_cat = "I'm split\non a line"
# '\\' will print '\'
backslash_cat = "I'm \\ a \\ cat"
# '\t*' will create a bullet list item
# '"""' will print whatever's within the quotation marks, and eliminates the need to 'force'/create line breaks
fat_cat = """
    I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    """

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

skinny_cat = '''
    let's try
    a new command
    triple single quotes
    woohoo
    '''

print skinny_cat
# can't see a difference between """ and '''
# "In triple-quoted strings, unescaped newlines and quotes are allowed (and are retained), except that three unescaped quotes in a row terminate the string. (A “quote” is the character used to open the string, i.e. either ' or ".) There is no difference between using single quotes and double quotes in Python." (from 2012)
# 'can use either depending on what feels best or what everyone else is doing.' (the course)

# will make the characters on line 23 flash in the terminal
# use ctrl+c to exit
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
