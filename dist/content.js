(() => {
  const body=document.body;
  try{body.classList.toggle('light',localStorage.getItem('carnival-scrapbook-theme')!=='dark');}catch{}
  const toggle=document.querySelector('.theme-toggle');
  const updateToggle=()=>toggle.setAttribute('aria-label',body.classList.contains('light')?'Switch to dark theme':'Switch to light theme');
  updateToggle();
  toggle.addEventListener('click',()=>{body.classList.toggle('light');updateToggle();try{localStorage.setItem('carnival-scrapbook-theme',body.classList.contains('light')?'light':'dark');}catch{}});
  const input=document.querySelector('#directory-search');
  if(!input)return;
  const cards=[...document.querySelectorAll('.directory-card')];
  const filters=[...document.querySelectorAll('[data-directory-filter]')];
  let place='all';
  function update(){
    const query=input.value.trim().toLocaleLowerCase();
    let shown=0;
    cards.forEach(card=>{const visible=card.dataset.search.includes(query)&&(place==='all'||card.dataset.location===place);card.hidden=!visible;if(visible)shown++;});
    const kind=document.querySelector('.people-directory')?'speakers':document.querySelector('.partner-gallery')?'partners':'events';
    document.querySelector('#directory-count').textContent=`${shown} of ${cards.length} ${kind}`;
    document.querySelector('.directory-empty').hidden=shown!==0;
  }
  input.addEventListener('input',update);
  filters.forEach(button=>button.addEventListener('click',()=>{place=button.dataset.directoryFilter;filters.forEach(item=>{const active=item===button;item.classList.toggle('active',active);item.setAttribute('aria-pressed',String(active));});update();}));
})();
