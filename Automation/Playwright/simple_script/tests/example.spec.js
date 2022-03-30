const { test, expect } = require('@playwright/test');

test('basic test', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  const title = page.locator('.navbar__inner .navbar__title');
//   assert title
  await expect(title).toHaveText('Playwright')
//   take screenshot
  await page.screenshot({ path: 'playwright_homepage.png' });
});