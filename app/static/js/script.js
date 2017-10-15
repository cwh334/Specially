var apiKey = "JRBjYMHeZm8FEz7guTXEIQuyQygFGgDf",
	paths = ["/v1/gifs/search"],
	lock = true,
	selected = null,
	limit = 3;

function onGifInput(str) {
	lock = true;
	window.setTimeout(function () {
		requestGifs(str);
		lock = false;
	}, 500);
}

function requestGifs(query) {
	var reqParams = {
			api_key: apiKey,
			q: query,
			limit: 3,
		},
		xhr = $.get("http://api.giphy.com" + paths[0] + "?" + $.param(reqParams));
	xhr.done(function (res) {
		displayGifs(res);
	});
}

function displayGifs(res) {
	$("#gif-display").html("");
	var data = res.data;
	for (var i = 0; i < data.length; i++) {
		if (data[i]) {
			$("#gif-display").append("<img src=" + data[i].images.fixed_height.url + ">");
		}
	}
}

window.onload = function () {
	$("#msgbox").on("input", function (evt) {
		$("#gif-input").val("");
		var val = $("#gif-input").val()
		val = val.slice(val.indexOf("|"));
		$("#gif-input").val(val + $(evt.target).val());
		onGifInput($("#gif-input").val());
	});
	$("#gif-input").val("|birthday dog").trigger("input");
	$("#gif-display").on("click", "img", function (data) {
		selected = $(data.target).attr("src");
		$("#gif-display img").removeClass("dark-background");
		$(this).addClass("dark-background");
		$("#url").val(selected);
	});
	$("#occasion").on("change", function (evt) {
		selected = evt.target.value;
		$("#gif-input").val(selected + "|" + $("#msgbox").val());
	});
	$("msgbox").on("input", function (evt, data) {

	});
}