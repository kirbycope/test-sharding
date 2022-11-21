# test-sharding
Split up tests by Feature and run concurrently.

## What is Sharding?
> A database shard, or simply a shard, is a horizontal partition of data in a database or search engine. Each shard is held on a separate database server instance, to spread load. - [Source](https://en.wikipedia.org/wiki/Shard_(database_architecture))

> When the test corpus is large or the execution time becomes long, we offer the possibility of splitting the tests across several devices: sharding. - [Source](https://source.android.com/docs/core/tests/tradefed/architecture/advanced/sharding)

### How Does This Help Testing?
A mobile device one runs one app at a time, so unlike desktop we cannot run multiple tests on a single device at once. What we can do is run a subset of tests on seperate devices. We ditribute the test load by `.feature` file and run each in a seperate thread.

![Test Sharding](/test_sharding.png)

## Running Tests
1. Run `python3 sandbox` or `python3 sandbox {dir}`

**ToDo**: Handle results
