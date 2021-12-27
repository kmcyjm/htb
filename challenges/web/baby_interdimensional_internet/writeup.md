Execute the python script using `python2 baby_....py`

will listen on port 1337

send a request like below for a command injection
`curl -v -d 'ingredient=qwertyuiop&measurements=__import__("os").popen("ls").read()' http://localhost:1337/`

The value to ingredient and measurements will be used to construct recipe, which in turn is executed by `calc()`. Since recipe is in the form of an assignment `%s = %s`, the right-hand side of the assignement will be executed prior to the assignment, and there will be a `<name of ingredient> = <list of files>` global variable available after the execution, then the `garage` globals is able to access `<name of ingredient>` and pass that to `calculations` in `render_template()`.