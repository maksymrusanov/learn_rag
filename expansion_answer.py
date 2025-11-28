import os

import umap
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

from helper_utils import project_embeddings, word_wrap
