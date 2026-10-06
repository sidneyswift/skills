// Requires an already available Playwright; no install or generation.
const assert=require('node:assert/strict');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
(async()=>{const browser=await chromium.launch({headless:true});try{
 const page=await browser.newPage(),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.argv[2]);await page.waitForFunction(()=>window.fixture);
 for(const story of ['object','space'])for(const long of [false,true])for(const portrait of [false,true]){
  const result=await page.evaluate(({story,long,portrait})=>{
   fixture.configure({story,long,portrait});let lastSource,cutAt,readFrames=0;
   for(let frame=0;frame<=144;frame++){
    const t=frame/24,s=fixture.render(t);if(lastSource&&lastSource!==s.source.source)cutAt=t;lastSource=s.source.source;
    if(t>=s.cues.complete&&t<s.cues.act){if(s.state.layout.progress!==1)throw Error('moving read');readFrames++;}
   }
   const first=fixture.render(1.5),pixels=document.querySelector('canvas').toDataURL();fixture.render(5.8);fixture.render(0);fixture.render(1.5);
   return {cutAt,readFrames,pixelStable:pixels===document.querySelector('canvas').toDataURL(),...first};
  },{story,long,portrait});
  assert.equal(result.cutAt,3);assert.ok(result.readFrames>=13);assert.equal(result.pixelStable,true);
  assert.equal(result.width,portrait?540:960);assert.ok(result.cues.act>=result.cues.complete+.55-1e-9);
 }
 assert.deepEqual(errors,[]);console.log('PASS: 8 story/copy/aspect variants; 1160 rendered samples, readable holds, fixed inner cut and pixel-identical seek');
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exit(1);});
