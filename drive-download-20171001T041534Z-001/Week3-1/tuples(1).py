#tuple is a sequence of immutable Python objects. 
#Tuples are sequences, just like lists. 
#The differences between tuples and lists are, the tuples cannot be changed unlike lists and 
#tuples use parentheses, whereas lists use square brackets.

#The empty tuple is written as two parentheses containing nothing

tup1 = ();
tup2 = (1, 2, 3, 4, 5 );

print "tup1 is", tup1
#print "tup1[0]: ", tup1[0]
print "tup2 is", tup2
print "tup2[1:5]: ", tup2[1:5]

tup3 = (12, 34.56);
tup4 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup3[0] = 100;

# So let's create a new tuple as follows
print "tup3 is", tup3
print "tup4 is", tup4
tup5 = tup3 + tup4;
print "tup3+tup4", tup5

tup = ('physics', 'chemistry', 1997, 2000);

print tup
del tup;
print "After deleting tup : "
print tup

#Operators like cmp, len, max, min etc
