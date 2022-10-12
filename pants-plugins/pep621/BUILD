python_sources(
    name="pep621_requirements",
    resolve="pants-plugins",
    interpreter_constraints=["==3.9.*"],
    sources=["__init__.py", "pep621_requirements.py"],
)

python_tests(
    name="tests",
    resolve="pants-plugins",
    interpreter_constraints=["==3.9.*"],
    sources=["pep621_requirements_test.py"],
)

python_source(
    name="plugin_registry",
    resolve="pants-plugins",
    source="register.py",
    interpreter_constraints=["==3.9.*"],
)

pants_requirements(name="pep621-pants-requirements", resolve="pants-plugins")
pep621_requirements(name="pep621-requirements", resolve="pants-plugins")
