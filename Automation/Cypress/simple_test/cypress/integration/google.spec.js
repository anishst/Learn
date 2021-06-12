// allow auto completion using cypress library
/// <reference types="cypress" /> 

describe("Testing Google Search", () => {

    it("Go to google", () => {
        cy.visit("https://google.com");
        cy.contains("Google Search");
        cy.get('.gLFyf').type("Cypress{enter}");
        cy.url().should("include", "google.com");

        // using them with assertions
        cy.contains("How it works").then(($link) => {
            const labelText = $link.text();
            expect(labelText).contains('How it works');
        }).click();
    })
})