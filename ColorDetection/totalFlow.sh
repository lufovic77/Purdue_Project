#!/bin/bash
echo "enter src image path"
read src_image
echo "enter sigma value for noise"
read sigma
./BM3D/BM3Ddenoising $src_image $sigma ImNoisy.png ImBasic.png ImDenoised.png ImDiff.png ImBias.png \
ImDiiffBias.png 1 dct 1 dct 1 rgb
mv *png noiseRet


 
