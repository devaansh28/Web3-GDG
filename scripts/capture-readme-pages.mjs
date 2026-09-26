import fs from 'node:fs/promises';
import {createRequire} from 'node:module';
const require=createRequire('/Users/devaansh28/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/package.json');
const {chromium}=require('playwright');
const output='screenshots/pages';
await fs.mkdir(output,{recursive:true});
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
try{
  const context=await browser.newContext({viewport:{width:1440,height:1300},deviceScaleFactor:1});
  const page=await context.newPage();
  for(const [name,path] of [['home','/?design=scrapbook#home'],['events','/archive.html'],['speakers','/people.html'],['ecosystem','/ecosystem.html'],['programme','/programme.html']]){
    console.log(`Opening ${name}`);
    await page.goto(`http://localhost:4500${path}`,{waitUntil:'domcontentloaded',timeout:15000});
    await page.evaluate(()=>document.fonts.ready);
    // Let finite scrapbook entrance motion settle so the README shows the
    // finished composition instead of a half-opacity animation frame.
    await page.waitForTimeout(name==='home'?1800:350);
    await page.screenshot({path:`${output}/${name}.jpg`,type:'jpeg',quality:84});
    if(name==='programme'){
      await page.locator('#demo-night').scrollIntoViewIfNeeded();
      await page.waitForTimeout(180);
      await page.screenshot({path:`${output}/programme-demo-night.jpg`,type:'jpeg',quality:84});
      await page.locator('#awards').scrollIntoViewIfNeeded();
      await page.waitForTimeout(180);
      await page.screenshot({path:`${output}/programme-awards.jpg`,type:'jpeg',quality:84});
    }
    console.log(`${name}: captured`);
  }
  await context.close();
}finally{await browser.close();}
