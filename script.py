from scannerpy import Database, DeviceType
from scannerpy.stdlib import NetDescriptor, parsers, bboxes
import os
import subprocess
import cv2
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import util
##NEW MODULES ADDED BY JEN
from scipy.misc import imread, imsave, imresize
util.download_video()

with Database() as db:

    # TODO(wcrichto): comment the demo. Make the Scanner philosophy more clear.
    # Add some figures to the wiki perhaps explaining the high level

    descriptor = NetDescriptor.from_file(db, 'nets/caffe_facenet.toml')
    facenet_args = db.protobufs.FacenetArgs()
    facenet_args.threshold = 0.5
    caffe_args = facenet_args.caffe_args
    caffe_args.net_descriptor.CopyFrom(descriptor.as_proto())
    caffe_args.batch_size = 5

    table_input = db.ops.Input()
    print(table_input)
    facenet_input = db.ops.FacenetInput(
        inputs=[(table_input, ["frame", "frame_info"])],
        args=facenet_args,
        device=DeviceType.GPU)
    facenet = db.ops.Facenet(
        inputs=[(facenet_input, ["facenet_input"]), (table_input, ["frame_info"])],
        args=facenet_args,
        device=DeviceType.GPU)
    facenet_output = db.ops.FacenetOutput(
        inputs=[(facenet, ["facenet_output"]), (table_input, ["frame_info"])],
        args=facenet_args)
"""
    if not db.has_table('example'):
        print('Ingesting video into Scanner ...')
        db.ingest_videos([('example', "/n/scanner/datasets/kcam/20150207_154033_788.mp4")], force=True)

    sampler = db.sampler()
    print('Running face detector...')
    outputs = []
    for scale in [0.5]:
        print('Scale {}...'.format(scale))
        facenet_args.scale = scale
        tasks = sampler.all([('example', 'example_faces_{}'.format(scale))],
                            item_size=50)
        [output] = db.run(tasks, facenet_output, force=True, work_item_size=5)
        outputs.append(output)

    all_bboxes = [
        [box for (_, box) in out.load(['bboxes'], parsers.bboxes)]
        for out in outputs]
    #print("printing all_bboxes[0][0]....\n")
    #print(all_bboxes[0][0])
    nms_bboxes = []
    frames = len(all_bboxes[0])
    runs = len(all_bboxes)
    #print("length of all_bboxes...")
    #print(runs)
    #print("length of all_bboxes[0]...")
    #print(frames)
    for fi in range(frames):
        frame_bboxes = []
        for r in range(runs):
            frame_bboxes += (all_bboxes[r][fi])
        frame_bboxes = bboxes.nms(frame_bboxes, 0.3)
        nms_bboxes.append(frame_bboxes)

    print('Extracting frames...')
    video_faces = nms_bboxes
    video_frames = [f[0] for _, f in db.table('example').load(['frame'])]
    #print(video_frames)
    #print(video_frames[0])
    #print(video_frames[0][0])
    #print(video_frames[0][0][0])  
    
    print("number of images: ")
    print(len(video_frames))
    print("number of row pixels: ")
    print(len(video_frames[0][0]))
    print("number of column pixels: ")
    print(len(video_frames[0][0][0]))'''
    #looping through all images
	#    list = []
    	#	count = 0
    	#demo_image_list = video_frames[0:10]
    	#demo_bbox_list = video_faces[0:10]  
    #for frame in demo_image_list:
    #    imsave("frames/frame%d.jpg"%count, frame)
    #    count+=1
    diction = dict()
    multlists = []
    for i in range(len(demo_bbox_list)):
	s = str(demo_bbox_list[i][0])
	print("demo_bbox_list: ", s)
	L = s.split()
	print(L)
	
	d = dict()
	d["x1"] = round(float(L[1]))
	#print(d["x1"])
	d["y1"] = round(float(L[3]))
	x2 = round(float(L[5]))
	y2 = round(float(L[7]))
	d["height"] = abs(d["y1"] - y2)
	d["width"] = abs(d["x1"] - x2)
	d["correct"] = "no answer"
	d["label"] = "face"
	multlists.append(d)
    diction["myimages"] = multlists
    print("Writing to pixel array file...")
    g = open("pixelarray.txt", "w+")
    for i in range(frame_shape[0]):
	for j in range(frame_shape[1]):
	    g.write(str(demo_image_list[i][j]))
    g.close()"""
'''print("Writing to bbox file...")
    f = open("bbox.txt", "w+")
    f.write(str(diction))
    f.close()
    '''
"""print('Writing output video...')
    frame_shape = video_frames[0].shape
    output = cv2.VideoWriter(
        'example_faces.mkv',
        cv2.VideoWriter_fourcc(*'X264'),
        24.0,
        (frame_shape[1], frame_shape[0]))

    for (frame, frame_faces) in zip(demo_image_list, demo_bbox_list):#video_frames, video_faces):
        for face in frame_faces:
            if face.score < 0.5: continue
            cv2.rectangle(
                frame,
                (int(face.x1), int(face.y1)),
                (int(face.x2), int(face.y2)),
                (255, 0, 0), 3)
        output.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    print("examples_faces.mkv-->directory of images")
"""    
"""vidcap = cv2.VideoCapture('example_faces.mp4')
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
  	(success,image) = vidcap.read()
  	print( 'Read a new frame: ', success)
  	cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  	count += 1
"""
