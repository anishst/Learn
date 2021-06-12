// allow auto completion using cypress library
/// <reference types="cypress" /> 

// mocha test runner 
it('google test', function () {

    cy.visit('https://www.google.com/');
    // get search input
    cy.get('.gLFyf').type("Cypress{enter}");
    cy.screenshot();
    cy.get('.dmenKe > :nth-child(1) > .usJj9c > .r > .l').click()

})

// it.only - run only this test
// it.only('login test', function () {

//     cy.visit('https://opensource-demo.orangehrmlive.com/');
//     cy.get('#txtUsername').type('Admin')
//     cy.get('#txtPassword').type('admin123')
//     cy.get('#btnLogin').click()

// })