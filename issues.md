<!-- TODO: Null directory handlers
    The distributed version of this will likely contain no directoies for source,
    staging, and refined data.
    Add handlers to check whether such files and directories exist, and create
    them if not.
    labels: bug
    assignees: danmassarano
-->

<!-- TODO: Make repo public
    Add code quality and dependencies checks in CI
    labels: ci, documentation
    assignees: danmassarano
-->

<!-- TODO: Add more badges
    - CI | build | coverage | documentation | versions | style | security | dependencies | quality
    labels: ci, documentation
    assignees: danmassarano
-->

<!-- TODO: Add error handling
    Add wherever applicable - especially important in the data scraping classes
    labels: enhancement
    assignees: danmassarano
-->

<!-- TODO: Add integration test
    Most changes will likely break unit tests, whereas integration tests
    should still pass for bugfixes and minor changes.
    labels: enhancement
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

<!-- TODO: Improve data cleanse process
    This is currently OK, but it does sometimes make data lose semantic meaning
    and results in flaky tests
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
