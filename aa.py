print('--------------------\nStarting the script\n--------------------')

# Importing url,setting
import json
with open('urls.json') as fileUrls:
	dataUrls = json.load(fileUrls)
with open('setting.json') as fileSetting:
	dataSetting = json.load(fileSetting)
rows = int(dataSetting['rows'])
cols = int(dataSetting['cols'])
imageWidth = int(dataSetting['imageWidth'])
imageHeight = int(dataSetting['imageHeight'])
print('rows=%d , cols=%d'%(rows,cols))

import urllib.request
from PIL import Image

ind = 1
totalWidth = rows*imageWidth
totalHeight = cols*imageHeight
newImage = Image.new('RGB',(totalWidth,totalHeight))
posLeft = 0
posTop = 0

for data in dataUrls:	
	# download Image
	print('Merging %s'%data['url'])
	imageFile = open('temp','wb')
	imageFile.write(urllib.request.urlopen(data['url']).read())
	imageFile.close()	
	
	# resize Image
	imageFile_ = Image.open('temp')
	imageFile__ = imageFile_.resize((imageWidth, imageHeight))
	
	# merging Image
	newImage.paste(imageFile__,(posLeft,posTop))
	
	# if filled not need go ahead
	if(ind%rows==0):
		posLeft = 0
		posTop += imageHeight
	else:
		posLeft += imageWidth
	if(ind == rows*cols): break
	ind+=1

import os
newImage.save('result.jpg')
os.remove('temp')

print('--------------------\nEnd of script\n--------------------')
