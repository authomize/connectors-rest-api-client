on_pull_request {
    run_linters()
    run_tests()
}

on_change to: master, {
    build_push_pypi_python_package()
}
