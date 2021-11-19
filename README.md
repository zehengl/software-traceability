<div align="center">
    <img src="https://raw.githubusercontent.com/zehengl/software-traceability/main/static/favicon.png" alt="logo" height="196">
</div>

# software-traceability

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

A Python application to demonstrate some software traceability studies

## Develop

### Dependency

    python -m venv venv
    .\venv\Scripts\activate
    pip install requirements-dev.txt

### Docs

    cd docs
    make html
    cd build/html
    python -m http.server 9000 --bind localhost

### Test

    pytest

## Credits

- [Icon][1] by [geotatah][2]

[1]: https://www.flaticon.com/free-icon/networking_992837#term=social%20relation&page=1&position=14
[2]: https://www.flaticon.com/authors/geotatah
