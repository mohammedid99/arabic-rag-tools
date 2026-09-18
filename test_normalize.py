from arabic_rag_tools.normalize import normalize_arabic


def test_tatweel():
    assert normalize_arabic("مـــكـــتـــبـــة") == "مكتبه"


def test_hamza_forms():
    assert normalize_arabic("أحمد إبراهيم آمن ٱلله") == "احمد ابراهيم امن الله"


def test_diacritics():
    assert normalize_arabic("مَكْتَبَةٌ") == "مكتبه"


def test_superscript_alef():
    assert normalize_arabic("هَٰذَا") == "هذا"


def test_arabic_indic_digits():
    assert normalize_arabic("سنة ٢٠٢٦") == "سنه 2026"


def test_whitespace():
    assert normalize_arabic("  كلمة\t\nكلمة  ") == "كلمه كلمه"


def test_alef_maqsura():
    assert normalize_arabic("مستشفى") == "مستشفي"


def test_latin_untouched():
    assert normalize_arabic("الملف report.pdf رقم ٣") == "الملف report.pdf رقم 3"


def test_empty():
    assert normalize_arabic("") == ""


def test_only_whitespace():
    assert normalize_arabic("   ") == ""
