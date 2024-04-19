# sentiment_analysis_of_kannada_product_reviews

Python Version: 3.11.9
Docker 

Dataset link: https://huggingface.co/datasets/ai4bharat/IndicSentiment/viewer/translation-kn/validation
              https://huggingface.co/datasets/ai4bharat/IndicSentiment/viewer/translation-kn/test

Bert model: bert-base-multilingual-cased


Steps to run project:
Step 1: Train model (main.ipynb), and save model in app/trained_model directory.
Step 2: edit "app/credentials.toml", add your docker email.
Step 3: Open terminal in app directory and run the following commands:
> docker build -t sentiment-analysis-app .
> docker run -p 80:80 sentiment-analysis-app
View frontend at http://localhost:80 
