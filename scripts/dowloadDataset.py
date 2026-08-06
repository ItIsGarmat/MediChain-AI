import kagglehub

print("Downloading dataset...")

path = kagglehub.dataset_download(
    "ranitroy2005/brain-tumor-ct-and-mri-dataset-tumor-vs-healthy"
)

print("Download completed!")
print("Dataset path:", path)