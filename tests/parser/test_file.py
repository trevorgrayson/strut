from tests.utils import fixture

from parser import HttpRequest


class TestFile(object):

    def test_file_one(self):
        requests = HttpRequest.parse_file(fixture("file_one.http"))

        assert requests[0].method, "GET"
        assert requests[0].url, "/kittens"
        assert requests[0].headers['Content-Type'], 'application/json'
        assert requests[0].body, "{'name': 'spot', 'owner': 'data'}"

    def test_file_three(self):
        requests = HttpRequest.parse_file(fixture("file_three.http"))

        assert len(requests), 3 

        assert requests[0].method, "GET"
        assert requests[0].url, "/kittens"
        assert requests[0].headers['Content-Type'], 'application/json'
        assert requests[0].body, "{'name': 'spot', 'owner': 'data'}"


