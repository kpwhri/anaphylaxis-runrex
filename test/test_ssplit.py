import pytest

from run import ssplit


@pytest.mark.parametrize('text, n_sents', [
    ('this! or that. These? No: - 1 hat, *2 coats.', 6),
])
def test_sentence_split(text, n_sents):
    sents = tuple(x[0] for x in ssplit(text))
    assert len(sents) == n_sents
    assert ''.join(sents) == text
