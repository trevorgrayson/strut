from renderers.swagger import SwaggerJsonRenderer, SwaggerYamlRenderer
from renderers.karate import KarateRenderer


def swagger_json(requests):
    return SwaggerJsonRenderer.render(requests)

def swagger_yaml(requests):
    return SwaggerYamlRenderer.render(requests)

def gherkin(requests):
    raise NotImplementedError("Coming soon!")

def karate(requests):
    return KarateRenderer.render(requests)

ACTIONS = {
  'swagger': swagger_yaml,
  'swagger-yaml': swagger_yaml,
  'swagger-json': swagger_json,
  'gherkin': gherkin,
  'karate': karate
}

