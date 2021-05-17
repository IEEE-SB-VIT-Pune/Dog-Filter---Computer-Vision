Computer Vision not only plays a pivotal role in a lot of modern day Artificial Intelligence Systems but also is the basis for a lot of stand alone systems like Object detection and the Face-unlock system on our phones! Another great example can be Snapchat and Instagram filters. So its safe to say that Social Media owes a lot of its popularity to Computer Vision. With this project, we plan to accomplish the very famous dog ears filter. The code provided is extremely flexible and user-friendly and can be found in the "Source code" folder. Once downloaded on your local system, you can run it on other filters too and perfectly configure your filter to your face by calibrating the values of the two scale variables in the code.

We would be writing our code in Python so please ensure that Python is already downloaded in your system.

<h2><b> Resources used </b></h2>

There will be two external files you will primarily need to build this project:
1. Haar Cascade files: Haar Cascade is an openCV algorithm which is used to detect an array of objects, smiles and eyes to mention a few alongside faces. In our project, we will be using it just for face detection. However, feel free to explore all the xml files by trying to detect all the objects that the model can detect. 
2. Image of the filter: We will be using the Dog ears filter but that is only restricted to this project. Please go ahead and experiment with different types of filters.

Both these files can be found in the folder labeled "Resources."

<h2><b> File setup </b></h2>

Instructions for setting up the Haar Cascade files:
1. Download the archived folder containing the Haar cascade files. It will be named as "haar-cascade-files-master.zip" in the resources folder.
2. In a terminal, type "pip install opencv-python" to donwload the opencv library. 
3. Navigate your way to where you have installed Python. Once in the folder, find the folder named "Lib", within Lib find "site-packages" which should contain a "cv2" folder. This is where you need to download and extract the Haar Cascade files. Follow: Python folder -> Lib -> site-packages -> cv2
4. Once the xml files are successfully extracted and placed in the shown directory, open the folder and move to the folder which shows all the xml files. This is the path you can copy to load your model in your python code

Note: The "cv2" folder in site-packages referred to in the second point will only be found if you have successfully installed openCV. 


Once you are able to setup the haar cascade files in the specified directory, you can use them in any code you want. Another thing to note is that the image used as filter needs to be in the working directory of the python file you are coding in. If not make sure you pass its exact location path as the parameter in the imread() function. If all the mentioned instructions are followed, the code should run smoothly right in the first go and that should leave you free to immediately experiment on the code by using filters of your own choice.
