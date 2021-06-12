const { AxePuppeteer } = require('@axe-core/puppeteer');

const puppeteer = require('puppeteer');

(async () => {

    const browser = await puppeteer.launch({ headless: false });

    const page = await browser.newPage();

    await page.setBypassCSP(true);

    // Emulate a mobile device

    await page.emulate(puppeteer.devices['Pixel 2']);

    await page.goto('https://www.deque.com');

    // Run the accessibility tests and gather the results

    const results = await new AxePuppeteer(page).analyze();

    console.log(results);

    await page.close();

    await browser.close();

})();