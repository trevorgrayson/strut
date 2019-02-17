from renderers.swagger import SwaggerRenderer


def swagger_json(requests):
    return SwaggerRenderer.json(requests)

def swagger_yaml(requests):
    return SwaggerRenderer.yaml(requests)

def gherkin(requests):
    raise NotImplementedError("Coming soon!")

ACTIONS = {
  'swagger': swagger_yaml,
  'swagger-yaml': swagger_yaml,
  'swagger-json': swagger_json,
  'gherkin': gherkin
}

