"""_summary_

Returns:
    _type_: _description_
"""

from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import TextSplitter


class CustomDelimiterTextSplitter(TextSplitter):
    def __init__(
        self,
        delimiter: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.delimiter = delimiter
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text: str):
        # Split the text by the custom delimiter
        splits = text.split(self.delimiter)

        # Merge chunks back to fit within chunk_size with chunk_overlap
        chunks = []
        current_chunk = ""
        for split in splits:
            if len(current_chunk) + len(split) + len(self.delimiter) <= self.chunk_size:
                current_chunk += split + self.delimiter
            else:
                chunks.append(current_chunk.strip(self.delimiter))
                current_chunk = split + self.delimiter

        if current_chunk:
            chunks.append(current_chunk.strip(self.delimiter))

        return chunks


def index_text_to_chroma(
    seg_text,
    embedding_llm,
    vectorestore_path,
):

    # Define the Text Splitter with custom delimiter
    text_splitter = CustomDelimiterTextSplitter(
        delimiter="-" * 49,
        chunk_size=1000,
        chunk_overlap=100,
    )

    # Split text into chunks
    chunks = text_splitter.split_text(seg_text)

    # Convert chunks to langchain_core Documents
    langchain_documents = [
        Document(page_content=chunk, metadata={"chunk_index": i})
        for i, chunk in enumerate(chunks)
    ]

    # Store chunks into Chroma
    vectorestore = Chroma(
        embedding_function=embedding_llm,
        persist_directory=vectorestore_path,
    )
    vectorestore.add_documents(langchain_documents)

    # Save the database
    vectorestore.persist()

    print(f"Indexed {len(chunks)} chunks into Chroma database '{vectorestore_path}'")
