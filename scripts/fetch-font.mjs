import fs from 'node:fs/promises';
const url='https://fonts.googleapis.com/css2?family=Archivo:wght@400..900&display=swap';
const r=await fetch(url,{headers:{'User-Agent':'Mozilla/5.0 AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'}});if(!r.ok)throw new Error(String(r.status));
const css=await r.text();const blocks=css.split('/* latin */');const latin=blocks.at(-1);const urls=[...new Set([...latin.matchAll(/url\((https:[^)]+)\)/g)].map(m=>m[1]))];
for(let i=0;i<urls.length;i++){const response=await fetch(urls[i]);if(!response.ok)throw new Error('Font fetch failed');await fs.writeFile(new URL(`../dist/assets/archivo-${i}.woff2`,import.meta.url),Buffer.from(await response.arrayBuffer()));}
console.log(JSON.stringify({fontFiles:urls.length,css:latin.replace(/url\((https:[^)]+)\)/g,(_,url)=>`url('assets/archivo-${urls.indexOf(url)}.woff2')`)}));
