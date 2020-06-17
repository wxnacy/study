#!/usr/bin/env bash
# Author: wxnacy(wxnacy@gmail.com)
# Description:

ipynb_files=`find . -name "*.ipynb" | grep -v checkpoints`
for file in $ipynb_files
do
    outdir=`python -c "import os;print(os.path.dirname('${file}'.replace('./', './static/')))"`
    jupyter nbconvert $file --output-dir $outdir
done
