var revolver, insert, currentTurn, bullets;



// ↑ 공용 변수
// ========================
// ↓ 게임 준비 함수

var screen = {
    canvas: document.createElement("canvas"),
    makeScreen: function () {
        this.canvas.width = 400;
        this.canvas.height = 400;
        this.context = this.canvas.getContext("2d");
        document.getElementById("canvas-russian").appendChild(this.canvas); // 캔버스 만들기
    },
    wipeScreen: function () {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height); // 캔버스 비우기
    }
};

function gameReady() {
    // 사이트 로딩 완료 시 실행할 함수
    randomSelect();
    screen.makeScreen();
    score = new component("20px", "Arial", "black", 30, 30, "text");
    highscore = new component("20px", "Arial", "black", 200, 30, "text");
    magazine = new drawingCircle(200, 200, 150, "gray", "dimgray");
    bullet1 = new drawingCircle(250, 113.4, 25, "yellow", "olive");
    bullet2 = new drawingCircle(300, 200, 25, "yellow", "olive");
    bullet3 = new drawingCircle(250, 286.6, 25, "yellow", "olive");
    bullet4 = new drawingCircle(150, 286.6, 25, "yellow", "olive");
    bullet5 = new drawingCircle(100, 200, 25, "yellow", "olive");
    bullet6 = new drawingCircle(150, 113.4, 25, "black", "dimgray");
    screen.wipeScreen();
    magazine.spawn();
    bullet1.spawn();
    bullet2.spawn();
    bullet3.spawn();
    bullet4.spawn();
    bullet5.spawn();
    bullet6.spawn();
    score.text = "점수: " + gameData.score;
    highscore.text = "최고점수: " + gameData.highscore;
    score.spawn();
    highscore.spawn();
}

function drawingCircle(x, y, radius, color, bgcolor) {
    circle = screen.context;
    circle.beginPath();
    circle.arc(x, y, radius, 0, 2 * Math.PI);
    circle.fillStyle = color;
    circle.fill();
    circle.lineWidth = 5; // 바깥선 굵기
    circle.strokeStyle = bgcolor;
    circle.stroke();

    this.spawn = function () {
        circle.beginPath();
        circle.arc(x, y, radius, 0, 2 * Math.PI);
        circle.fillStyle = color;
        circle.fill();
        circle.lineWidth = 5; // 바깥선 굵기
        circle.strokeStyle = bgcolor;
        circle.stroke();
    }

    // (1) 회전시 x축과 y축 위치 재조정
    // (2) 재조정한 위치에 다시 그리기
}

function component(width, height, color, x, y, type) {
    this.type = type;
    this.width = width;
    this.height = height;
    this.color = color;
    this.x = x;
    this.y = y;

    this.spawn = function () {
        icon = screen.context;
        if (this.type == "text") // (텍스트일 경우)
        {
            icon.font = this.width + " " + this.height;
            icon.fillStyle = color;
            icon.fillText(this.text, this.x, this.y);
        } else {
            icon.fillStyle = this.color;
            icon.fillRect(this.x, this.y, this.width, this.height);
        }
    }
};

function updateScreen() {
    screen.wipeScreen(); // 스크린을 리셋하고
    bullet1.spawn();
    bullet2.spawn();
    bullet3.spawn();
    bullet4.spawn();
    bullet5.spawn();
    bullet6.spawn();
    // 위치가 변경된 총알을 생성
    // 점수 텍스트를 생성
}



function gameStart() {
    document.getElementById("start-russian").style.visibility = "hidden";
}


// ======================================================


function randomSelect() {
    currentTurn = 0;
    revolver = ["n", "n", "n", "n", "n", "n"];
    var insert = Math.floor((Math.random() * 6)) // 0부터 5까지 (행렬을 쉽게 사용하기 위함)
    revolver[insert] = 'y';
    bullets = revolver.length;
    console.log("총알 배치: " + revolver);
    console.log("남은 탄창: " + bullets);
}

function selectShoot() {
    if (revolver[0] == "n")
    {
        console.log("당신은 살았습니다!");
        revolver.splice(0, 1);
    }
    else if (revolver[0] == "y")
    {
        console.log("BANG!!! 당신은 죽었습니다!");
        console.log("GAME OVER");
    }
}

function selectPass() {
    var movedBullet = revolver[0];
    revolver.splice(0, 1);
    revolver.splice(6, 0, movedBullet);
    console.log("총알 배치: " + revolver);
    // 다음 탄창으로 넘어감.
    // 발사와 원리가 같지만, 0번째 값을 삭제하진 않고 맨 뒤로 넘김
    // 무조건 점수 -1점 처리.
}

function selectDrop() {
    if (revolver[0] == "y")
    {
        console.log("총알이 있었습니다! 대단하시군요!");
        console.log("GAME OVER");
    }
    else if (revolver[0] == "n")
    {
        console.log("총알이 없었습니다! 그래도 다행이군요!");
        console.log("GAME OVER");
    }
    // 총알이 있을거라 예상하고 게임을 포기.
    // 성공하면 점수 획득, 실패하면 총알 위치를 알려준 후 게임 오버
}