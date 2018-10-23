#Numeric
width = 20
height = 30
print 'height*width is', height*width

#String manipulation
s = 'First line.\nSecond line.'  # \n means newline
print(s)  # with print(), \n produces a new line

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

#Strings can be concatenated (glued together) with the + operator, and repeated with *:
# 3 times 'un', followed by 'ium'
print "", 3 * 'un' + 'ium', ""

#Strings can be indexed (subscripted), with the first character having index 0. 
#There is no separate character type; a character is simply a string of size one

word = 'Python'
print "word[0]", word[0]  # character in position 0
print "word[5]", word[5]  # character in position 5

print "word[-1]", word[-1]  # last character
print "word[-2]", word[-2]  # second-last character
print "word[-6]", word[-6]

#Note that since -0 is the same as 0, negative indices start from -1.

#In addition to indexing, slicing is also supported.

print "word[0:2]", word[0:2]  # characters from position 0 (included) to 2 (excluded)
print "word[2:5]", word[2:5]  # characters from position 2 (included) to 5 (excluded)
print "word[:2] + word[2:]", word[:2] + word[2:]

#List - written as a list of comma-separated values (items) between square brackets. 
#Lists might contain items of different types, but usually the items all have the same type.
squares = [1, 4, 9, 16, 25]
print "squarers is", squares

#Indexing and slicing
print "squares[0]",  squares[0]  # indexing returns the item
print "squares[-1]", squares[-1]
print "squares[-3:]", squares[-3:]  # slicing returns a new list

#Lists also support operations like concatenation:
squares + [36, 49, 64, 81, 100]
print "squares + [36, 49, 64, 81, 100]", squares + [36, 49, 64, 81, 100]
#Unlike strings, which are immutable, lists are a mutable type, 
#i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
print "cubes unmodified is", cubes
cubes[3] = 64  # replace the wrong value
print "cubes is", cubes

#You can also add new items at the end of the list, 
#by using the append() method (we will see more about methods later):
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print "cubes after append is", cubes

#Assignment to slices is also possible, and this can even 
#change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print "letters is", letters
# replace some values
letters[2:5] = ['C', 'D', 'E']
print "letters after replacement is", letters
# now remove them
letters[2:5] = []
print "letters after deleting a slice", letters
# clear the list by replacing all the elements with an empty list
letters[:] = []
print "letters after clearing all elements", letters

#The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print "length of letters is", letters, "is", len(letters)





