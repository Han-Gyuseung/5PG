
.. raw:: html

 <b>Properties of free relaxed microstates</b><br>
 <canvas id="canvas1" width="300" height="300"></canvas><br>
 <b>Strain energy induced by local compositional fluctuation</b><br>
 <canvas id="canvas2" width="300" height="300"></canvas><br>

 <script>
 var canvas1 = document.getElementById("canvas1");
 var ctx1 = canvas1.getContext('2d');

 var canvas2 = document.getElementById("canvas2");
 var ctx2 = canvas2.getContext('2d');
 
 function drawCircle(ctx,x,y,r,c){
  ctx.fillStyle = c;
  ctx.beginPath();
  ctx.arc(x,y,r,0,2*Math.PI);
  ctx.fill();
 }
 function drawSquare(ctx,x,y,l,c){
  ctx.fillStyle = c;
  ctx.fillRect(x-l/2,y-l/2,l,l);
  ctx.strokeRect(x-l/2,y-l/2,l,l);
 }
 function clearCanvas(ctx){
  ctx.clearRect(0,0,300,300);
 }
 function writeText(ctx,x,y,string,c='black'){
  ctx.font = '15px arial';
  ctx.fillStyle = c;
  ctx.fillText(string,x,y+15)
 }
 const color1=[255,0,0]
 const color0=[0,0,255]
 function color_string(c,r=1){
  return "rgb("+String(Math.floor(c[0]))+","+String(Math.floor(c[1]))+","+String(Math.floor(c[2]))+","+String(r)+")"
 }
 function color_atom(species){ return species==1?color_string(color1):color_string(color0) }
 function radius_atom(species){ return species==1?10:8 }
 function color_box(a,b,c,d,r=1){
  s1=(a+b+c+d)/4
  s2=1-s1
  r=r/2
  c0=color1[0]*s1+color0[0]*s2
  c1=color1[1]*s1+color0[1]*s2
  c2=color1[2]*s1+color0[2]*s2
  return color_string([c0,c1,c2],r)
 }

 function BM_x(i){
  j=i/1000+1
  return 300*(j)**3-150
 }
 function BM_y(i){
  j=i/1000+1
  return 150-1000*(0.01*(1/j**2-1)**3+2*(1/j**2-1)**2)
 }



 function drawMicrostate(ctx,x,y,s1,s2,s3,s4,scale=1,ratio=1){
  r=ratio
  l=(35+(s1+s2+s3+s4)*2.5)*r
  drawSquare(ctx,x,y,l,color_box(s1,s2,s3,s4,r));
  drawCircle(ctx,x-l*0.25,y-l*0.25,radius_atom(s1)*scale,color_atom(s1));
  drawCircle(ctx,x-l*0.25,y+l*0.25,radius_atom(s2)*scale,color_atom(s2));
  drawCircle(ctx,x+l*0.25,y-l*0.25,radius_atom(s3)*scale,color_atom(s3));
  drawCircle(ctx,x+l*0.25,y+l*0.25,radius_atom(s4)*scale,color_atom(s4));
 }
 writeText(ctx1,70,0,'  x  '); writeText(ctx1,130,0,'energy'); writeText(ctx1,190,0,'other property');
 writeText(ctx1,190,15,'   (optional)')
 drawMicrostate(ctx1,40,60,0,0,0,0,1,1);  writeText(ctx1,70,45,'0.00');  writeText(ctx1,130,45,'-9.189');  writeText(ctx1,190,45, '   1.42');
 drawMicrostate(ctx1,40,110,1,0,0,0,1,1); writeText(ctx1,70,95,'0.25');  writeText(ctx1,130,95,'-9.339');  writeText(ctx1,190,95, '   1.02');
 drawMicrostate(ctx1,40,160,1,1,0,0,1,1); writeText(ctx1,70,145,'0.50'); writeText(ctx1,130,145,'-9.581'); writeText(ctx1,190,145,'   0.85');
 drawMicrostate(ctx1,40,210,1,1,1,0,1,1); writeText(ctx1,70,195,'0.75'); writeText(ctx1,130,195,'-9.763'); writeText(ctx1,190,195,'   0.51');
 drawMicrostate(ctx1,40,260,1,1,1,1,1,1); writeText(ctx1,70,245,'1.00'); writeText(ctx1,130,245,'-9.978'); writeText(ctx1,190,245,'   0.74');

 function draw_ctx2(t,s1,s2,s3,s4){
  ctx2.strokeStyle = 'black';
  ctx2.beginPath();
  ctx2.moveTo(300*(0.9)**3-150,150-1000*(0.01*(1/0.9**2-1)**3+2*(1/0.9**2-1)**2))
  for(i=-100;i<100;i++){
   j=i/1000+1
   //ctx2.lineTo(300*(j)**3-150,150-1000*(0.01*(1/j**2-1)**3+2*(1/j**2-1)**2))
   ctx2.lineTo(BM_x(i),BM_y(i))
  }
  ctx2.moveTo(50,10);
  ctx2.lineTo(50,150);
  ctx2.lineTo(250,150);
  ctx2.moveTo(45,15);
  ctx2.lineTo(50,10);
  ctx2.lineTo(55,15);
  ctx2.moveTo(245,145);
  ctx2.lineTo(250,150);
  ctx2.lineTo(245,155);
  ctx2.stroke();
  writeText(ctx2,0,15,'strain')
  writeText(ctx2,0,30,'energy')
  writeText(ctx2,255,140,'V/V0')
 
  var index=Math.abs(t%400-200)-100; //-100~100
  var x=BM_x(index);
  var y=BM_y(index);
  
  drawCircle(ctx2,x,y,5,"black")
  drawMicrostate(ctx2,x,200,s1,s2,s3,s4,1,index/1000+1);
 }

 var time=0;
 var ctx2_atom1=0;
 var ctx2_atom2=0;
 var ctx2_atom3=0;
 var ctx2_atom4=0;
 function animate_ctx2(timestamp){
  t=timestamp/20
  if (Math.floor(t/400)!=time){
   time=Math.floor(t/400)
   ctx2_atom1=Math.round(Math.random())
   ctx2_atom2=Math.round(Math.random())
   ctx2_atom3=Math.round(Math.random())
   ctx2_atom4=Math.round(Math.random())
  }
  clearCanvas(ctx2)
  draw_ctx2(t,ctx2_atom1,ctx2_atom2,ctx2_atom3,ctx2_atom4)
  window.requestAnimationFrame(animate_ctx2)
 }
 window.requestAnimationFrame(animate_ctx2)




 </script>
