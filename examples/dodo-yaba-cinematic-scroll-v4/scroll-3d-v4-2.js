// V4.2 placement patch layered on top of scroll-3d-v4-1.js.
// Keeps the V4.1 state/events while standardizing topping density and distribution.
drawBuilder=function(){
  if(builderReady<7)return;
  builderCtx.clearRect(0,0,760,760);
  const sizeScale=sizes.find(x=>x[0]===buildState.size)[2];
  builderCtx.save();builderCtx.translate(380,380);builderCtx.scale(sizeScale,sizeScale);builderCtx.translate(-380,-380);
  containImage(builderImages.dough,380,380,590,590,1,0,1);
  builderCtx.save();clipPizza();
  containImage(builderImages.sauce,380,380,438,438,.96,0,1);
  containImage(builderImages.cheese,380,380,468,468,.90,0,1.02);
  const layouts={
    Pepperoni:[[340,315,.20,-.10],[420,330,.18,.08],[465,405,.18,-.04],[365,445,.19,.10]],
    Mushrooms:[[325,355,.15,-.15],[445,360,.14,.12],[405,455,.15,-.08]],
    'Red onion':[[365,340,.14,-.16],[445,420,.13,.14],[330,435,.13,.06]],
    'Bell pepper & basil':[[420,350,.15,.10],[340,395,.14,-.12],[430,455,.13,-.04]]
  };
  buildState.toppings.forEach(name=>{const def=toppingDefs[name],img=builderImages[def.key];(layouts[name]||[]).forEach(([x,y,s,r])=>containImage(img,x,y,230,230,1,r,s));});
  builderCtx.restore();builderCtx.restore();
  const base=sizes.find(x=>x[0]===buildState.size)[1],extra=buildState.toppings.reduce((n,t)=>n+toppingDefs[t].price,0);
  document.querySelector('#buildPrice').textContent=fmt(base+extra);
  document.querySelector('#buildName').textContent=buildState.toppings.length?buildState.toppings.join(' · '):'CHEESE BASE';
};
// Redraw immediately with the standardized placement engine.
drawBuilder();
