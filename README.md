# Detection-of-Watch
This project is based on detection of watch with help of OpenCV with Python (using self trained Haar Cascade .xml file) 

About the Project :

As I mentioned above that i have used self trained cascade(.xml) files 
so, The steps to build our own cascade file are as below:
 1) collect the dataset used for training the cascade (both positive and negative images)
 2) create seperate folder for positive and negative images and name them 'p' and 'n' respectively
 3) install Cascade-Trainer-GUI (http://amin-ahmadi.com/cascade-trainer-gui/) on your system and train the cascade by specifying values to the parameters in it
  that includes path to the dataset etc.
 4) Then start the training
 
 I collected the dataset and trained with help 'Cascade-Trainer-GUI' trainer 
The parameters of my cascade (some of them given as input and rest are generated while training the cascade) includes :

cascadeDirName: C:\Users\rajen\Desktop\OpenCV Project\classifier
vecFileName: C:\Users\rajen\Desktop\OpenCV Project\pos_samples.vec
bgFileName: C:\Users\rajen\Desktop\OpenCV Project\neg.lst
numPos: 51
numNeg: 1000
numStages: 10
precalcValBufSize[Mb] : 1024
precalcIdxBufSize[Mb] : 1024
acceptanceRatioBreakValue : -1
stageType: BOOST
featureType: HAAR
sampleWidth: 32
sampleHeight: 32
boostType: GAB
minHitRate: 0.995
maxFalseAlarmRate: 0.5
weightTrimRate: 0.95
maxDepth: 1
maxWeakCount: 100
mode: BASIC
Number of unique features given windowSize [32,32] : 510112
 
After the successful completion of the training ( which went around 4 to 5 hours) ,cascade was generated which i named it as "watch_cascade"
Then I coded using OpenCV (library) in python and used this trained cascade "watch_cascade" for detecting and testing it on test images
The dataset of Positive and Negative images, watch_cascade(.xml) file , code and test image were added to this repository
 
 
# Why Cascade-Trainer-GUI for training ??
Though there are other methods for training the cascade , I used Cascade-Trainer-GUI(application) for training my cascade because it user friendly i.e we can simply install this application on our system and train the cascade by specifying some parameter and few clicks , whereas other methods involves mounting the dataset from local machine to global machine ,etc which are complex and after many hours of training it is not guaranteed that the cascade will build successfully


CONCLUSION :
With help of self trained cascade file along with OpenCV with Python I successfully detected the watch in the test image.
We can also detect  watches in the vedio files and real time (using the webcams).
    
