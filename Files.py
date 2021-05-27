# Computers use file systems to store and retrieve data.
# Each file is an individual container of related information.
# If you’ve ever saved a document, downloaded a song, or even sent an email you’ve created a file on some computer somewhere.
# Even script.py, the Python program you’re editing in the learning environment, is a file.

# Let’s say we had a file called real_cool_document.txt with these contents:
# real_cool_document.txt
# Wowsers!

# We could read that file like this:
# script.py

with open('real_cool_document.txt') as cool_doc:
    cool_contents = cool_doc.read()
print(cool_contents)

# This opens a file object called cool_doc and creates a new indented block where you can read the contents of the opened file.
# We then read the contents of the file cool_doc using cool_doc.read() and save the resulting string into the variable cool_contents.
# Then we print cool_contents, which outputs the statement Wowsers!.

with open('welcome.txt') as text_file:
    text_data = text_file.read()
    print(text_data)

# When we read a file, we might want to grab the whole document in a single string, like .read() would return.
# But what if we wanted to store each line in a variable?
# We can use the .readlines() function to read a text file line by line instead of having the whole thing.

# Suppose we have a file: keats_sonnet.txt
# To one who has been long in city pent,
# ’Tis very sweet to look into the fair
# And open face of heaven,—to breathe a prayer
# Full in the smile of the blue firmament.

# script.py
with open('keats_sonnet.txt') as keats_sonnet:
    for line in keats_sonnet.readlines():
        print(line)

# The above script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt.
# It then iterates over each line in the document and prints the entire file out.

with open('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)
