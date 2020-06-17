#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

ipynb_files=`find . -name "*.ipynb" | grep -v checkpoints`
for file in `find static -name "*.html"`
do
    outfile=`python -c "print('${file}'.replace('static/', ''))"`
    ossutil cp -u $file oss://notebook-cn/${outfile}
done
