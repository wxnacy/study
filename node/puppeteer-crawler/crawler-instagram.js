const puppeteer = require('puppeteer');

(async () => {
	const browser = await puppeteer.launch({headless: false});
	const page = await browser.newPage();
    await page.setJavaScriptEnabled(true);
	await page.goto('https://www.instagram.com/nike/');

	// Get the "viewport" of the page, as reported by the page.
	const dimensions = await page.evaluate(() => {
        // avatar
        let avatarSelector = '#react-root > section > main > article > header > div > div > div > img'
        let avatarDom = document.querySelector(avatarSelector)
        let avatar = ''
        if( avatarDom ){
            avatar = avatarDom.src
        }

        // name
        let nameSelector = '#react-root > section > main > article > header > section > div._ienqf > h1'
        let nameDom = document.querySelector(nameSelector)
        let name = ''
        if( nameDom ){
            name = nameDom.innerText;
        }


		return {
            avatar: avatar,
            name: name,
		};
	});

	console.log('Dimensions:', dimensions);

	await browser.close();
})();
