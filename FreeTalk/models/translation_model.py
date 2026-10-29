
import torch

from transformers import (
    M2M100ForConditionalGeneration,
    M2M100Tokenizer
)


class TranslationModel:
    """
    Translate text between languages using M2M100.
    """

    def __init__(self, model_name="facebook/m2m100_418M"):
        """
        Load the pretrained model and its tokenizer.

        The model is downloaded on first use and
        cached locally for future runs.
        """

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.tokenizer = M2M100Tokenizer.from_pretrained(
            model_name
        )

        self.model = M2M100ForConditionalGeneration.from_pretrained(
            model_name
        ).to(self.device)

        self.model.eval()


    def translate(self, text, source_language, target_language):
        """
        Translate text into a selected language.

        Args:
            text (str):
                Original message.

            source_language (str):
                Source language code, such as "en".

            target_language (str):
                Target language code, such as "es".

        Returns:
            str:
                Translated message.
        """

        self.tokenizer.src_lang = source_language

        encoded = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=256
        ).to(self.device)

        with torch.inference_mode():
            output = self.model.generate(
                **encoded,
                forced_bos_token_id=self.tokenizer.get_lang_id(
                    target_language
                ),
                max_new_tokens=256
            )

        return self.tokenizer.batch_decode(
            output,
            skip_special_tokens=True
        )[0]
