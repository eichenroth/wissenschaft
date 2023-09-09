from typing import Any, Generator

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS

from common import ASSET_PATH, INDEX_NAME


def load_pdf_pages() -> Generator[Document, Any, None]:
  paths = ASSET_PATH.glob('*.pdf')

  for path in paths:
    loader = PyPDFLoader(str(path))
    pages = loader.load_and_split()
    for page in pages:
      yield page


if __name__ == '__main__':
  pages = list(load_pdf_pages())
  faiss = FAISS.from_documents(pages, OpenAIEmbeddings())

  faiss.save_local(ASSET_PATH, INDEX_NAME)
