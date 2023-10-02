const canvas=document.getElementById("canvas");
const ctx=canvas.getContext("2d");
let snakeFood=null;
let count=0;
let button=document.getElementById("restart-button");
let image=document.getElementById("foodImage");
let snakeHeadImage=document.getElementById("headImage");
let snakeBodyImage=document.getElementById("bodyImage");
class snake{

    constructor(){    // INITIALIZING OUR SNAKE BODY PARAMETERS
        this.init_len=5;
        this.direction="right";
        this.cells=[];
    }
    createSnake(){         
        for(let i=0 ; i<this.init_len ; i++){
            this.cells.push({
                x:i,
                y:0
            })

        }
    }
    drawSnake(){    // STYLING THE APPEARANCE OF THE SNAKE
        ctx.clearRect(0,0,1200,600);
        ctx.fillStyle="white";
        ctx.font="40px sans-serif";
        ctx.fillText(`Score: ${count}`,30,50);

        this.cells.shift();
        ctx.fillStyle='brown';
        ctx.drawImage(image,snakeFood.x,snakeFood.y,60,60);
        for(let i=0 ; i<this.cells.length ; i++){
            this.cells[i].x%=20;
            this.cells[i].y%=10;
            if(this.cells[i].x===-1){
                this.cells[i].x=20;
            }
            if(this.cells[i].y===-1){
                this.cells[i].y=10;
            }
             
            const cell=this.cells[i];
            if(i===this.cells.length -1){
                ctx.fillStyle='red';

                
            ctx.drawImage(snakeHeadImage,cell.x*60,cell.y*60,58,58);

            }
            else{
                ctx.fillStyle='green';
                ctx.fillRect(cell.x*60,cell.y*60,58,58);
            }

            
        }

    }
    updateSnake(){

        let headX=this.cells[this.cells.length-1].x;
        let headY=this.cells[this.cells.length-1].y;
        let nextHeadX=(headX+1);
        let nextHeadY=headY;
        for(let i=0 ; i<this.cells.length-1; i++){
            if(headX===this.cells[i].x && headY===this.cells[i].y){  // HANDLING GAMEOVER CONDITIONS
                gameOver();
            }
        
        }
        if(snakeFood.x===(headX*60) && snakeFood.y===(headY*60)){  // DECIDING ACTIONS WHEN SNAKE HIT THE FOOD
            snakeFood=randomFood();   // CALLING RANDOM FOOD EACH TIME SNAKE TOUCHES FOOD
            this.cells.push({
                x:headX,
                y:headY
            }); 
            count++;
        }
        
        if(this.direction==='left'){
            nextHeadX=headX-1;
        }
        else if(this.direction==='up'){
            nextHeadX=headX;
            nextHeadY=headY-1;
        }
        else if(this.direction==='down'){
            nextHeadX=headX;
            nextHeadY=headY+1;
        }
        else if(this.direction==='right'){
            nextHeadX=headX+1;
        }


        this.cells.push({
            x:nextHeadX,
            y:nextHeadY
        });
    }
    gameLoop(){
        Snake.updateSnake();
        Snake.drawSnake();
    }
    changeDirection(direction){
        this.direction=direction;
    }

};
function snake_init(){
    snakeFood=randomFood();
    Snake.createSnake();
    Snake.drawSnake();           
    function keypressed(e){     // MAKING KEYBOARD KEYS TO CONTROL THE DIRECTION OF SNAKE MOVEMENT

        if(e.key=="ArrowLeft"){
            Snake.changeDirection("left");
        }
        else if(e.key=="ArrowDown"){
            Snake.changeDirection("down");
        }
        else if(e.key=="ArrowRight"){
            Snake.changeDirection("right");
        }
        else if(e.key=="ArrowUp"){
            Snake.changeDirection("up");
        }

    }
    document.addEventListener("keydown",keypressed);
}
function randomFood(){      // INITIALIZING THE FOOD OF THES SNAKE
    let foodX= Math.floor(Math.random() * (20-1))*60 ; // DECIDING COORDINATES OF FOOD 
    let foodY= Math.floor(Math.random() * (10-1))*60 ; 
    let food={
        x:foodX,
        y:foodY
    }
    return food;
}
const Snake=new snake();                    // CALLING SNAKE
snake_init();
const id=setInterval(Snake.gameLoop,300);   // CALLING SNAKE AND PUTTING ITS MOVEMENT IN THE LOOP
function gameOver(){
    clearInterval(id);
    myFunction();
}


window.addEventListener("load", function(){               // HANDLING RESTART BUTTON PROPERTIES
    var loadingMessage = document.getElementById('loadingMessage');
    loadingMessage.style.display = 'none'; 

});

button.addEventListener("click",()=>{   // TO MAKE UR SNAKE MOVE REPEATEDLY
    setTimeout(function() {
        location.reload();
      }, 100);
});