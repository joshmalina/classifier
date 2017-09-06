#!/bin/bash
# Basic while loop

for a in 0.01 0.04 0.05 0.07 0.09
do for b in 5 10 15
do
  echo BEGIN
  echo learning rate "$a"
  echo num epochs "$b"
  /Users/joshuamalina/opt/devel/src/fastText/fasttext supervised -epoch $b -input movies.preprocessed.train -output model.movies -wordNgrams 2 -lr $a
  /Users/joshuamalina/opt/devel/src/fastText/fasttext test model.movies.bin movies.preprocessed.valid
  echo $END
done
done
