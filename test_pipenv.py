import pytest

import pipenv.utils



def test_convert_deps_to_pip():

    # requests = '*'
    deps = {'requests': '*'}
    deps = pipenv.utils.convert_deps_to_pip(deps)
    assert deps[0] == 'requests'

    # requests = {}
    deps = {'requests': {}}
    deps = pipenv.utils.convert_deps_to_pip(deps)
    assert deps[0] == 'requests'

    # requests = { extras = ['socks'] }
    deps = {'requests': {'extras': ['socks']}}
    deps = pipenv.utils.convert_deps_to_pip(deps)
    assert deps[0] == 'requests[socks]'

    # Django = '>1.10'
    deps = {'django': '>1.10'}
    deps = pipenv.utils.convert_deps_to_pip(deps)
    assert deps[0] == 'django>1.10'

    # pinax = { git = 'git://github.com/pinax/pinax.git', ref = '1.4', editable = true }
    deps = {'pinax': {'git': 'git://github.com/pinax/pinax.git', 'ref': '1.4', 'editable': True}}
    deps = pipenv.utils.convert_deps_to_pip(deps)
    assert deps[0] == '-e git+git://github.com/pinax/pinax.git@1.4 --egg=pinax'


def test_convert_from_pip():

    # requests
    dep = 'requests'
    dep = pipenv.utils.convert_deps_from_pip(dep)
    assert dep == {'requests': '*'}

    # Django>1.10
    dep = 'Django>1.10'
    dep = pipenv.utils.convert_deps_from_pip(dep)
    assert dep == {'Django': '>1.10'}

    # requests[socks]
    dep = 'requests[socks]'
    dep = pipenv.utils.convert_deps_from_pip(dep)
    assert dep == {'requests': {'extras': ['socks']}}

    # TODO: -e git+git://github.com/pinax/pinax.git@1.4


