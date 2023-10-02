let item=document.getElementsByClassName("list-group-item");
let items=document.querySelectorAll("li");
let list=document.querySelector("#items");
let itemsList=document.querySelector("ul");
let inputAdd=document.getElementById("addForm");
let inputSearch=document.getElementById("filter");
let themeOptions=document.querySelectorAll('input[type="radio"]');
let reset=document.querySelector(".reset");

//storing in local memory



reset.addEventListener('click', function (event) {
    localStorage.clear();
    location.reload();
    localStorage.setItem("jj", 0);
    for(let i of items){
    
        localStorage.setItem( `cItem${parseInt(localStorage.getItem("jj"))}`,i.firstChild.textContent  );
        let temp=parseInt(localStorage.getItem("jj"));
        localStorage.setItem("jj",temp+1);

    }
});





function storeItem(newLi){
    localStorage.setItem( `cItem${parseInt(localStorage.getItem("jj"))}`, newLi );
    let temp=parseInt(localStorage.getItem("jj"));
    localStorage.setItem("jj",temp+1);
}

function storeTheme(theme){
    localStorage.setItem( "theme", theme);

} 


//using local memory data 

function applyTheme(){

    const activeTheme=localStorage.getItem("theme");

    themeOptions.forEach( (i)=>{

        if(i.id===activeTheme){

            i.checked=true;

        }

    } ); 

}
function applyItem(){
    for(let i=4 ; i<parseInt(localStorage.getItem("jj")); i++){    
        let newLi=document.createElement("li");
        newLi.draggable="true";
        newLi.className="list-group-item";
        newLi.textContent=localStorage.getItem(`cItem${i}`);
        let newDel=document.createElement("button");
        newDel.className="btn btn-danger btn-sm float-end delete";
        newDel.textContent="X";
        newLi.append(newDel);
        itemsList.append(newLi);
    }
    

}
themeOptions.forEach( (theme)=>{

    theme.addEventListener( "click", ()=>{

        storeTheme(theme.id);
        applyTheme();

    } ); 

} );


///////////////////////


document.onload=applyItem();
document.onload = applyTheme();


////////////////////////


inputAdd.addEventListener("submit",addItem);
itemsList.addEventListener("click",deleteDo);
inputSearch.addEventListener("keyup",searchDo);


function addItem(e){
    e.preventDefault(); 
    let newLi=document.createElement("li");
    newLi.className="list-group-item";
    newLi.textContent=e.target[0].value;
    let newDel=document.createElement("button");
    newDel.className="btn btn-danger btn-sm float-end delete";
    newDel.textContent="X";
    newLi.append(newDel);
    itemsList.append(newLi);
    storeItem(e.target[0].value);
    e.target[0].value="";
    localStorage.reload(); //////////////////////////
}

function deleteDo(e){
    let value = e.target.parentElement.firstChild.textContent;
    if(e.target.classList.contains("btn-danger")){
        if(confirm("Do you really want to delete this element??")){
            itemsList.removeChild(e.target.parentElement);
            let identity=e.target.getAttribute('fdprocessedid');
        }
    }
    let ii=0;
    for(let i=0 ; i<parseInt(localStorage.getItem("jj")) ; i++){
        if( localStorage.getItem( `cItem${i}` ) === value ){
            ii=i;
            localStorage.removeItem(`cItem${i}`);
            i=parseInt(localStorage.getItem("jj"));
        }

    }
    for(let i=ii+1 ; i<parseInt(localStorage.getItem("jj"))  ; i++){
        let v=localStorage.getItem( `cItem${i}` );
        localStorage.removeItem(`cItem${i}`);
        localStorage.setItem( `cItem${i-1}` , v);
    }
    let temp=parseInt(localStorage.getItem("jj"));
    localStorage.setItem("jj",temp-1);
}
function searchDo(e){

    let item=e.target.value.toLowerCase();
    let searchSpace= document.querySelectorAll("li") ;

    Array.from(searchSpace).forEach( (i)=>{
        let text=i.textContent.toLowerCase();
        if( text.includes(item)  ){
            i.style.display="block";
        }
        else{
            i.style.display="none";
        }
    });
        
}



// DRAG AND DROP //

let updatedItem=document.getElementsByClassName("list-group-item");
let dragSrcContent;

for(let li of updatedItem){
    li.addEventListener( "dragstart" , dragStart );
    li.addEventListener( "dragover" , dragOver );
    li.addEventListener( "drop" , dragDrop );

}
function dragStart(e){
    dragSrcContent=this;
    e.dataTransfer.effectAllowed="move";
    e.dataTransfer.setData("text/html",dragSrcContent.firstChild.textContent);
}
function dragOver(e){
    e.preventDefault();
    e.dataTransfer.dropEffect="move";
}
function dragDrop(e){
    let value1=dragSrcContent.firstChild.textContent;
    let value2 = e.target.firstChild.textContent;
    let ii1=0;
    let ii2=0;
    for(let i=0 ; i<parseInt(localStorage.getItem("jj")) ; i++){
        if( localStorage.getItem( `cItem${i}` ) === value1 ){
            ii1=i;
            i=parseInt(localStorage.getItem("jj"));
        }
    }
    for(let i=0 ; i<parseInt(localStorage.getItem("jj")) ; i++){
        if( localStorage.getItem( `cItem${i}` ) === value2 ){
            ii2=i;
            i=parseInt(localStorage.getItem("jj"));
        }
    }
    localStorage.setItem( `cItem${ii1}`, value2 );
    localStorage.setItem( `cItem${ii2}`, value1 );
    
    if(dragSrcContent!=this){
        dragSrcContent.firstChild.textContent=this.firstChild.textContent;
        this.firstChild.textContent=e.dataTransfer.getData("text/html");

    }

}