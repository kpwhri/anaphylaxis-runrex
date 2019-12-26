import re

from runrex.main import process
from runrex.schema import validate_config

from anaphylaxis_nlp.algo.epinephrine import get_epinephrine
from anaphylaxis_nlp.algo.primary_dx import get_anaphylaxis_dx
from anaphylaxis_nlp.algo.sudden import get_suddenness


def main(config_file):
    conf = validate_config(config_file)
    algorithms = {
        'dx': get_anaphylaxis_dx,
        'sudden': get_suddenness,
        'epinephrine': get_epinephrine,
    }
    process(**conf, algorithms=algorithms, ssplit=ssplit)


def ssplit(text):
    text = '  '.join(text.split('\n'))  # join broken lines
    for sentence in re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|\*)\s', text):
        yield from (sent for sent in re.split(r'[*•-]', sentence))


if __name__ == '__main__':
    import sys

    try:
        main(sys.argv[1])
    except IndexError:
        raise AttributeError('Missing configuration file: Usage: run.py file.(json|yaml|py)')
