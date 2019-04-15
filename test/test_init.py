from markyp_highlightjs import CDN,\
                               js,\
                               themes,\
                               highlight

def test_HighlightJSCDN():
    assert CDN.CDN_URL == "https://cdnjs.cloudflare.com/ajax/libs/highlight.js"
    assert CDN.VERSION == "9.15.6"
    assert CDN.cdn_url_with_version() ==\
        "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6"
    assert CDN.url_for_js() ==\
        "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"
    assert CDN.url_for_style("default") ==\
        "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/default.min.css"

def test_js():
    assert js.js_import.markup ==\
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"></script>'

    assert js.js_init.markup ==\
        '<script >\nhljs.initHighlightingOnLoad();\n</script>'

    js_import, js_init = js.js
    assert str(js_import) ==\
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"></script>'
    assert str(js_init) ==\
        '<script >\nhljs.initHighlightingOnLoad();\n</script>'

def test_themes():
    assert str(themes.atom_one_dark) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/atom-one-dark.min.css">'
    assert str(themes.atom_one_light) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/atom-one-light.min.css">'
    assert str(themes.darcula) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/darcula.min.css">'
    assert str(themes.default) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/default.min.css">'
    assert str(themes.github) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/github.min.css">'
    assert str(themes.github_gist) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/github-gist.min.css">'
    assert str(themes.idea) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/idea.min.css">'
    assert str(themes.monokai) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/monokai.min.css">'
    assert str(themes.solarized_dark) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/solarized-dark.min.css">'
    assert str(themes.solarized_light) ==\
        '<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/solarized-light.min.css">'

def test_highlight():
    assert highlight("import antigravity", language="python").markup ==\
        '<pre >\n<code class="python">import antigravity</code>\n</pre>'
