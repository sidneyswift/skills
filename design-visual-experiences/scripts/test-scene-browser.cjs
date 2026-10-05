// Optional browser integration check. Serve the skill folder over local HTTP.
// PLAYWRIGHT_MODULE can point to an already available Playwright installation.
const assert=require('node:assert/strict');
let chromium;
try { ({chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright')); }
catch { throw new Error('Needs existing playwright; set PLAYWRIGHT_MODULE or run in a project with playwright installed.'); }
const url=process.argv[2];
if (!url) throw new Error('Usage: node scripts/test-scene-browser.cjs http://localhost:PORT/assets/scene-study.html');
(async()=>{
 const browser=await chromium.launch({headless:true});
 try {
  const page=await browser.newPage({viewport:{width:1100,height:800}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.goto(url);await page.evaluate(()=>window.ready);
  const resultTimes=[];
  for(const variant of[0,1]){
   for(const time of[0,.6,.9,1.65,1.95,1.999999,2,2.2,3.8,1.5]){
    const result=await page.evaluate(({variant,time})=>window.renderStudy(variant,time),{variant,time});
    assert.ok(result.measuredWidths.every(w=>w<=350),'copy fits available line width');
    assert.ok(result.panel.y+42+(result.lines.length-1)*26<result.button.y,'copy clears controls');
    assert.equal(result.media.source,time<2?'object':'diagram','inner edit remains independent of UI');
    if(time===2)assert.equal(result.media.frameIndex,6,'second source begins at its trim');
    if(time<result.resultTime)assert.equal(result.feedback,0,'no premature response');
    if(time===0){resultTimes.push(result.resultTime);assert.equal(result.lines.length>1,variant===1);}
   }
  }
  assert.notEqual(...resultTimes,'shared cue follows timing change');
  await page.getByRole('button',{name:'Change content'}).click();
  await page.locator('#seek').fill('2.2');
  assert.match(await page.locator('#clock').textContent(),/diagram/);
  assert.deepEqual(errors,[]);
  console.log('PASS: browser long-copy/aspect variants, dependent cue edit, source cut, interactive seek and no page errors. No creative/playback approval implied.');
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
