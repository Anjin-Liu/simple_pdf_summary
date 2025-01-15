# Simple PDF Summary Report Generation

## Demostration

- [`demo.ipynb`](demo.ipynb) - Jupyter notebook to show how the scripts works

## DevBox Setup

```
conda create -n pdf_summary python=3.10.4 ipykernel setuptools -y
conda activate pdf_summary
pip install -r requirements.txt
```

## Usage

Update your LLM token in [`./credentials/llm-cred.json`](./credentials/llm-cred.json)

```
{
  "google-api-key": "your-api-token"
}
```

Config your own ChatLLM and EmbeddingLLM in the [`./helper/project_config.py`](./helper/project_config.py)

```
ChatLLM = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    max_retries=1,
    google_api_key=llm_cred["google-api-key"],
)

EmbeddingLLM = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=llm_cred.get("google-api-key"),
)
```

Run the step scripts

```
# add current folder into python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# step 1 - extract, preprocess and segmentation
# the raw data will be save under ./data/02_extracted_raw_data/{file_name}.txt
# the preprocessed data will be saved under ./data/03_preprocessed_data/{file_name}.txt
# the segmented text will be saved under ./data/03_preprocessed_data/{file_name}_seg.txt
python -m step.s01_extract_pdf_text --file_name test_1

# step 2 - data validation (WIP)

# step 3 - indexing the segmented text and keep it into a local vector store
# the vector store will be kept under ./data/04_indexed_vector_data/{file_name}.chroma_db
python -m step.s03_llm_chunk_and_indexing --file_name test_1

# step 4 - generate summary report
# the summary report will be kept under ./data/05_report_data/{file_name}_report.md
python -m step.s04_llm_report_geneartion --file_name test_1
```

## Requirements

- internet access
- google-api-token (or your own LLM api token)
- ~16GB RAM

## Usage

1. Install requirements from [`pyproject.toml`](pyproject.toml).
2. Set paths and other config variables in [`janestreet/config.py`](janestreet/config.py).

### Scripts

- [`s01_extract_pdf_text.py`](step/s01_extract_pdf_text.py) - Step 1. extract, preprocess and segment the pdf text
- [`s02_preprocessed_data_validation.py`](step/s02_preprocessed_data_validation.py) - Step 2. (WIP) validate the preprocess text
- [`s03_llm_chunk_and_indexing.py`](step/s03_llm_chunk_and_indexing.py) - Step 3. index the chunks of the text segments into a vector store
- [`s04_llm_report_geneartion.py`](step/s04_llm_report_geneartion.py) - Step 4. retrieve related content and generate summary report
