window.addEventListener('load',function(){
    const canvas=document.getElementById('canvas1');
    // willReadFrequently will enable a software acclerated 2D canvas
    const ctx=canvas.getContext('2d',{willReadFrequently: true})
    // if we set canvas size in css the element size and drawing size won't be synchronized
    // drawing size will be strecthed and the images will be distorted
    // so we need to do it using way below
    canvas.width=window.innerWidth
    canvas.height=window.innerHeight

    class Particle {
        constructor(effect,x,y,color){
            this.effect=effect
            this.x=Math.random()*this.effect.canvasWidth
            this.y=this.effect.canvasHeight
            this.color=color
            this.originX=x
            this.originY=y
            this.size=this.effect.gap
            this.dx=0
            this.dy=0
            this.vx=0
            this.vy=0
            this.force=0
            this.angle=0
            this.distance=0
            this.friction=Math.random()*0.6+0.15
            this.ease=0.1+Math.random()*0.1+0.005

        }
        draw(){
            this.effect.context.fillStyle=this.color
            this.effect.context.fillRect(this.x,this.y,this.size,this.size)
        }
        update(){
            this.dx=this.effect.mouse.x-this.x
            this.dy=this.effect.mouse.y-this.y
            this.distance=this.dx*this.dx+this.dy*this.dy
            this.force=-this.effect.mouse.radius/this.distance
            if (this.distance < this.effect.mouse.radius){
                this.angle=Math.atan2(this.dy,this.dx)
                this.vx+=this.force*Math.cos(this.angle)
                this.vy+=this.force*Math.sin(this.angle)
            }
            this.x+=(this.originX-this.x)*this.ease+( this.vx*=this.friction)
            this.y+=(this.originY-this.y)*this.ease+(this.vy*=this.friction)
        }
    }

    class Effect {
        constructor(context,canvasWidth,canvasHeight){
            this.context=context;
            this.canvasWidth=canvasWidth;
            this.canvasHeight=canvasHeight;
            this.textX=this.canvasWidth/2
            this.textY=this.canvasHeight/2
            this.fontSize=130;
            this.lineHeight=this.fontSize*0.8
            this.maxTextWidth=this.canvasWidth*0.5
            this.textInput=document.getElementById('textInput')
            this.textInput.addEventListener('keyup',(e)=>{
                if (e.key!==' '){
                    this.context.clearRect(0,0,this.canvasWidth,this.canvasHeight)
                    this.wrapText(e.target.value)
                }
            })
            // particles text
            this.particles=[]
            this.gap=3
            this.mouse={
                radius:20000,
                x:0,
                y:0
            }
            window.addEventListener('mousemove',(e)=>{
                this.mouse.x=e.x
                this.mouse.y=e.y
            })

        }
        wrapText(text){
            const gradient=this.context.createLinearGradient(0,0,this.canvasWidth,this.canvasHeight)
            gradient.addColorStop(0.3,'red')
            gradient.addColorStop(0.5,'orange')
            gradient.addColorStop(0.7,'yellow')
            this.context.lineWidth=3
            this.context.strokeStyle='red'
            this.context.textAlign='center'
            this.context.textBaseline='middle'
            this.context.fillStyle=gradient
            this.context.font=this.fontSize+'px Bangers'
            this.context.textAlign='center'
            this.context.textBaseline='middle'
            // this.context.fillText(text,this.textX,this.textY)
            // this.context.strokeText(text,this.textX,this.textY)
            // break multiline text
            let linesArray=[];
            let lineCounter=0;
            let line='';
            let words=text.split(' ');
            for (let i=0; i<words.length ;i++){
                let testline=line+words[i]+' ';
                if (this.context.measureText(testline).width>this.maxTextWidth){
                    line=words[i]+' ';
                    lineCounter++;
                }else{
                    line=testline;
                }
                linesArray[lineCounter]=line;
                // ctx.fillText(line,canvas.width/2,canvas.height/2+i*70)
            }
            let textHeight=this.lineHeight*lineCounter;
            this.textY=this.canvasHeight/2-textHeight/2;
            linesArray.forEach((e,index)=>{
                this.context.fillText(e,this.textX,this.textY+(index*this.lineHeight));
                this.context.strokeText(e,this.textX,this.textY+(index*this.lineHeight));
            })
            this.convertToParticles()
        }
        convertToParticles(){
            this.particles=[]
            // returns pixel data for specified part of canvas
            const pixels=this.context.getImageData(0,0,this.canvasWidth,this.canvasHeight).data
            this.context.clearRect(0,0,this.canvasWidth,this.canvasHeight)
            for(let y=0;y<this.canvasHeight;y+=this.gap){
                for(let x=0;x<this.canvasWidth;x+=this.gap){
                    const index=(y*this.canvasWidth+x)*4
                    const alpha=pixels[index+3];
                    if (alpha>0){
                        const red=pixels[index]
                        const green=pixels[index+1]
                        const blue=pixels[index+2]
                        const color='rgb('+red+','+green+','+blue+')'
                        this.particles.push(new Particle(this,x,y,color))
                    }
                }
            }
        }
        render(){
            this.particles.forEach(particle=>{
                particle.update()
                particle.draw()
            })
        }
        resize(width,height){
            this.canvasWidth=width
            this.canvasHeight=height
            this.textX=this.canvasWidth/2
            this.textY=this.canvasHeight/2
            this.maxTextWidth=this.canvasWidth*0.5
        }
    }
    const effect=new Effect(ctx,canvas.width,canvas.height)
    // effect.wrapText('Hello world lets do something new')
    function animate(){
        ctx.clearRect(0,0,canvas.width,canvas.height)
        effect.render()
        // to create an animation loop and pass it its father function
        requestAnimationFrame(animate)
    }
    animate()
    window.addEventListener('resize',function(){
        canvas.width=window.innerWidth
        canvas.height=window.innerHeight
        effect.resize(canvas.width,canvas.height)
        effect.wrapText(effect.textInput.value)
    })
    // ctx.beginPath();
    // ctx.moveTo(canvas.width/2,0);
    // ctx.lineTo(canvas.width/2,canvas.height)
    // ctx.stroke()
    // ctx.beginPath();
    // ctx.moveTo(0,canvas.height/2);
    // ctx.lineTo(canvas.width,canvas.height/2)
    // ctx.stroke()
    // const maxTextwidth=canvas.width * 0.8;
    // const lineHeight=80; 
    
    // const gradient=ctx.createLinearGradient(0,0,canvas.width,canvas.height)
    // gradient.addColorStop(0.3,'red')
    // gradient.addColorStop(0.5,'fuchsia')
    // gradient.addColorStop(0.7,'purple')
    
    // ctx.fillStyle=gradient
    // ctx.strokeStyle='blue'
    // ctx.lineSpacing='10px';
    // ctx.font='80px Helvetica'

    // function wrapText(text){
    
    // }
    // textInput.addEventListener('keyup',function(e){
    //     ctx.clearRect(0,0,canvas.width,canvas.height)
    //     wrapText(e.target.value)
    // })
})