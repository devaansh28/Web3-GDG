import fs from 'node:fs/promises';
const root = new URL('../dist/assets/', import.meta.url);
await fs.mkdir(root,{recursive:true});
const assets = {
 'logo.svg':'/_next/static/media/logo.a67d6019.svg',
 'threeway.png':'/threeway.png',
 'raj.png':'/_next/static/media/raj.064687c4.png',
 'nadja.png':'/_next/static/media/nadja.cdcddeb3.png',
 'ajeet.png':'/_next/static/media/ajeet.b49103e2.png',
 'astha.jpeg':'/_next/static/media/astha.94dc315e.jpeg',
 'vidhi.jpg':'/_next/static/media/vidhi.5cc9f80d.jpg',
 'prashant.jpeg':'/_next/static/media/Prashant.76610cb1.jpeg',
 'blog.png':'/_next/static/media/blog.251e4800.png',
 'blog2.png':'/_next/static/media/blog2.0eee1005.png',
 'blog3.png':'/_next/static/media/blog3.61e53ab3.png',
 'degen.png':'/1.png',
 'w3wc.png':'/events/3.png',
 'founders.png':'/maha.png',
 'pizza.png':'/pizza.png',
 'brinc.png':'/brinc.png'
};
await Promise.all(Object.entries(assets).map(async([name,path])=>{
 const r=await fetch('https://www.web3carnival.world'+path);
 if(!r.ok) throw new Error(`${name}: ${r.status}`);
 await fs.writeFile(new URL(name,root),Buffer.from(await r.arrayBuffer()));
 console.log(name);
}));
