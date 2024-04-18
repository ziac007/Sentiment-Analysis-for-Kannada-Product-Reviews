from datasets import load_dataset
import pandas as pd

# Load the dataset with the specific configuration for Kannada translation
dataset = load_dataset("ai4bharat/IndicSentiment", "translation-kn")

# Access the entire dataset (let's assume you want the validation split)
complete_dataset = dataset['test']

# Convert dataset to pandas DataFrame
df = pd.DataFrame(complete_dataset)

# Save as CSV
csv_file = "dataset_test.csv"
df.to_csv(csv_file, index=False)

print("Dataset saved as CSV:", csv_file)
