mkdir test
mkdir test/test2
mkdir test/test2/test3/test4
mkdir -p test/test2/test3/test4

touch test/test.py
touch test/test2/test2.py
touch test/test2/test3/test3.py
touch test/test2/test3/test4/test4.py

rm test/test.py
rm test/test2/test3/test3.py
rm -R test/test2/test3
rm -R test