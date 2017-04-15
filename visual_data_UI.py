import json
import glob
#Static values
JSONFILENAME = "visual_data_UI.js"
BBOX_FILENAME = "bbox.txt"


jpegArray = [
"frame0.jpg",
"frame1.jpg",
"frame2.jpg",
"frame3.jpg",
"frame4.jpg",
"frame5.jpg",
"frame6.jpg",
"frame7.jpg",
"frame8.jpg",
"frame9.jpg"
]

###making dummy data array###
def makeArray(List, labelVal, correctVal):
	result=[]
	f = open(BBOX_FILENAME, "r")
	bbox_arr = f.read()
	bbox_arr = bbox_arr.split("\n")
	print(bbox_arr)
	for (i, bbox) in zip(List, bbox_arr):
		diction = dict()
		diction["jpeg_file"] = i
		diction["label"] = labelVal
		diction["correct"] = correctVal
		diction["x1"] = 5
		diction["y1"] = 5
		diction["width"] = 50
		diction["height"] = 50
		result.append(diction)
	return result

print(makeArray(jpegArray, "face", "no answer"))

###write dummy data array to .js file###
def writeToFile(array, filename):
	s = json.dumps(makeArray(array, "coffee", "no answer"))
	L = glob.glob(filename)
	if len(L)==0:
		print(filename + " doesn't exist.")
		f=open(filename, "w+")
		f.write("{myimages=" + s)
		f.close
	elif len(L)==1:
		print(filename + " exists!")
		f = open(filename, "r")
		if f.mode =='r':
			content = f.read()
			if len(content)>0: 
				content = content[:-1]
		f.close
		f = open(filename, "w+")
		if len(content)>0:
			f.write(content+ ",\n" + s[1:]+"}")
		else:
			f.write("{myimages=" + s+"}")
		f.close
	else:
		print("error: more than one "+ filename + " file.")

#writeToFile(jpegArray, "visual_data_UI.json")














