# Testing


## Levels of Testing
- **Unit testing** - verify your code at the level of functions and classes; positive and negative testing at the lowest layers of 
code; first safety net for catching bugs; should run fast; automate
- Component Testing - library and complied binary level tests
- **System Testing** - tests the external interfaces of a system which is a collection os sub-systems
- Performance Testing - testing done at sub-system and system levels to verify timing resource usages are acceptable
- **Acceptance Testing** - is a level of software testing where a system is tested for acceptability. The purpose of this test is to evaluate the system's compliance with the business requirements and assess whether it is acceptable for delivery.

# BDD

Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project. 

- extension of TDD
- tests are written first and then devlopment based on scenarios listed in tests
## Cucumber

Cucumber is a tool that supports Behaviour-Driven Development(BDD)

- https://cucumber.io/
- [step definitions](https://cucumber.io/docs/cucumber/step-definitions/)
 
```gherkin
Feature: Guess the word

  # The first example has two steps
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  # The second example has three steps
  Scenario: Breaker joins a game
    Given the Maker has started a game with the word "silky"
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters
```


# Agile Testing
Agile software development has resulted in burning down the silos of the traditional waterfall development methodology. 

Agile Manifesto:
- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

## Agile Metrics

- **Sprint velocity**: Velocity is the amount of work completed by the agile team in a given period of time. Sprint velocity is basically the rate at which the conditions mentioned in the software requirements specifications get converted into lines of tested code, or the number of story points covered by the team on every sprint.
- **Sprint burndown**: Also known as the burndown chart, this is a graphical representation of estimated tasks planned and the actual tasks completed. 


## Resources
- Getting Started - https://cucumber.io/guides/overview/#what-is-cucumber


## Gherkin

Gherkin is a simple set of grammar rules that makes plain text structured enough for Cucumber to understand.

Feautre file is composed of one feautre and multiple scenarios

- Gherkin Reference: https://cucumber.io/docs/gherkin/

### Syntax examples

GIVEN I am on the blog page\
WHEN I press the new post button\
THEN I am on the new post page

- Feature keyword - describes which part of the functionality scenarios are being created for.
- Scenario keyword - is used to describe the test case title.
- Given keyword - describes pre-conditions required to complete the scenario.
- When keyword - is used to describe the scenario’s steps.
- Then keyword - describes the expected result of the scenario.
- And keyword - can be used for Given, When and Then keywords to describe additional steps.


## Behave

**behave** is behaviour-driven development, Python style. Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project. 

https://behave.readthedocs.io/en/latest/tutorial.html


```pip install behave```

###  Dev Info:

- all scenarios are kept in feature files that should be put in the features directory
- All scenario steps must have an implementation

Docs: https://behave.readthedocs.io/en/latest/
Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project. 
### Test Driven Development (TDD) 
- practice of writing your test script before writing code

Workflow
 - red - write failing unit test
 - green - write passing unit test
 - refactor - clean up unit test

## 508 Compliance Testing

Section 508 requires that all website content be accessible to people with disabilities.

It is the law:
Section 508 of the Rehabilitation Act (29 U.S.C. 794d), as amended by the Workforce Investment Act of 1998 (P.L. 105-220), August 7, 1998.

Beginning January, 2018, new ADA regulations for web accessibility will go into effect. While organizations cannot be 100% compliant, there are steps that they can take to ensure their sites are accessible to those with disabilities.

### Some Checks to do:
- Review the Website Content Accessibility Guidelines (WCAG 2.0). These guidelines offer recommendations on how to make your website accessible; https://www.w3.org/WAI/standards-guidelines/wcag/
- Conduct an audit of your site using a WAVE Web Accessibility Tool. Google Chrome’s WAVE Tool is a great tool to look for accessible issues, including missing alt tags, styles, etc.; https://wave.webaim.org/
- Make sure your images have descriptive alt tags. Alt tags are used by screen readers, players, and voiceovers to describe elements on a website to users
- Keep inputs and forms accessible
- Enable keyboard navigation
- see this article for more tips: https://karlgroves.com/2018/05/25/automated-lies-with-one-line-of-code

### Checklists
- WebAIM Checklist: https://webaim.org/standards/wcag/checklist
- ADA Checklist: https://www.ada.gov/pcatoolkit/chap5chklist.htm
- How to Meet WCAG: https://www.w3.org/WAI/WCAG21/quickref/?versions=2.0
- https://a11yproject.com/checklist/

### Mobile Accessiblity

-  https://www.w3.org/WAI/standards-guidelines/mobile/
- https://interactiveaccessibility.com/blog/mobile-accessibility-move#.Xle-V6hKiUk
## Blogs

- https://karlgroves.com/category/accessibility-testing


## Tools

### Automation
- Selenium
- UFTOne
- Katalon
- [Ghost inspector](https://ghostinspector.com/)
- MicroFocus storm runner
- NuSum
### Performance
- JMeter
- Gatling
### TestComplete
- record and playback options
- has JIRA and Jenkins integration
- support coding using 7? different programming lanugages; ex. Python
- supports both desktop and web applications

# Blogs
- https://www.automatetheplanet.com/
- https://willowtreeapps.com/ideas
- Google Testing: https://testing.googleblog.com/
- https://testguild.com/blog/
- https://www.rainforestqa.com/blog/