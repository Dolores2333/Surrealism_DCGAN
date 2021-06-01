<p align="right">
<i>contact: mzha (at) ust(dot) hk</i>
</p>

# Surrealism_DCGAN
Reimplementation of [art-DCGAN by Robbie Barrat](https://github.com/robbiebarrat/art-DCGAN) and [Jordan Bird](https://github.com/jordan-bird/art-DCGAN-Keras) in art-dcgan-keras. 

### utils
utils is a folder for obtaining the training dataset from scratch. it is composed of:
- WikiArtScraper.py
- UrlDownload.py
- ImageProcessor.py

The dataset is scrped from WikiArt by WikiArtScraper.py and UrlDownload.py and then processed by ImageProcessor.py. The codes relies heavily on previous work down by [CHEN Huangrong](http://chenhuangrong.com/2018/10/26/2018-10-26-downloading-images-from-wikiart/)
### data
data contains the pics scraped from WikiArt for training. Traing data for each task is named after the corresponding genre, for example, surrealism. Applying ImageProcessor.py to surrealism gives us a processed imageset surrealismCroped. Images in surrealismCroped is of the same size 128*128 of RGB coding. 

### output
output stores outputs in two subfolder
- samples
- weights

## Real Surrealism Examples
![eg1](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/000.png)
![eg2](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/ascensionist-saint-cecilia.png)
![eg3](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/atrani-coast-of-amalfi-1.png)
![eg4](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/bather-1928.png)
![eg5](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/bella-in-mourillon-1926.png)
![eg6](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/bright-intervals-1928(1).png)
## Output of Day 2
![eg1](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/1622532689931.png)
![eg2](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/1622532726930.png)
![eg3](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/1622532865217.png)
![eg4](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/1622532533601.png)
![eg5](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/1622532828274.png)
![eg6](https://github.com/Dolores2333/Surrealism_DCGAN/blob/main/pics/1622532874466.png)


# Future work
- Fire the art-dcgan-keras.py to command line with genre, epoch ect. as args
- Keep training model for finer outcome in surrealism (daily updating)


