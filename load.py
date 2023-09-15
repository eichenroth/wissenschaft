import time
from typing import Any, Generator, List

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS

from common import ASSET_PATH, INDEX_NAME


def load_document_pages() -> Generator[List[Document], Any, None]:
  paths = list(str(path) for path in ASSET_PATH.glob('**/*.pdf'))
  paths.sort()

  for path in paths:
    print(path)
    loader = PyPDFLoader(path)
    yield loader.load_and_split()


if __name__ == '__main__':
  faiss = None
  
  for document_pages in load_document_pages():
    if faiss is None:
      faiss = FAISS.from_documents(document_pages, OpenAIEmbeddings())

      faiss.index
    else:
      faiss.add_documents(document_pages)
    time.sleep(0.001)

  faiss.save_local(ASSET_PATH, INDEX_NAME)
