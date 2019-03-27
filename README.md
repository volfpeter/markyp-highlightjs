# markyp-highlightjs

Highlight.js-based syntax highlighting for web pages built with [markyp-html](https://github.com/volfpeter/markyp-html).

## Installation

The project is listed on the Python Package Index, it can be installed simply by executing `pip install markyp-highlightjs`.

## Getting started

The following code shows the creation of a simple webpage that displays syntax highlighted Python code. There are three things to note in the example:

- The selected theme (CSS) is added to the head of the document.
- The syntax highlighted code is created using the `highlight()` method.
- The JavaScript code that imports and initializes Highlight.js is added to the `javascript` section of the page.

```Python
from markyp_html import webpage
from markyp_highlightjs import js, themes, highlight

code = "\n".join([
    "from markyp_html import webpage",
    "from markyp_highlightjs import js, themes, highlight",
    "page = webpage(",
    "    highlight(\"import antigravity\", language=\"python\"),",
    "    page_title=\"markyp-highlightjs demo page\",",
    "    head_elements=[themes.darcula],",
    "    javascript=js.js",
    ")",
    "",
    "print(page)"
])

page = webpage(
    highlight(code, language="python"),
    page_title="markyp-highlightjs demo page",
    head_elements=[themes.monokai],
    javascript=js.js
)

print(page)
```

For more details on how this package works, please see [markyp](https://github.com/volfpeter/markyp) and [markyp-html](https://github.com/volfpeter/markyp-html).

## Community guidelines

In general, please treat each other with respect and follow the below guidelines to interact with the project:

- _Questions, feedback_: Open an issue with a `[Question] <issue-title>` title.
- _Bug reports_: Open an issue with a `[Bug] <issue-title>` title, an adequate description of the bug, and a code snippet that reproduces the issue if possible.
- _Feature requests and ideas_: Open an issue with an `[Enhancement] <issue-title>` title and a clear description of the enhancement proposal.

## Contribution guidelines

Every form of contribution is welcome, including documentation improvements, tests, bug fixes, and feature implementations.

Please follow these guidelines to contribute to the project:

- Make sure your changes match the documentation and coding style of the project, including [PEP 484](https://www.python.org/dev/peps/pep-0484/) type annotations.
- `mypy` is used to type-check the codebase, submitted code should not produce typing errors. See [this page](http://mypy-lang.org/) for more information on `mypy`.
- _Small_ fixes can be submitted simply by creating a pull request.
- Non-trivial changes should have an associated [issue](#community-guidelines) in the issue tracker that commits must reference (typically by adding `#refs <issue-id>` to the end of commit messages).
- Please write [tests](#testing) for the changes you make (if applicable).

If you have any questions about contributing to the project, please contact the project owner.

As mentioned in the [contribution guidelines](#contribution-guidelines), the project is type-checked using `mypy`, so first of all, the project must pass `mypy`'s static code analysis.

The project is tested using `pytest`. The chosen test layout is that tests are part of the application code, see [this page](https://docs.pytest.org/en/latest/goodpractices.html#tests-as-part-of-application-code) for details on what it means in practice.

If `pytest` is installed, the test set can be executed using the `pytest` command from within the project directory.

If `pytest-cov` is also installed, a test coverage report can be generated by executing `pytest --cov src/` from the root directory of the project.

## License - MIT

The library is open-sourced under the conditions of the MIT [license](https://choosealicense.com/licenses/mit/).
