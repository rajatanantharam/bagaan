# Bagaan (বাগান) 
Bagaan uses [local binary patterns](https://en.wikipedia.org/wiki/Local_binary_patterns) for classifying an image. Then it uses supervised machine learning with [LinearSVC](https://en.wikipedia.org/wiki/Support_vector_machine) to predict if a given image is a garden or not. 

#Requires 
- OpenCV 3.0
- python 2.7 
- [scikit-learn](http://scikit-learn.org/stable/)

#Configure
create folders in root
- images/testing
- images/training/garden
- images/training/notgarden

Get a set of training sets (more the merrier) [There's a lot here](http://groups.csail.mit.edu/vision/SUN/) and have them available in the folder garden & notgarden 

Put the images you wanna test in the testing folder 

#Usage 
python bagaan.py -t images/training/ -e images/testing/
