"""Arabic text normalization for search and RAG pipelines."""

import re


def normalize_arabic(text: str) -> str:
    """Normalize Arabic text for search and matching.

    Unifies alef/hamza forms, taa marbuta, alef maqsura, removes tatweel
    and diacritics, and converts Arabic-Indic digits to ASCII.

    Normalization is lossy and intended for search/matching only.
    Do not use the output for display.
    """
    # Replace أ إ آ ٱ with ا
    text = text.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا').replace('ٱ', 'ا')
    # Replace ة with ه
    text = text.replace('ة', 'ه')
    # Replace ى with ي
    text = text.replace('ى', 'ي')
    # Remove tatweel (U+0640)
    text = text.replace('ـ', '')
    # Remove diacritics (U+064B to U+0652, plus U+0670)
    text = re.sub(r'[ً-ْٰ]', '', text)
    # Convert Arabic-Indic digits ٠-٩ to 0-9
    text = text.replace('٠', '0').replace('١', '1').replace('٢', '2').replace('٣', '3')
    text = text.replace('٤', '4').replace('٥', '5').replace('٦', '6').replace('٧', '7')
    text = text.replace('٨', '8').replace('٩', '9')
    # Collapse whitespace into one and strip edges
    text = re.sub(r'\s+', ' ', text).strip()
    return text
