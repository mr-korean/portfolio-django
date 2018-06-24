var selectedQuote = 0; // 선택된 명언의 순번 (덮어씌워짐)
var allQuotes = 0; // 저장된 명언의 총 개수 (덮어씌워짐)

var quote = {
    'original' : "Place for original quote.",
    'translated' : "번역문이 들어갈 자리입니다. (출처 - BrainyQuote)",
    'name' : "말한 사람입니다. (ex. 이홍기)",
    'order' : "선택된 문장이 몇 번째인가",
    'all': "전체 문장 개수"
};

function getCounter() {
    $.ajax({
        url: "/quote/ajax/count_all_quote/",
        type: "GET",
        error: function (error) {
            console.log("명언 집계 실패.");
        },
        success: function (data) {
            allQuotes = data.counted;
            console.log("명언 집계 성공 - 총 " + data.counted + "개");
            quote.all = allQuotes;
        }
    });
}

function quoteCheck() {
    $.ajax({
        url: "/quote/ajax/quote_download/",
        type: "GET",
        error: function (error) {
            quote.original = "An error has occured."
            quote.translated = "오류로 인해 명언을 받아오지 못했습니다.";
            quote.name = "관리자";
            quote.order = "명언";
            quote.all = "없음";
            console.log("명언 검색 실패.");
        },
        success: function (data) {
            quote.original = data.original;
            quote.translated = data.translated;
            quote.name = data.name;
            quote.order = data.selected + 1;
            console.log("명언 검색 성공.");
            document.getElementById("place-quote").innerHTML = quote.original + "<br>" + quote.translated;
            document.getElementById("place-info").innerHTML = "- " + quote.name + ", ( " + quote.order + " / " + quote.all + " )";
            console.log("명언 출력 성공.");
        }
    });
}

function startQuoteFinder() {
    getCounter();
    quoteCheck();
}