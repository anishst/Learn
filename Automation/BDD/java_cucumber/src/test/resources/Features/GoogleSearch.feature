Feature: To Test Google Search
  Tests the Google Search Feature

  @stability
  Scenario: Test Google Search
    Given User is on Google Search Page
    When I enter search term in box
    And I click on Search button
    Then Show Results
