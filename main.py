from fastai.vision.all import *

# Define the path to your data
data_path = Path('./data_upload_v3/data_upload_v3/')

tfms = [Resize(224), Normalize.from_stats(*imagenet_stats)]

dblock = DataBlock(blocks=(ImageBlock, CategoryBlock),
                   get_items=get_image_files,
                   get_y=parent_label,
                   splitter=GrandparentSplitter(train_name='train', valid_name='test'),
                   item_tfms=[ToTensor(), Resize(224)],  # Convert to tensor and resize
                   batch_tfms=[*tfms, IntToFloatTensor()])  # Normalize and convert to float tensor

dls = dblock.dataloaders(data_path, num_workers=0)

learn = vision_learner(dls, resnet34, metrics=accuracy)

learn.fine_tune(epochs=5)

# Save the trained model
# learn.export('path_to_your_model.pkl')

