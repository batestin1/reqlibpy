
<h1 align="center">

<img src="https://img.shields.io/static/v1?label=REQLIBPY%20POR&message=Bates&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center">REQLIBPY </p> </h3>

<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> The <i>`reqlibpy`</i> library allows any files that configure a <i>`pip` </i> library installation to be installed automatically, along with their dependencies, whenever the library is imported for the first time.
The library must be installed using the command <i> `pip install reqlibpy` </i>, and after installation, just import the library with <i>`from reqlibpy import *`</i>.
The code will recursively check all directories in the project to find the requirements.txt file (even if it's misspelled, or in the wrong directory, eg "batatatinha/batata.txt") and install its dependencies.
The code will not display any error messages at the prompt, only what has been installed and what has been updated.
The code will run only once, on the first library import, to avoid unnecessary and repeated code execution. </p>

>> <h3> How install </h3>

```
pip install reqlibpy

```

>> <h3> How Works </h3>

```
from reqlibpy import *

```
    