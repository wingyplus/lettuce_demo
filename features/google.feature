Feature: Search on Google Search

    Scenario: Search keyword on Google Search
        Given I am on Google Search
        When I search keyword "cucumber"
        Then I see title of first result should begin with Cucumber
