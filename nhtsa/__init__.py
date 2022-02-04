import functools
import json

import requests
from django.core.cache import cache

API_URL = "https://vpic.nhtsa.dot.gov/api/"


def _cache_result(f):
    @functools.wraps(f)
    def wrapper(arg):
        sentinel = object()
        result = cache.get(arg, sentinel)
        if result is not sentinel:
            return result
        result = f(arg)
        cache.set(arg, result)
        return result

    return wrapper


class NHTSAError(Exception):
    pass


@_cache_result
def _models_for_make(make):
    try:
        results = requests.get(
            API_URL + f"vehicles/getmodelsformake/{make.lower()}?format=json",
            timeout=5,
        ).json()["Results"]
    except (
        ConnectionError,
        requests.Timeout,
        json.JSONDecodeError,
        KeyError,
    ) as err:
        raise NHTSAError from err
    try:
        return set(result["Model_Name"] for result in results)
    except KeyError as err:
        raise NHTSAError from err


def make_exists(make):
    return len(_models_for_make(make)) > 0


def model_exists(make, model):
    if not make_exists(make):
        return False
    return model in _models_for_make(make)
