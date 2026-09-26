import {createRequire} from 'node:module';
import assert from 'node:assert/strict';
const require=createRequire('/Users/devaansh28/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/package.json');
const {chromium}=require('playwright');
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
try {
  for(const reduced of [false,true]) {
    const c=await browser.newContext({viewport:{width:1440,height:1000},reducedMotion:reduced?'reduce':'no-preference'});
    await c.addInitScript(()=>{Element.prototype.requestPointerLock=()=>Promise.reject();Element.prototype.setPointerCapture=()=>{};Element.prototype.releasePointerCapture=()=>{};});
    const p=await c.newPage();await p.goto('http://localhost:4500');await p.evaluate(()=>document.fonts.ready);
    // Missing replay or an inert handler would fail: the user must be able to replay the entrance.
    assert.equal(await p.getByRole('button',{name:'Replay entrance'}).count(),1,'Replay entrance is available');
    await p.waitForTimeout(1800);
    await p.getByRole('button',{name:'Replay entrance'}).click();
    const animated=await p.locator('.hero').evaluate(e=>e.getAnimations({subtree:true}).some(a=>a.playState==='running'));
    assert.equal(animated,!reduced,'Entrance replays only when motion is allowed');
    await p.waitForTimeout(1800);
    const before=await p.locator('body').evaluate(e=>e.classList.contains('light'));
    await p.locator('.theme-toggle').click();await p.reload();
    assert.equal(await p.locator('body').evaluate(e=>e.classList.contains('light')),!before,'Theme persists');
    await p.locator('.theme-toggle').click();
    await p.waitForTimeout(1800);await p.screenshot({path:`lab/scrapbook-${reduced?'reduced':'desktop'}.png`});
    if(!reduced){await p.locator('[data-track=Blockchain]').click();assert.equal(await p.locator('.stamp-area .stamp').count(),1);await p.locator('#tracks').screenshot({path:'lab/scrapbook-tracks.png'});}
    await c.close();
  }
  for (const width of [360,390,768,1024]) {
    const c=await browser.newContext({viewport:{width,height:900}});
    await c.addInitScript(()=>{Element.prototype.requestPointerLock=()=>Promise.reject();Element.prototype.setPointerCapture=()=>{};Element.prototype.releasePointerCapture=()=>{};});
    const p=await c.newPage();await p.goto('http://localhost:4500');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1800);
    assert.equal(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,`${width}px overflow`);
    const cta=await p.locator('.hero-ctas .join-button').boundingBox();assert.ok(cta.y+cta.height<900,'Hero action visible');
    await p.screenshot({path:`lab/scrapbook-${width}.png`});
    await p.screenshot({path:`lab/scrapbook-full-${width}.png`,fullPage:true});
    await c.close();
  }
  console.log('PASS: replay animation, reduced-motion fallback, persisted theme, passport selection, mobile/tablet layouts');
}finally{await browser.close();}
