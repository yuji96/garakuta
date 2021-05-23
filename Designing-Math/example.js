function setup(){	//最初に実行される
	
}

function loop(){	//常時実行される
	ctx.clearRect(0, 0, screenWidth, screenHeight);
	ctx.lineWidth = 2;
	ctx.strokeStyle = "green";

  var r = screenWidth * 0.45;
  var l_edge = screenWidth * 0.1;
  var l_center = screenWidth * 0.1;
  var x_offset = screenWidth / 2;
  var y_offset = screenHeight / 2;
  var toRad = Math.PI / 180;
  var time = 180 * curYubiX / screenWidth + 90;

	for (var i=0; i<2; i++){
    time += 180 * i;
    for(var phi=0; phi<360; phi=phi+5){

      var x_edge = r * Math.cos(0) * Math.cos(phi * toRad) * Math.cos(time * toRad) - r * Math.sin(0) * Math.sin(time * toRad) / 2;
      var x_center = r * Math.cos(70 * toRad) * Math.cos(phi * toRad) * Math.cos(time * toRad) - r * Math.sin(70 - toRad) * Math.sin(time * toRad) / 2;

      var y_edge = r * Math.cos(0) * Math.sin(phi * toRad);
      var y_center = r * Math.cos(70 * toRad) * Math.sin(phi * toRad);

      x_edge += x_offset;
      x_center += x_offset;
      y_edge += y_offset;
      y_center += y_offset;

      var hx_edge = l_edge * (- Math.sin(time * toRad)) + x_edge;
      var hy_edge = y_edge;

      var hx_center = l_center * Math.cos(phi * toRad) * Math.cos(time * toRad) + x_center;
      var hy_center = l_center * Math.sin(phi * toRad) + y_center;

      ctx.beginPath();
      ctx.moveTo(x_edge, y_edge);
      ctx.bezierCurveTo(hx_edge, hy_edge, hx_center, hy_center, x_center, y_center);
      ctx.stroke();
    }
  }

  var r_wing = r * 0.9;
  var width_wing = r * Math.sin(30 * toRad);
  var rotate = new Date().getTime() * 3 / 1000;;
  
  for(var i=0; i<360; i=i+60){

    var x_edge = r_wing * Math.cos(i * toRad + rotate) * Math.cos(time * toRad) + x_offset;
    var y_edge = r_wing * Math.sin(i * toRad + rotate) + y_offset;

    var hx_edge1 = width_wing * Math.cos((i - 90) * toRad + rotate) * Math.cos(time * toRad) + x_edge;
    var hx_edge2 = width_wing * Math.cos((i + 90) * toRad + rotate) * Math.cos(time * toRad) + x_edge;
    var hy_edge1 = width_wing * Math.sin((i - 90) * toRad + rotate) + y_edge;
    var hy_edge2 = width_wing * Math.sin((i + 90) * toRad + rotate) + y_edge;

    ctx.beginPath();
    ctx.moveTo(x_offset, y_offset);
    ctx.bezierCurveTo(x_offset, y_offset, hx_edge1, hy_edge1, x_edge, y_edge);
    ctx.bezierCurveTo(hx_edge2, hy_edge2, x_offset, hy_center, x_offset, y_offset);
    ctx.stroke();
  }
}

function touchStart(){	//タッチ(マウスダウン)されたら
	
}

function touchMove(){	//指が動いたら(マウスが動いたら)
	
}

function touchEnd(){	//指が離されたら(マウスアップ)
	
}
