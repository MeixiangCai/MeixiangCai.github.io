# AI-Powered Image Classification and Automatic Organization

## Objective
Use the **Image Classification API** to automatically categorize a large set of photos and organize them into corresponding folders.

## Process
1. Retrieve the list of all images.  
2. Iterate through each image to obtain its file path.  
3. Apply **advancedGeneral** from **AipImageClassify** to classify the image.  
4. Generate a folder name based on the classification result.  
5. Move the image to the target folder.  
6. For images with the same classification result, move them into the already created folder.  

- The folder **“项目”** contains previously classified images. You may delete the corresponding folders to practice automatic classification.  
