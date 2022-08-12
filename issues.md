<!-- TODO: Add pre commit hook
    Look into best ways to do this
    - Run black formatting
    - Remove whitespaces
    - Run pylint
    - Sort imports
    - Update requirements
    - Not committing on main
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: Add GitHub Actions for CI
    Actions for linting, running tests, checking code quality, security issues, broken/deprecated dependencies, missing requirements, and building
    - Run pylint
    - All requirements are set
    - Dependencies are up to date
    - Security scans
    - Code quality scan
    - Build
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: Write tests
    Write unit tests for as much as possible. There are some limitations, such as that you can't really unit test AI stuff, but do whatever is possible
    There are some refactoring dependencies that need to be handled first
    labels: enhancement
    assignees: danmassarano
-->

<!-- TODO: Add error handling
    Add wherever applicable - especially important in the data scraping classes
    labels: enhancement
    assignees: danmassarano
-->

<!-- TODO: Udd utils file to orchestrate
    labels: enhancement
    assignees: danmassarano
-->

<!-- TODO: Documentation
    Add docstrings and documentation for classes and methods
    labels: documentation
    assignees: danmassarano
-->

<!-- TODO: Add dockerfile for chatbot
    The chatbot runs on an older version of python so will need to be run in a container
    May need to handle Mac (Silicon and Intel) and Windows differently
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: Add makefile to build requirements and run
    This should allow everything to run on all machines as long as they have python3.9 installed
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: Add automated way of transforming data sources to .yml
    This is currently a manual process but should be automated
    labels: enhancement
    assignees: danmassarano
-->

<!-- TODO: Can the chatbot cache/store trained data?
    Training the chatbot is especially time consuming, can this be stored or cached?
    labels: enhancement, question
    assignees: danmassarano
-->

<!-- TODO: Use cached input
    Allow for option to skip scraping new data and use cached input files
    labels: enhancement, question
    assignees: danmassarano
-->

<!-- TODO: Additional Idea: Sherlock Holmes
    labels: epic, enhancement
    assignees: danmassarano
-->

<!-- TODO: Additional Idea: Bob Dylan Lyrics
    labels: epic, enhancement
    assignees: danmassarano
-->

<!-- TODO: Additional Idea: Write a song in a genre
    labels: epic, enhancement
    assignees: danmassarano
-->

<!-- TODO: Additional Idea: Follow a twitter hashtag
    labels: epic, enhancement
    assignees: danmassarano
-->

<!-- TODO: Additional Idea: Flirt bot
    labels: epic, enhancement
    assignees: danmassarano
-->