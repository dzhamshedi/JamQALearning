describe ("Open google ad find dns-shop", () => {
    beforeEach (() => {
        cy.viewport(1920,1080)    
        cy.visit("https://www.google.com/")
    })
    it("Get url", () => {
        cy.url().should("include", "google.com").log("Google opened")
        cy.get('.gLFyf').type("dns-shop").type("{enter}")
        cy.get("a[href^='https:']").contains("dns-shop.ru").click()
    })
})