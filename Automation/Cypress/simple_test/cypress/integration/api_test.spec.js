// allow auto completion using cypress library
/// <reference types="cypress" /> 

context("Test API from fake JSON Server", () => {

    // delete post 2 before adding it
    beforeEach("DELETE before creatinga new value", () => {
        cy.request({
            method: 'DELETE',
            url: 'http://localhost:3000/posts/2',
            failOnStatusCode: false
        }).then((x) => {
            expect(x.body).to.be.empty
        })
    })

    it("Test GET functionality of JSON Server", () => {
        cy.request("http://localhost:3000/posts/1").its('body').should('have.property', 'id');
    })

    it("Test POST functionality of JSON Server", () => {
        cy.request({
            method: 'POST',
            url: 'http://localhost:3000/posts',
            body: {
                "id": 2,
                "title": "Test Post from Cypress",
                "author": "Anish"
            }
        }).then((response) => {
            expect(response.body).has.property("title", "Test Post from Cypress");
        })
    })
});