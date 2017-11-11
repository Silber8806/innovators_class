echo "This is the command line."
echo "This last exercise will show you how to do similar things here:"

echo ""
echo "This is how to read a file:"
echo "Use cat command:"
cat kafka.data

echo ""
echo ""
echo "You can also count the number of lines:"
echo "use the cat <filename> | wc -l"
cat kafka.data | wc -l

echo ""
echo ""
echo "You can also count the words themselves:"
echo "use the cat <filename> | wc -w"
cat kafka.data | wc -w

echo ""
echo ""
echo "You can also count the characters themselves:"
echo "use the cat <filename> | wc -c"
cat kafka.data | wc -c

echo ""
echo ""
echo "To search a file in the command line, use the following:"
echo "use the grep <pattern> <filename>"
grep " the " kafka.data

echo ""
echo ""
echo "The above lines contain the world ' the '"

echo ""
echo ""
echo "You can filter and then do line,word or character counts too."
echo "You would use grep first and feed it to wc command"
grep " the " kafka.data | wc -l 
echo ""
echo ""
echo "The above is the line count of lines with the in them!"
echo "Note that python and bash might not have the same counts"
echo "This has to do with how the data is interpreted..."
echo "You'll have to always check if some cases are missing"