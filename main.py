with open("docs/index.html", "w") as out:
    with open("README.md") as _in:
        out.write(f"""<html>
<body>
<h1>Website README</h1>
<div>
{_in.read()}
</div>
</body>
</html>"""
        )