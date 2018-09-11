var random1, random2, position1, position2, position3, save1, save2, numbers, cupsChanged, shuffleCount, makeInterval, hiddenAnswer, finalAnswer, youMissed, parsedData;
var rotationLimit = 1; // 섞기 돌리는 횟수
var cups = ["A", "B", "C"];


// (※) 화면 새로고침. 움직이는 효과는 전부 여기에 있다.
// "지우기- 조건확인 - 좌표이동 - 그리기"의 무한반복이다.
function updateScreen() {
    // (청소 → 표시) 세트
    screen.wipeScreen();
    cupA.respawn();
    cupB.respawn();
    cupC.respawn();
    score.text = "점수: " + gameData.score;
    highscore.text = "최고점수: " + gameData.highscore;
    score.respawn();
    highscore.respawn();
};

function gameReady() {
    // 사이트가 로딩되면 실행될 함수. 게임을 준비한다.
    // 캔버스 생성 → 도형 생성 → 도형 표시
    screen.makeScreen();
    score = new component("20px", "Arial", "black", 30, 30, "text");
    highscore = new component("20px", "Arial", "black", 200, 30, "text");
    cupA = new component(50, 50, "dimgray", 70, 180);
    cupB = new component(50, 50, "dimgray", 170, 180);
    cupC = new component(50, 50, "dimgray", 270, 180);
    cupA.respawn();
    cupB.respawn();
    cupC.respawn();
    score.text = "점수: " + gameData.score;
    highscore.text = "최고점수: " + gameData.highscore;
    score.respawn();
    highscore.respawn();
    document.getElementById("monteButton-1").style.visibility = "hidden";
    document.getElementById("monteButton-2").style.visibility = "hidden";
    document.getElementById("monteButton-3").style.visibility = "hidden";
};

var screen = {
    // 캔버스 세트(생성 및 청소)
    canvas: document.createElement("canvas"),
    makeScreen: function () {
        this.canvas.width = 400;
        this.canvas.height = 400;
        this.context = this.canvas.getContext("2d");
        document.getElementById("canvas-monte").appendChild(this.canvas); // 캔버스 만들기
    },
    wipeScreen: function () {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height); // 캔버스 비우기
    }
};

// (※) 컵의 속성, 다시 그리기, 이동, 현재 위치 확인.
function component(width, height, color, x, y, type) {
    this.type = type;
    this.width = width;
    this.height = height;
    this.color = color;
    this.x = x;
    this.y = y;
    this.boostX = 0;
    this.selected = false;
    this.goal = 0;

    // this.A = 70; // 배열에서 처음 A의 자리
    // this.B = 170; // 배열에서 처음 B의 자리
    // this.C = 270; // 배열에서 처음 C의 자리

    this.respawn = function () {
        // type를 파악하여 텍스트인지 도형인지 확인
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
    this.moveThis = function () {
        // x좌표 이동
        // 야바위 게임에서는 x좌표만 움직이므로 x좌표의 변화를 이용하여
        // 움직임을 표시한다.
        this.x += this.boostX;
    }
    this.checkPosition = function () {
        // x좌표 확인
        if (this.x == this.goal) {
            this.boostX = 0;
        } else if (this.x !== this.goal && this.x < this.goal) {
            this.boostX = 2;
        } else if (this.x !== this.goal && this.x > this.goal) {
            this.boostX = -2;
        }
    }
};

// (2) "시작"을 누르면 야바위가 시작된다.
function gameStart() {
    document.getElementById("monteButton-1").style.visibility = "hidden";
    document.getElementById("monteButton-2").style.visibility = "hidden";
    document.getElementById("monteButton-3").style.visibility = "hidden";
    document.getElementById("start-monte").style.visibility = "hidden";
    randomAnswer(); // (3) 정답을 무작위로 선택한다.
    checkHiddenAnswer(); // (4) 정답을 빨간색으로 확인시킨다. (정답 확인 3초)
    setTimeout(shuffling, (3000 + 1000)); // (5) checkHiddenAnswer로부터 초 뒤에 섞기를 시작한다.
};

function randomAnswer() {
    document.getElementById("message-monte").innerHTML = "빨간색 박스의 위치를 기억하세요."; // 정답 미리보기 안내
    hiddenAnswer = Math.floor((Math.random() * 3) + 1) // 무작위로 1개 선택 (3개 기준)
    switch (hiddenAnswer) {
        case 1:
            cupA.selected = true;
            cupB.selected = false;
            cupC.selected = false;
            finalAnswer = "A";
            break;
        case 2:
            cupA.selected = false;
            cupB.selected = true;
            cupC.selected = false;
            finalAnswer = "B";
            break;
        case 3:
            cupA.selected = false;
            cupB.selected = false;
            cupC.selected = true;
            finalAnswer = "C";
            break;
    };
};

function checkHiddenAnswer() {
    if (cupA.selected == true) {
        cupA.color = "red";
        updateScreen(); // 빨간색으로 다시 그리기
        cupA.color = "dimgray";
    } else if (cupB.selected == true) {
        cupB.color = "red";
        updateScreen();
        cupB.color = "dimgray";
    } else if (cupC.selected == true) {
        cupC.color = "red";
        updateScreen();
        cupC.color = "dimgray";
    }
    setTimeout(updateScreen, 3000); // 3초 뒤에 회색으로 다시 그리기
};

// (6) (최중요) 설계도 - 골라인 설정 - 애니메이션 ON - 도착 확인 - 애니메이션 OFF - 정답 확인
function shuffling() {
    document.getElementById("message-monte").innerHTML = "이제부터 섞겠습니다. 집중하세요!";
    // ※ 인터벌은 맨 처음에 한 번 돌게 하고, 섞기가 전부 끝나면 멈추기로 한다.
    makeInterval = setInterval(moveCups, 8);

    // ※ 전술한대로 for문은 인터벌 이전에 결과를 전부 내버리기 때문에, if를 이용해
    // 필요할 때만 결과를 도출하도록 한다.
    shuffleCount = 0;
    var waitCounter;
    watchThis();

    function watchThis() {
        if (shuffleCount < rotationLimit) {
            rotationCheck();
            setDestination();
            shuffleCount++;
            waitCounter = 1800;
            setTimeout(watchThis, waitCounter);
            // console.log("watchThis " + shuffleCount + "회 실시, " + cups);
        } else {
            answerMeNow();
        };
    };
};

function moveCups() {
    // 좌표이동 → 위치확인( → "표시 세트")
    cupA.moveThis();
    cupB.moveThis();
    cupC.moveThis();
    cupA.checkPosition();
    cupB.checkPosition();
    cupC.checkPosition();
    updateScreen();
};

// (6.1) 설계도 만들기
function rotation() {
    // 현재 결과값이 이전하고 같으면 다시 하는 부분을 여기에 넣는다.
    numbers = [0, 1, 2]; // 자리 배치용 배열
    cupsChanged = ["cups를", "여기에", "덮어씌움"];
    random1 = (Math.floor(Math.random() * 3));
    position1 = numbers[random1];
    numbers.splice(random1, 1);
    random2 = (Math.floor(Math.random() * 2));
    position2 = numbers[random2];
    numbers.splice(random2, 1);
    position3 = numbers[0];

    save1 = cups[position1];
    save2 = cups[position2];
    cups[position2] = save1;
    cups[position1] = save2;

    cupsChanged[position1] = cups[position1];
    cupsChanged[position2] = cups[position2];
    cupsChanged[position3] = cups[position3];
};

function rotationCheck() {
    if (cupsChanged == cups || (cups == ["A", "B", "C"] && i == rotationLimit)) {
        rotation();
    } else {
        rotation();
        cups[0] = cupsChanged[0];
        cups[1] = cupsChanged[1];
        cups[2] = cupsChanged[2];
    }
};

// (6.2) 앞서 설정한 좌표값에 따라 컵을 움직인다.
function setDestination() {
    // (중요) 설계도에 따라 컵의 목적지를 설정한다.
    if (cups[0] == "A") {
        cupA.goal = 70;
    } else if (cups[1] == "A") {
        cupA.goal = 170;
    } else if (cups[2] == "A") {
        cupA.goal = 270;
    }

    if (cups[0] == "B") {
        cupB.goal = 70;
    } else if (cups[1] == "B") {
        cupB.goal = 170;
    } else if (cups[2] == "B") {
        cupB.goal = 270;
    }

    if (cups[0] == "C") {
        cupC.goal = 70;
    } else if (cups[1] == "C") {
        cupC.goal = 170;
    } else if (cups[2] == "C") {
        cupC.goal = 270;
    }
};

// (?) 섞기 과정이 끝나면 질문을 던진다.
function answerMeNow() {
    if (cups[0] == finalAnswer) {
        youMissed = 1;
    } else if (cups[1] == finalAnswer) {
        youMissed = 2;
    } else if (cups[2] == finalAnswer) {
        youMissed = 3;
    }
    clearInterval(makeInterval);
    // (혹시 모르니까) 인터벌 정지 함수를 다시 한 번 넣는다.

    document.getElementById("message-monte").innerHTML = "다 섞었습니다. 빨간색 박스는 몇 번 자리에 있을까요?";
    console.log(hiddenAnswer, cupsChanged)
    // console.log("설계도 : " + cups + "정답 : " + finalAnswer);
    document.getElementById("monteButton-1").style.visibility = "visible";
    document.getElementById("monteButton-2").style.visibility = "visible";
    document.getElementById("monteButton-3").style.visibility = "visible";
};

function choose1() {
    // (중요) 틀렸을 경우, 답을 finalAnswer가 아니라 이게 cups 배열에서 몇 번째인지 숫자로 알려주도록 한다.
    if (cups[0] == finalAnswer) {
        youCorrect();
    } else {
        youWrong();
    };
    gameReset();
};

function choose2() {
    if (cups[1] == finalAnswer) {
        youCorrect();
    } else {
        youWrong();
    };
    gameReset();
};

function choose3() {
    if (cups[2] == finalAnswer) {
        youCorrect();
    } else {
        youWrong();
    };
    gameReset();
};

function youCorrect() {
    document.getElementById("message-monte").innerHTML = "정답입니다! 축하합니다!"
    gameData.score += 1;
    gameData.highscore += 1;
}

function youWrong() {
    document.getElementById("message-monte").innerHTML = "땡! 틀렸습니다... 정답은 " + youMissed + "번입니다.";
    gameData.score -= 1;
}

function gameReset() {
    document.getElementById("monteButton-1").style.visibility = "hidden";
    document.getElementById("monteButton-2").style.visibility = "hidden";
    document.getElementById("monteButton-3").style.visibility = "hidden";
    if (gameData.score >= gameData.highscore) {
        gameData.highscore = gameData.score;
        HighscoreUpload();
    }
    scoreUpload();
    document.getElementById("start-monte").style.visibility = "visible";
    updateScreen();
}

function clearScore() {
    if (window.confirm("현재 점수를 초기화하시겠습니까?")) {
        gameData.score = 0;
        updateScreen();
        score.respawn();
    }
};

function scoreUpload() {
    console.log("전송할 현재 점수:" + gameData.score);
    $.ajax({
        url: "/game/ajax/score_upload_monte/",
        type: "GET",
        data: {'uploadedScore': gameData.score},
        dataType: 'JSON',
        error: function (error) {
            console.log("점수가 전송되지 않았습니다.");
        },
        success: function (data) {
            console.log(data.message);
        }
    });
}

function HighscoreUpload() {
    console.log("전송할 최고 점수:" + gameData.highscore);
    $.ajax({
        url: "/game/ajax/highscore_upload_monte/",
        type: "GET",
        data: {'uploadedHighscore': gameData.highscore},
        dataType: 'JSON',
        error: function (error) {
            console.log("최고점수가 전송되지 않았습니다.");
        },
        success: function (data) {
            console.log(data.message);
        }
    });
}

function scoreDownload() {
    $.ajax({
        url: "/game/ajax/record_download_monte/",
        type: "GET",
        error: function (error) {
            console.log("회원의 점수를 찾지 못했습니다.");
        },
        success: function (data) {
            gameData.score = data.score;
            gameData.highscore = data.highScore;
            console.log("회원의 점수를 확인했습니다.");
            console.log("현재 점수:" + gameData.score + ", 최고 점수:" + data.highScore)
        }
    });
}