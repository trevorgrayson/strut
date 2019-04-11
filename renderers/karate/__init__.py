KARATE_FORMAT = """Given url '{url}'
    When method {method}
    Then status 200

"""

# And request {request}
# Then status {status_code}
# And match response == {response}


class KarateRenderer():


    @classmethod
    def _render_request(cls, request):
        # response = mk_request(request)

        return KARATE_FORMAT.format(
            url=request.url,
            request="{}",
            method=request.method.lower(),
            # request=request.
            # status_code=response.status_code,
            # response=response.text
        )


    @classmethod
    def render(cls, requests):
        return "\n".join(map(cls._render_request, requests))

