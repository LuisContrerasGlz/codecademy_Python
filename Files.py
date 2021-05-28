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

# Sometimes you don’t want to iterate through a whole file.
# For that, there’s a different file method, .readline(), which will only read a single line at a time.
# If the entire document is read line by line in this way subsequent calls to .readline() will not throw an error but will start returning an empty string ("").

# Suppose we had this file: millay_sonnet.txt

# I shall forget you presently, my dear,
# So make the most of this, your little day,
# Your little month, your little half a year,
# Ere I forget, or die, or move away,

# script.py

with open('millay_sonnet.txt') as sonnet_doc:
    first_line = sonnet_doc.readline()
    second_line = sonnet_doc.readline()
    print(second_line)

# This script also creates a file object called sonnet_doc that points to the file millay_sonnet.txt.
# It then reads in the first line using sonnet_doc.readline() and saves that to the variable first_line.
# It then saves the second line (So make the most of this, your little day,) into the variable second_line and then prints it out.

with open('just_the_first.txt') as first_line_doc:
    first_line = first_line_doc.readline()
    print(first_line)

# What if we want to create a file of our own? With Python we can do just that. It turns out that our open() function that we’re using to open a file to read needs another argument to open a file to write to.

with open('generated_file.txt', 'w') as gen_file:
    gen_file.write("What an incredible file!")

# Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode.
# The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.
# This code creates a new file in the same folder as script.py and gives it the text What an incredible file!.
# It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.

with open('bad_bands.txt', 'w') as bad_bands_doc:

    bad_bands_doc.write('The Beatles')
