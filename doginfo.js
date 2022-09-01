function YesScroll () {
    const pagination = document.querySelector('.paginaiton');
    const fullContent = document.querySelector('.infinite');
    const screenHeight = screen.height;
    let oneTime = false;
    document.addEventListener('scroll',OnScroll,{passive:true})
     function OnScroll () {
       const fullHeight = fullContent.clientHeight;   
       const scrollPosition = pageYOffset;
       if (fullHeight-screenHeight/2 <= scrollPosition && !oneTime) {
         oneTime = true;
         madeBox();
       }
     }
      function madeBox() {
        const list = document.createElement('div');
        const box = list.cloneNode('false');
        box.className="first";
        
        for (var i=0; i<5; i++){
          list.appendChild(box.cloneNode('true'));
        }    
        list.className = "list";
        fullContent.appendChild(list);
        oneTime = false;
      }
    }
    YesScroll();