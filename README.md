# strut

Using the HTTP formatting standard to define web endpoints.

The Swagger/OpenAPI specifications are generally ubiquitous and extremely useful.  The 
difficulty comes in when having to remember the fieldnames exactly, or how the document
is structured.  Required fields lead to a lot of noise when compiling them.

It is the purpose of this specification to make defining HTTP endpoints much easier by 
making a more intuitive entry system.  By minimizing format and structure, and by leveraging
the HTTP standard (which may already be known by the developer) it may be quicker and easier
to define APIs.


## Features

### Documenting

By generating [Swagger](https://swagger.io/) yaml/json this project can tap into a rich
community of GUI definitions.

### Testing

This format should lead to be able to infer standard [Gherkin Syntax](https://docs.cucumber.io/gherkin/)
tests, that could automatically generate testing.

```
./bin/strut gherkin definition.http
```

### Code Generation

By compiling down to Swagger code, server code can be generated.  See an example implementation on 
[editor.swagger.io/](http://editor.swagger.io/) under the "Generate Server" tab.

```
./bin/strut swagger definition.http
```

### Web Scripting

`http` files can describe a procedural list of requests to make to a webserver. 
This can be used to script requests to a service, potentially multiple services 
in future iterations.

### Scripts

To convert a `.http` file into a swagger document:

```
# yaml
./bin/strut swagger filename.http

# json 
./bin/strut swagger-json filename.http

```

TODO FTL to convert between formats?

### Definitions

#### `.http` Files

`.http` files are composed of a collection of HTTP Messages, which can be used 
to describe a service.  Standard HTTP Messages (as defined by 
[rfc2616](https://tools.ietf.org/html/rfc2616)) with each separated by 
?double newline? characters (in the same way as headers and bodies are 
separated), that file can be read in as a `list` of `HttpRequest` objects.

```
from parser import HttpRequest

requests = HttpRequest.parse_file("filename.http")
```

### Spec Aggregation as a Service

By setting up a web service locally, you can use a web browser, curl, Postman, 
or any other HTTP client to hit your local webservice, and accumulate a 
specification.  This can be saved to a `.http` formatted file for reusability.


## Project Life Cycle

### Testing the Project

```
pytest
```

