import glob
import os
import tensorflow as tf
import sys


# Link to directories; 
image_dir = sys.argv[1] # Where we have images

# Find the categories
images = glob.glob(image_dir+"*")
images = sorted([x.replace(image_dir,'') for x in images])
print("images are: ", images)

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("labels.txt")]

with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')



with tf.Session() as sess:

    for image in images:
        image_path = image_dir + image
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()

        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
        
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        print("\n", image_path)
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, score))
        

        filename = "tmp/results_testing_function.txt"    
        with open(filename, 'a+') as f:
            f.write('\n**%s**\n' % (image_path))
            for node_id in top_k:
                human_string = label_lines[node_id]
                score = predictions[0][node_id]
                f.write('%s (score = %.5f)\n' % (human_string, score))

