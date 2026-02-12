#!/bin/bash


#pelican content -o output/ -s pelicanconf.py -t /home/wrongbaud/projects/vss/blog-resources/pelican-themes/pelican-bootstrap3

for file in $(ls output/*.html)
do
sed -i 's/<table>/<table class="tb tr tc table table-hover">/g' $file
sed -i 's/<img/<img class="center" height="80%" width="80%" style="border: 4px solid black;"/g' $file
done

#cp vss-style.css output/theme/css/style.css

#ghp-import output/ -b gh-pages -r origin -p -n