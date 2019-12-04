How to run:

./python model.py neg_threshold level1_threshold level2_threshold level3_threshold

Where:

neg_threshold: Minumum score that a phrase will need to be classified as negative. Range: [0,0 ; 7,0]
level1_threshold: Range for level 1 of bullying psychological impact. Range: [0,0 ; 7,0]
level2_threshold: Range for level 1 of bullying psychological impact. Range: [0,0 ; 7,0]
level3_threshold: Range for level 1 of bullying psychological impact. Range: [0,0 ; 7,0]

0,0 < level1 < level2 < level3 < 7,0

Level 4 of psychological impact is on the range from level3_threshold to 7,0.

