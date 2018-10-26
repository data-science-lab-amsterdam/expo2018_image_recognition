#Linux retraining command
python src/retrain.py \
--bottleneck_dir=tmp/bottlenecks \
--how_many_training_steps=30 \
--model_dir=tmp/model_dir \
--output_graph=tmp/retrained_graph.pb \
--output_labels=tmp/retrained_labels.txt \
--summaries_dir=tmp/retrain_logs \
--image_dir=images-cropped

#Windows retraining command
#python retrain.py --bottleneck_dir=bottlenecks --how_many_training_steps 500 --model_dir=model_dir --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --summaries_dir=retrain_logs --image_dir=images