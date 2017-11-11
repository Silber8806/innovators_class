# Navigate to this folder.

## Type the following command to start a simple web server:

python -m SimpleHTTPServer  

## Go to your browser and type: 127.0.0.1:8000

## To access access files...just add /<filename>

examples:
127.0.0.1:8000/index.html
127.0.0.1:8000/index1.html
127.0.0.1:8000/index2.html
...

## index.html ... etc must exist before you do this.

## index.html

This is a hello world!

## index2.html

This shows you basic tags.

## index3.html

This shows you the basic construct of a webpage.
It has a head and a body.  You put your html in 
the body.

## index4.html

This shows you how to apply colors to individual elements.
This also uses head and body.

## index5.html

You can isolate the css or styles into the head section.  It 
then applies to all eleemnts of a specific type.

## index6.html

The last example I copies from boostrap website.  It just shows you
a more professional website.  If you run http://127.0.0.1/8000/index6.html
you will see a very nice looking web template.  

This is provided as an example at bootstrap main website, but adapted with files locally:

https://v4-alpha.getbootstrap.com/examples/jumbotron/

I would recommend using git pull to get the files...it is not meant as something to type.

## Conclusion.

Web servers like SimpleHTTPServer create a connection with the internet and serve files from the local computer.

In this case:
Computer Name (localhost): 127.0.0.1
Connection point (port): 8000
File_name (path): /index.html

When you type:
127.0.0.1:8000/index.html

It looks up the computer (local one), connects over the port (8000) 
and the web server provides a file called index.html (in file directory).

The browser takes that file and interprets it.


127.0.0.1:8000 

