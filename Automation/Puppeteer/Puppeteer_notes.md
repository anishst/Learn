# Puppeteer

Puppeteer is a Node.js library maintained by Chrome's development team from Google. Puppeteer provides a high-level API to control headless Chrome or Chromium or interact with the DevTools protocol.

- Official Guide: https://github.com/GoogleChrome/puppeteer#puppeteer
- Google Guide: https://developers.google.com/web/tools/puppeteer/

- Puppeteer requires at least Node v6.4.0
- can generate PDFs of pages

## Initializing Project

1. make a project folder
2. move in to dir
3. ```npm init --yes```  to initialize project
4. ```npm install puppeteer``` 


## Sample file:
```
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  await page.screenshot({path: 'example.png'});

  await browser.close();
})();
```

to run: ```node example.js```

## Tools
- Cheerio (```npm install cheerio```) - dom parser tool; used for web scraping
  - Github: https://github.com/cheeriojs/cheerio
  - Official site:https://cheerio.js.org/

## Resources
- https://www.toptal.com/puppeteer/headless-browser-puppeteer-tutorial
- [Accessiblity testing example](https://www.deque.com/blog/accessibility-testing-for-the-mobile-web/)
## Known Issues

Issue: get PrintToPDF is not implemented error when trying to generate pdf

Solution: run in headless mode


