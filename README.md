# struct

Using the HTTP formatting standard to define web endpoints.

The Swagger/OpenAPI specifications are generally ubiquitous and extremely useful.  The 
difficulty comes in when having to remember the fieldnames exactly, or how the document
is structured.  Required fields lead to a lot of noise when compiling them.

It is the purpose of this specification to make defining HTTP endpoints much easier by 
making a more intuitive entry system.  By minimizing format and structure, and by leveraging
the HTTP standard (which may already be known by the developer) it may be quicker and easier
to define APIs.


## Documenting

By generating [Swagger](https://swagger.io/) yaml/json this project can tap into a rich
community of GUI definitions

## Testing

This format should lead to be able to infer standard [Gherkin Syntax](https://docs.cucumber.io/gherkin/)
tests, that could automatically generate testing.

## Code Generation

By compiling down to Swagger code, server code can be generated.  See an example implementation on 
[editor.swagger.io/](http://editor.swagger.io/) under the "Generate Server" tab.


## Sources

### Reading `.http` Files

By adding standard HTTP Messages (as defined by [rfc2616](https://tools.ietf.org/html/rfc2616)) with each separated by 
?double newline? characters (like between headers and bodies), that file can be read in to get an `list` of `HttpRequest`
objects.

```
from parser import HttpRequest

requests = HttpRequest.parse_file("filename.http")
```

### Spec Aggregation as a Service

By setting up a web service locally, you can use a web browser, curl, Postman, or any other
HTTP client to hit your local webservice, and accumlate a specification.  The can be saved to a file
for reusability.


## Project

### Testing the Project

```
pytest
```

