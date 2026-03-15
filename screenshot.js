const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  
  await page.goto('http://localhost:8080', { waitUntil: 'networkidle' });
  await page.screenshot({ path: '/tmp/site-screenshot.png', fullPage: true });
  
  console.log('Screenshot saved to /tmp/site-screenshot.png');
  await browser.close();
})();
