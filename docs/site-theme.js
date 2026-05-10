(function(){
  const html=document.documentElement;
  const buttons=Array.from(document.querySelectorAll('.theme-toggle'));
  const icons=Array.from(document.querySelectorAll('#themeIcon,.theme-icon'));
  if(!buttons.length)return;
  function setTheme(theme){
    const isLight=theme==='light';
    if(isLight){html.setAttribute('data-theme','light');}else{html.removeAttribute('data-theme');}
    icons.forEach(function(icon){icon.textContent=isLight?'☀':'☾';icon.setAttribute('aria-hidden','true');});
    buttons.forEach(function(button){
      button.setAttribute('aria-label','Toggle theme');
      button.setAttribute('aria-pressed',String(isLight));
      if(!button.hasAttribute('type'))button.setAttribute('type','button');
    });
    localStorage.setItem('theme',theme);
  }
  const saved=localStorage.getItem('theme');
  setTheme(saved||'dark');
  buttons.forEach(function(button){
    button.addEventListener('click',function(){setTheme(html.getAttribute('data-theme')==='light'?'dark':'light');});
  });
})();
