import yaml

EXPECTED_KEYS = set(["aws_access_key", "aws_secret_key", "bucket"])


def read_config(filename):
    with open(filename) as f:
        config = yaml.load(f)
    if set(config.keys()) != EXPECTED_KEYS:
        raise Exception(
            'Invalid config file: expecting keys %s' % EXPECTED_KEYS)
    return config
