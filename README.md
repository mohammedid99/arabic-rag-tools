# arabic-rag-tools

Text normalization for Arabic search and RAG pipelines.

## The problem

Standard text pipelines treat these as different words:

| Written | Also written |
|---|---|
| أحمد | احمد |
| مكتبة | مكتبه |
| مـكـتـبـة | مكتبة |
| ٢٠٢٦ | 2026 |
| مَكْتَبَة | مكتبة |

A user searching for `أحمد` will not find documents containing `احمد`.
In a RAG pipeline this looks like the model "not knowing" the answer,
when in fact retrieval never returned the right chunk.

## Install

```bash
git clone https://github.com/USERNAME/arabic-rag-tools.git
cd arabic-rag-tools
```

## Usage

```python
from arabic_rag_tools.normalize import normalize_arabic

normalize_arabic("الـمَكْتَبَة رقم ٥")
# 'المكتبه رقم 5'

normalize_arabic("أحمد إبراهيم")
# 'احمد ابراهيم'
```

Normalize both your documents and the incoming query with the same
function, so the two sides match.

## What it does

- Unifies alef forms: `أ إ آ ٱ` to `ا`
- Unifies `ة` to `ه` and `ى` to `ي`
- Removes tatweel (U+0640)
- Removes diacritics (U+064B–U+0652, U+0670)
- Converts Arabic-Indic digits `٠-٩` to `0-9`
- Collapses whitespace

Latin text, numbers and filenames pass through untouched.

## Note

Normalization is lossy: `على` and `علي` both become `علي`.
Use it for search and matching, not for display.

## Tests

```bash
pip install pytest
pytest
```

## Roadmap

- [x] Text normalization
- [ ] Arabic sentence splitting (`؟ ؛ .` and Arabic full stop)
- [ ] Chunking with sentence-boundary awareness
- [ ] Retrieval benchmark: normalized vs raw

## License

MIT
