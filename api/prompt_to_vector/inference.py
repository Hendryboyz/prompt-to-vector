from sentence_transformers import SentenceTransformer
import logging
import os
from config import Settings

class TextEncoder:
    def __init__(self):
        settings = Settings()
        self.model_path = settings.p2v_model_path
        if os.path.isdir(self.model_path) == False:
            self.model_path = 'Alibaba-NLP/gte-large-en-v1.5'
        self.model = SentenceTransformer(
            model_name_or_path=self.model_path,
            trust_remote_code=True,
        )
        self.logger = logging.getLogger('text-encoder')
        self.logger.info(f'Encoder started, load model from: {self.model_path}')

    def encode_sentences(
        self,
        sentences: list[str],
        batch_size: int = 512,
        normalize: bool = True, 
        verbose: bool = False
    ):
        sentence_embeddings = self.model.encode(
            sentences,
            batch_size=batch_size,
            show_progress_bar=verbose,
            normalize_embeddings=normalize,
        )
        
        return sentence_embeddings

