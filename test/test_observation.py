import pytest
from runrex.algo.pattern import Document

from anaphylaxis_nlp.algo.observation import OBSERVATION, MONITORING, get_observation, ObsStatus


@pytest.mark.parametrize('text', [
    'admit overnight',
    'admit for observation',
    'transferred to main hospital for monitoring',
    'transfered to icu',  # intentional misspelling
])
def test_observation(text):
    assert OBSERVATION.matches(text)


@pytest.mark.parametrize('text', [
    'close monitoring',
])
def test_monitoring(text):
    assert MONITORING.matches(text)


def test_get_observation():
    sent = 'We will admit him for further observation.'
    doc = Document('name', text=sent)
    res = next(get_observation(doc))
    assert res.value == ObsStatus.OBSERVATION.name
    assert res.text == sent
