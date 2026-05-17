# Theory Questions

## What is the difference between unit testing, integration testing, regression testing, and performance testing?

### Unit testing
Unit tests are low-level tests which target small, individual components in isolation: for example the individual functions and methods of classes and modules. As a result, unit tests run very quickly and can be considered "low-cost" tests.

### Integration testing
Integration tests are more "expensive" than unit tests in terms of time and computing resources. They test the interaction between 2 or more components. A simple example could be testing a function which adds data to the database - in this case the test would need to check the data in the database after the function has been called. API testing is also typicaly classed as integration testing.

### Performance testing
Performance testing validates that a system meets defined performance criteria — things like response time, throughput, and stability under load. Unlike unit or integration tests which check what a system does, performance tests check how well it does it. Performance tests are the most "expensive" of all, often requiring dedicated infrastructure and significant time to run. Common forms include:

- Load testing — does the system perform acceptably under the expected number of concurrent users?
- Stress testing — at what point does the system break, and how does it recover?
- Spike testing — how does the system handle a sudden sharp increase in traffic?
- Endurance testing — does performance degrade over a sustained period, for example due to memory leaks?

Performance testing is typically carried out in a dedicated environment that mirrors production as closely as possible, since results are meaningless if the hardware and infrastructure differ significantly from the real thing.

### Regression testing
Regression testing does not describe one particular form of testing: running a suite of regression tests generally means running older tests (which can be any or all of: unit, integration, performance, end-to-end and other types of test) when the codebase is updated. The point of regression testing is to make sure that existing functionality still works as expected when new code is added.

## Describe the process of working with TDD (Test-Driven Development).
TDD is the opposite of the traditional approach to software development - instead of writing code first, then writing a tests to check it works, TDD requires that tests are written before any functional code is written.

TDD requires that user stories and acceptance criteria have been defined, so that test cases can be written. The TDD process can be described as a cycle consisting of 3 stages:

1. RED: Write a test, watch it fail
2. GREEN: Write just enough code to pass the test
3. REFACTOR: Improve the code without changing its behaviour. 

The idea of this cycle is that it acts as a rapid feedback loop which keeps the developer on-track.

TDD requires a mindset shift from traditional software development: by writing the tests first, the developer naturally starts to think in terms of fulfilling the acceptance criteria.

TDD comes with an upfront cost as the tests needs to be writtten before any functional code is produced. However, it comes with certain benefits:

- Debugging becomes easier, as you naturally have a test-suite which pinpoints any failure
- Refactoring the codebase is less likely to cause unexpected problems, as you naturally have a comprehensive suite of regression tests available
- When combined with automated testing and Continuous Integration, breaking changes are easily and quickly spotted
- The TDD process leads to a self-documenting product, as the tests-suite forms a living specification of how the product should behave

## Describe how BDD (Behavior-Driven Development) differs from TDD.
BDD and TDD are similar approaches to software development, in that they both require that tests are written before the functional coding begins. 

A fundamental difference between the two approaches lies in the focus of the scripts which drive the development process. In TDD, the scripts are functional test scripts which are primarliy designed to be seen and used by developers. In BDD however, the scripts are written in such a way that any stakelholder in the project can understand them - so they form a common understanding of how the system or product should behave.

BDD scripts (known as feature files) use a special syntax called Gherkin which can both be easily understood by a human and also easily and reliabvly processed by a computer. Gherkin describes system behaviour in terms of scenarios, using a Given/When/Then structure:

- Given - the intial state / pre-conditions of the test
- When - the action(s) or event(s) of the behaviour being tested
- Then - the expected outcome or result

Because feature files can be read by any stakeholder - developers, testers, product owners, and clients alike - they serve as a living specification of the system. This  helps to snsure that all stakeholders share a common understanding of the expected behaviour, and this is a key reason for the existence of BDD.

In practical testing terms, BDD frameworks (such as Behave for Python) read the scenarios in feature files line by line, mapping each line to a step in a step file. The step files are where the actual test logic lives. This separation is a key feature of BDD.

A final comparison with TDD, is in the types of test each approach is best suited to. TDD is particularly powerful when applied to unit tests and simple integration tests, whereas BDD is more suited to end-to-end tests and more complex integration tests: BDD's human-readable scenarios naturally describe user journeys and system-level behaviour, which maps well to end-to-end testing. On the other hand, TDD is a natural fit for unit tests because they, like TDD scripts, are technical in nature and developer-facing — and the rapid RED/GREEN/REFACTOR cycle maps well to the small, focused scope of a unit test. 

## Imagine that you were going to build a website similar to Reading List (both frontend and backend). If you could choose freely, what types of tests would you want to use? Explain and justify your choices.
I would use all of the test types discussed above, including both TDD and BDD approaches. There is only one caveat - regarding performance testing which I will discuss futher on. 

I see unit tests and integration tests as non-negotiable: they are critical in ensuring that the system is error free and stable. By also employing automated testing in a CI workflow, they form a low-cost and high coverage suite of regression tests which are crucial the long-term maintainability and stability of the system.

End-to-end testing is also crucial in the development of a user-facing application on the web. It doesn't matter if you have 100% testing coverage through unit and integration test, if the actual user interface does not work as intended!'

Regression tests are a natural inclusion - they already exist as they are simply the tests used in development being re-used in an automated test-suite. There will be a cost of maintaining them over time as the codebase evolves, but I see this as small considering the benefits of long-term stability and protection against breaking changes.

The decision to implement performance testing would depend very much on the use-case. For example, if the website was designed as a hobby/occasional use project, then it would not be worth the cost of implementing performance tests (unless of course the aim was to learn about/ practice the implementation of such tests...). On the other hand, if this was to be a high-use system, or potentially a system whose user-base would increase over time then performance testing would become an important part of the project.

Regarding methodologies, for unit testing in particular, I would use TDD for the reasons described above in my previous answer (small, focused, technical in nature and suited to rapid development). Likewise, I would want to use BDD for E2E (end-to-end) testing and more complex integration testing (API testing for example, especially if there is a database connection involved). BDD would be particularly important if there were multiple stakeholders involved, but even if it was only me, I think BDD is a great way to document the application's behaviour and to get in the mindset of the user. It also makes the process structuring, maintaining and implementing E2E tests much easier. 