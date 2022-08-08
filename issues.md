<!-- TODO: Consolidate data sources into one directory.
    Data sources are scattered across 3 subprojects - these should all be contained in a data directory.
    labels: refactor
    assignees: danmassarano
-->

<!-- TODO: Organise project into extract/transform/train/run structure
    This project was initially created in a hackathon so things got rushed. Update structure so that it's properly organised
    labels: refactor
    assignees: danmassarano
-->

<!-- TODO: Refactor classes used to grab source data
    Go back to just using twitter for now and build an elon-bot and have it scrape data properly
    labels: refactor
    assignees: danmassarano
-->

<!-- TODO: Get proper requirements files in place
    There's really 5 projects in here, each with their own requirements - get this consolidated properly.
    labels: refactor
    assignees: danmassarano
-->

<!-- TODO: Write tests
    Write unit tests for as much as possible. There are some limitations, such as that you can't really unit test AI stuff, but do whatever is possible
    There are some refactoring dependencies that need to be handled first
    labels: enhancement
    assignees: danmassarano
-->

<!-- TODO: Add pre commit hook
    Look into best ways to do this - it should check for things like tests, branching, linting, that requirements are updated, etc
    - Run black formatting
    - Run pylint
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: Add GitHub Actions for CI
    Actions for linting, running tests, checking code quality, security issues, broken/deprecated dependencies, missing requirements, and building
    - Run black formatting
    - Run pylint
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: Add error handling
    Add wherever applicable - especially important in the data scraping classes
    labels: enhancement
    assignees: danmassarano
-->

<!-- TODO: Documentation
    Add docstrings and documentation for classes and methods
    labels: documentation
    assignees: danmassarano
-->

<!-- TODO: Write up proper README
    labels: documentation
    assignees: danmassarano
-->

<!-- TODO: Add makefile to build requirements and run
    This should allow everything to run on all machines as long as they have python3.9 installed
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: Add dockerfile for chatbot
    The chatbot runs on an older version of python so will need to be run in a container
    May need to handle Mac (Silicon and Intel) and Windows differently
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: load_teams_data should be a general 'load_from_txt' method
    labels: refactor
    assignees: danmassarano
-->

<!-- TODO: load_twitter_data should be a general 'load_from_csv' method
    labels: refactor
    assignees: danmassarano
-->

<!-- TODO: load_linkedin_data should be a general 'load_from_json' method
    labels: refactor
    assignees: danmassarano
-->

<!-- TODO: Update data loader to read all files in data directory
    Data loader is using hardcoded paths at present - update so that it just iterates through a directory and loads everything
    labels: refactor
    assignees: danmassarano
-->

<!-- TODO: Improve data cleanse and normalisation process
    Data cleansing is currently a bit clumsy and requires manual checking and intervention. Rewrite so that it can run properly and integrate so it's fully automated
    labels: enhancement
    assignees: danmassarano
-->


<!-- TODO: Add automated way of transforming data sources to .yml
    This is currently a manual process but should be automated
    labels: enhancement
    assignees: danmassarano
-->

<!-- TODO: Add lockfile
    Get this in place once requirements are more stable
    labels: ci
    assignees: danmassarano
-->

<!-- TODO: Can the chatbot cache/store trained data?
    Training the chatbot is especially time consuming, can this be stored or cached?
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