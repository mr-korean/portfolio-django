var revolver, insert, bullets, rollCount, rollLimit, rollPattern, makeInterval;

// ↑ 공용 변수
// ========================
// ↓ 게임 준비 함수

var screen = {
    canvas: document.createElement("canvas"),
    // 캔버스 만들기
    makeScreen: function () {
        this.canvas.width = 400;
        this.canvas.height = 400;
        this.context = this.canvas.getContext("2d");
        document.getElementById("canvas-russian").appendChild(this.canvas);

    },
    // 캔버스 비우기
    wipeScreen: function () {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }
};

function gameReady() {
    // 사이트 로딩 완료 시 실행할 함수
    
    // 캔버스 생성
    screen.makeScreen();

    // 도형 생성
    score = new component("20px", "Arial", "black", 30, 30, "text");
    highscore = new component("20px", "Arial", "black", 200, 30, "text");
    magazine = new drawingCircle(200, 200, 150, "gray", "dimgray");
    // 탄창 위치 패턴 : A
    bullet1 = new drawingCircle(250, 113.4, 25, "yellow", "olive");
    bullet2 = new drawingCircle(300, 200, 25, "yellow", "olive");
    bullet3 = new drawingCircle(250, 286.6, 25, "yellow", "olive");
    bullet4 = new drawingCircle(150, 286.6, 25, "yellow", "olive");
    bullet5 = new drawingCircle(100, 200, 25, "yellow", "olive");
    bullet6 = new drawingCircle(150, 113.4, 25, "yellow", "olive");
    // 발사한 총알은 black, dimgray로 색깔 변경
    screen.wipeScreen();
    score.text = "점수: " + gameData.score;
    highscore.text = "최고점수: " + gameData.highscore;
    magazine.spawn();
    bullet1.spawn();
    bullet2.spawn();
    bullet3.spawn();
    bullet4.spawn();
    bullet5.spawn();
    bullet6.spawn();
    score.spawn();
    highscore.spawn();
    rollPattern = "A";
    document.getElementById("russian-shoot").style.visibility = "hidden";
    document.getElementById("russian-pass").style.visibility = "hidden";
    document.getElementById("russian-drop").style.visibility = "hidden";
}

function drawingCircle(x, y, radius, color, bgcolor) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
    this.bgcolor = bgcolor;

    this.spawn = function () {
        circle = screen.context;
        circle.beginPath();
        circle.arc(this.x, this.y, radius, 0, 2 * Math.PI);
        circle.fillStyle = this.color;
        circle.fill();
        circle.lineWidth = 5; // 바깥선 굵기
        circle.strokeStyle = this.bgcolor;
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
            icon.fillStyle = this.color;
            icon.fillText(this.text, this.x, this.y);
        } else {
            icon.fillStyle = this.color;
            icon.fillRect(this.x, this.y, this.width, this.height);
        }
    }
};

function updateScreen() {
    screen.wipeScreen(); // 스크린을 리셋하고
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
    // 위치가 변경된 총알을 생성
    // 점수 텍스트를 생성
}

// ↑ 게임 준비 함수
// ======================================================
// ↑ 탄창 관련 연출

function rollMagazine() {
    document.getElementById("message-russian").innerHTML = "탄창 돌리는 중...";
    // makeInterval = setInterval(checkPattern, 8);
    rollCount = 0;
    rollLimit = 4; // 정식 버전 = 40
    var waitCounter;
    rollSet();

    function rollSet() {
        if (rollCount < rollLimit) {
            checkPattern();
            rollCount++;
            waitCounter = 100;
            setTimeout(rollSet, waitCounter); // 주어진 횟수동안 반복
            randomSelect();
            console.log("탄창 돌리기 " + rollCount + "회 실시");
        }
        else {
            // 돌기 연출이 끝난 후, 선택지를 보여준다.
            document.getElementById("russian-shoot").style.visibility = "visible";
            document.getElementById("russian-pass").style.visibility = "visible";
            document.getElementById("russian-drop").style.visibility = "visible";
        }
    }
}

function checkPattern() {
    if (rollPattern == "A") {
        rollPattern = "B";
        patternB();
        updateScreen();
    }
    else if (rollPattern == "B") {
        rollPattern = "A";
        patternA();
        updateScreen();
    };
}

function patternA() {
    bullet1.x = 250;
    bullet1.y = 113.4;
    bullet2.x = 300;
    bullet2.y = 200;
    bullet3.x = 250;
    bullet3.y = 286.6;
    bullet4.x = 150;
    bullet4.y = 286.6;
    bullet5.x = 100;
    bullet5.y = 200;
    bullet6.x = 150;
    bullet6.y = 113.4;
    console.log("회전 패턴: A");
}

function patternB() {
    bullet1.x = 200;
    bullet1.y = 100;
    bullet2.x = 286.6;
    bullet2.y = 150;
    bullet3.x = 286.6;
    bullet3.y = 250;
    bullet4.x = 200;
    bullet4.y = 300;
    bullet5.x = 113.4;
    bullet5.y = 250;
    bullet6.x = 113.4;
    bullet6.y = 150;
    console.log("회전 패턴: B");
}

function bulletFiredEffect() {
    switch (revolver.length) {
        case 6:
            bullet1.color = "black";
            bullet1.bgcolor = "dimgray";
            updateScreen();
            break;
        case 5:
            bullet1.color = "black";
            bullet1.bgcolor = "dimgray";
            bullet2.color = "black";
            bullet2.bgcolor = "dimgray";
            updateScreen();
            break;
        case 4:
            bullet1.color = "black";
            bullet1.bgcolor = "dimgray";
            bullet2.color = "black";
            bullet2.bgcolor = "dimgray";
            bullet3.color = "black";
            bullet3.bgcolor = "dimgray";
            updateScreen();
            break;
        case 3:
            bullet1.color = "black";
            bullet1.bgcolor = "dimgray";
            bullet2.color = "black";
            bullet2.bgcolor = "dimgray";
            bullet3.color = "black";
            bullet3.bgcolor = "dimgray";
            bullet4.color = "black";
            bullet4.bgcolor = "dimgray";
            updateScreen();
            break;
        case 2:
            bullet1.color = "black";
            bullet1.bgcolor = "dimgray";
            bullet2.color = "black";
            bullet2.bgcolor = "dimgray";
            bullet3.color = "black";
            bullet3.bgcolor = "dimgray";
            bullet4.color = "black";
            bullet4.bgcolor = "dimgray";
            bullet5.color = "black";
            bullet5.bgcolor = "dimgray";
            updateScreen();
            break;
        case 1:
            bullet1.color = "black";
            bullet1.bgcolor = "dimgray";
            bullet2.color = "black";
            bullet2.bgcolor = "dimgray";
            bullet3.color = "black";
            bullet3.bgcolor = "dimgray";
            bullet4.color = "black";
            bullet4.bgcolor = "dimgray";
            bullet5.color = "black";
            bullet5.bgcolor = "dimgray";
            bullet6.color = "black";
            bullet6.bgcolor = "dimgray";
            updateScreen();
            break;
    }
}

// ↑ 탄창 관련 연출
// ======================================================
// ↓ 실제 게임 함수

function gameStart() {
    bullet1.color = "yellow";
    bullet1.bgcolor = "olive";
    bullet2.color = "yellow";
    bullet2.bgcolor = "olive";
    bullet3.color = "yellow";
    bullet3.bgcolor = "olive";
    bullet4.color = "yellow";
    bullet4.bgcolor = "olive";
    bullet5.color = "yellow";
    bullet5.bgcolor = "olive";
    bullet6.color = "yellow";
    bullet6.bgcolor = "olive";
    updateScreen();
    document.getElementById("start-russian").style.visibility = "hidden";
    document.getElementById("russian-shoot").style.visibility = "hidden";
    document.getElementById("russian-pass").style.visibility = "hidden";
    document.getElementById("russian-drop").style.visibility = "hidden";
    document.getElementById("message-russian").innerHTML = "게임을 시작합니다!";
    setTimeout(rollMagazine, 2000);
    // (1) 총알이 돌아가는 연출을 보여준다.
    // (2) 연출이 끝나면 3가지 선택지를 띄운다.
}

function randomSelect() {
    revolver = ["n", "n", "n", "n", "n", "n"];
    var insert = Math.floor((Math.random() * 6)) // 0부터 5까지 (행렬을 쉽게 사용하기 위함)
    revolver[insert] = 'y';
    bullets = revolver.length;
    console.log("총알 배치: " + revolver);
    console.log("남은 탄창: " + bullets);
}

function selectShoot() {
    // 결과 확인을 위해 선택지를 다시 숨긴다.
    document.getElementById("russian-shoot").style.visibility = "hidden";
    document.getElementById("russian-pass").style.visibility = "hidden";
    document.getElementById("russian-drop").style.visibility = "hidden";
    // 결과를 볼 때까지 일부러 뜸을 들인다.
    document.getElementById("message-russian").innerHTML = "과연 결과는...?";
    setTimeout(checkShoot, 3000);
    function checkShoot() {
        if (revolver[0] == "n")
        {
            // 캔버스에 "*CLICK*"이라는 큰 글자를 파란색으로 표시('철컥'이라는 영어 표현)
            document.getElementById("message-russian").innerHTML = "축하합니다! 생존하셨습니다!";
            document.getElementById("russian-shoot").style.visibility = "visible";
            document.getElementById("russian-pass").style.visibility = "visible";
            document.getElementById("russian-drop").style.visibility = "visible";
            bulletFiredEffect();
            shootWin();
            updateScreen();
            revolver.splice(0, 1);
        }
        else if (revolver[0] == "y")
        {
            // 캔버스에 "BANG!!!"이라는 큰 글자를 빨간색으로 표시('빵!'이라는 영어 표현)
            document.getElementById("message-russian").innerHTML = "BANG!!! 사망하셨습니다!<br>GAME OVER";
            document.getElementById("start-russian").style.visibility = "visible";
            bulletFiredEffect();
            shootLose();
            updateScreen();
        }
    }
}

function shootWin() {
    switch (revolver.length) {
        case 6:
            gameData.score += 1;
            gameData.highscore += 1;
            break;
        case 5:
            gameData.score += 2;
            gameData.highscore += 2;
            break;
        case 4:
            gameData.score += 3;
            gameData.highscore += 3;
            break;
        case 3:
            gameData.score += 4;
            gameData.highscore += 4;
            break;
        case 2:
            gameData.score += 5;
            gameData.highscore += 5;
            break;
        case 1:
            gameData.score += 6;
            gameData.highscore += 6;
            break;
    }
}

function shootLose() {
    switch (revolver.length) {
        case 6:
            gameData.score -= 2;
            break;
        case 5:
            gameData.score -= 3;
            break;
        case 4:
            gameData.score -= 4;
            break;
        case 3:
            gameData.score -= 5;
            break;
        case 2:
            gameData.score -= 6;
            break;
        case 1:
            gameData.score -= 7;
            break;
    }
}

function selectPass() {
    document.getElementById("message-russian").innerHTML = "다음 총알로 넘어갔습니다.";
    var movedBullet = revolver[0];
    revolver.splice(0, 1);
    revolver.splice(6, 0, movedBullet);
    gameData.score -= 1;
    updateScreen();
    console.log("총알 배치: " + revolver);
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

// ↑ 실제 게임 함수
// ======================================================
// ↓ 점수 관련

function clearScore() {
    if (window.confirm("현재 점수를 초기화하시겠습니까?")) {
        gameData.score = 0;
        updateScreen();
        score.spawn();
        highscore.spawn();
    }
}