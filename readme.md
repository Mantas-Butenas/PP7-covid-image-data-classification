# COVID-19 Image Data Classification

This project aims to classify COVID-19 and non-COVID-19 (normal) chest X-ray images using fast.ai. The dataset used in this project is the [Data Upload v3 dataset](https://www.dropbox.com/scl/fi/ajy4i9u4bjt4ho3dz4l37/data_upload_v3.zip?rlkey=kyh5oz91vykk7cao6jiip4dyn&e=1&dl=0), which consists of chest X-ray images categorized into COVID-19 positive and non-COVID-19 (normal) cases.

## Dataset
- The dataset can be downloaded from this [link](https://www.dropbox.com/scl/fi/ajy4i9u4bjt4ho3dz4l37/data_upload_v3.zip?rlkey=kyh5oz91vykk7cao6jiip4dyn&e=1&dl=0).
- Original creator of the dataset: [DeepCovid](https://github.com/shervinmin/DeepCovid).

## Installation
1. Clone the repository:

```bash
   git clone https://github.com/your_username/covid-image-classification.git
```

2. Navigate to the project directory:
```bash
cd covid-image-classification
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Training
To train the model, follow these steps:

1. Open **main.py** and modify the **data_path** variable to point to the directory where you've downloaded the dataset.
2. Run the following command to start the training process:
```bash
python main.py
```
## Testing Custom Cases
To test custom cases with the trained model:

1. Open **custom_testing.py** and modify the **path_to_your_model.pkl** variable to point to the trained model file.
2. Replace **path_to_your_image.jpg** with the path to the image you want to classify.
3. Run the following command:
```bash
python custom_testing.py
```
## Usage

To train the model or perform inference on new images, follow the instructions in the provided scripts and notebooks. Ensure you have all dependencies installed as listed in the **requirements.txt** file.

## Citation

If you use this code or the dataset in your research, please consider citing the original sources:

Minaee S, Kafieh R, Sonka M, Yazdani S, Jamalipour Soufi G. Deep-COVID: Predicting COVID-19 from chest X-ray images using deep transfer learning. Med Image Anal. 2020 Oct;65:101794. doi: 10.1016/j.media.2020.101794. Epub 2020 Jul 21. PMID: 32781377; PMCID: PMC7372265.

## License

This project is licensed under the [MIT License](LICENSE).